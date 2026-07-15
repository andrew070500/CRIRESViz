from dataclasses import dataclass
from collections.abc import Iterator
from criresviz.database.loader import load_settings_database
from .molecule import Molecule
from .setting import CRIRESSetting

import pandas as pd

@dataclass(slots=True)
class CRIRESBand:
    """
    Collection of CRIRES+ wavelength settings belonging to one spectral band.

    A CRIRESBand behaves similarly to a CRIRESSetting, but contains multiple
    settings. It can be passed directly to ``plot()`` and supports utilities
    such as ``coverage()`` and ``info()``.
    """

    name: str
    settings: list

    def __iter__(self) -> Iterator:
        return iter(self.settings)

    def __len__(self) -> int:
        return len(self.settings)

    def __getitem__(self, index):
        return self.settings[index]
    
    
    @property
    def wavelength_range(self):
        """
        Overall wavelength range covered by the band.
        """
        return (
            min(s.wavelength_range[0] for s in self),
            max(s.wavelength_range[1] for s in self),
        )
    
    @property
    def orders(self):
        """
        Return every order from every setting.
        """
        return [
            order
            for setting in self
            for order in setting
        ]
    
    
    @classmethod
    def from_band(cls, band: str) -> list["CRIRESSetting"]:
        """
        Load every CRIRES+ wavelength setting belonging to one band.
    
        Parameters
        ----------
        band : str
            Spectral band identifier (e.g. "Y", "J", "H", "K", "L", "M").
    
        Returns
        -------
        list[CRIRESSetting]
            All wavelength settings in that band.
        """
        
        valid = {"Y", "J", "H", "K", "L", "M"}
        
        assert band in valid, f"Unknown band: '{band}'. Choose one of {sorted(valid)}."
    
        band = band.upper()
    
        database = load_settings_database()
    
        settings = [
            CRIRESSetting.from_name(name)
            for name, info in database.items()
            if info["band"] == band
        ]
    
        return CRIRESBand(
            name=band,
            settings=settings,
        )

    def coverage(self, *molecules, decimals=2):
        """
        Compute the detector coverage of one or more molecules.
    
        Coverage is defined as the percentage of the total detector wavelength
        covered by the active opacity regions of each molecule.
    
        Parameters
        ----------
        *molecules : Molecule
            One or more Molecule objects.
        decimals : int or None, optional
            Number of decimal places used to round the result.
    
        Returns
        -------
        float, dict[str, float], or str
            - float if a single molecule is provided.
            - dict if multiple molecules are provided.
            - formatted table if no molecules are provided.
        """
        
        lines = [
            "Species      Coverage",
            "─────────────────────",
        ]
    
        if not molecules:
            molecules = [
                Molecule.from_name(name)
                for name in Molecule.available()
            ]

    
        #
        # Merge detector wavelength intervals
        #
        intervals = []
    
        for order in self:
            for detector in order:
                intervals.append(
                    (
                        detector.wavelength_min,
                        detector.wavelength_max,
                    )
                )
    
        intervals.sort()
    
        merged = []
    
        for start, end in intervals:
    
            if not merged:
                merged.append([start, end])
    
            elif start <= merged[-1][1]:
                merged[-1][1] = max(
                    merged[-1][1],
                    end,
                )
    
            else:
                merged.append([start, end])
    
        total = sum(
            end - start
            for start, end in merged
        )
    
        #
        # Compute molecular coverage
        #
        results = {}
    
        for molecule in molecules:
    
            covered = 0.0
    
            for det_start, det_end in merged:
    
                for mol_start, mol_end in molecule.active_regions:
    
                    covered += max(
                        0.0,
                        min(det_end, mol_end)
                        - max(det_start, mol_start),
                    )
    
            value = 100 * covered / total
    
            if decimals is not None:
                value = round(value, decimals)
    
            results[molecule.name] = value
    
        #
        # Return result
        #
        
        for name, value in sorted(results.items()):
                lines.append(f"{name:<10} {value:>7.2f} %")
                
        table = "\n".join(lines)
        print(table)
        
        
    @classmethod
    def rank(cls, self, molecule, sky=None, verbose=True):
        
        rows = []
        
        database = load_settings_database()
        
        for name, info in database.items():

            if info["band"] == self.name:        
                setting = CRIRESSetting.from_name(name)
            
                coverage = setting.coverage(
                    molecule,
                    verbose=False,
                )
            
                row = {
                    "Setting": name,
                    "Coverage": coverage,
                }
            
                if sky is not None:
            
                    transmission = sky.mean_transmission(wavelength_range=setting.wavelength_range)
            
                    radiance = sky.mean_radiance(wavelength_range=setting.wavelength_range)
                    max_radiance = sky.radiance.max()
                    radiance_score = 1 - radiance / max_radiance
    
                    score = coverage * transmission * radiance_score
            
                    row["Transmission"] = transmission
                    row["Radiance Score"] = radiance_score
                    row["Score"] = score
            
                else:
            
                    row["Score"] = coverage
            
                rows.append(row)
        
        results = pd.DataFrame(rows)
        results = results.sort_values(
            by="Score",
            ascending=False,
        ).reset_index(drop=True)
        pd.options.display.float_format = "{:,.2f}".format
        
        if verbose:
            print(results)
            
        return results
    
    @classmethod
    def find_best_setting(cls, self, molecule, sky=None):
        """
        Return the best ranked setting, according
        to the score derived in the rank function
        """
        rank = cls.rank(self, molecule, sky=sky, verbose=False)

        print(rank.iloc[0])

        return rank.iloc[0]
    
    def __str__(self):
    
        wmin, wmax = self.wavelength_range
    
        return (
            "CRIRES+ Band\n"
            "──────────────────────────────\n"
            f"Band:               {self.name}\n"
            f"Settings:           {len(self)}\n"
            f"Wavelength range:   "
            f"{wmin:.3f}–{wmax:.3f} μm"
        )