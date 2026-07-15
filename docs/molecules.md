# Molecules

CRIRESViz represents every molecular species as a `Molecule` object.

A molecule stores the wavelength regions where its opacity is significant, allowing these regions to be visualized together with CRIRES+ wavelength settings and atmospheric models.

CRIRESViz does **not** compute opacities on the fly during plotting. Instead, the opacity regions are precomputed once and stored in a lightweight database, making plotting instantaneous.

---

# Available molecules

Display every available molecular species

```python
from criresviz import Molecule

Molecule.available()
```

---

# Loading a molecule

Load a molecule using its chemical formula.

```python
co = Molecule.from_name("CO")
```

The returned object contains all the information required for plotting.

```python
print(co)
```

Example output

```text
Molecule
──────────────────────────────
Name:              CO
Temperature:       1500 K
Pressure:          1.0 bar
Wavelength range:  0.80–5.60 μm
```

---

# Plotting molecules

A molecule can be plotted directly together with one or more CRIRES+ settings.

```python
setting = CRIRESSetting.from_name("M4368")

co = Molecule.from_name("CO")

plot(
    setting,
    co,
)
```

Multiple molecules can be overlaid simultaneously.

```python
plot(
    setting,
    co,
    Molecule.from_name("H2O"),
    Molecule.from_name("CO2"),
)
```

---

# Active regions

Internally, every molecule is represented by a collection of wavelength intervals.

```python
co.active_regions
```

returns

```python
[
    (4.51, 4.63),
    (4.68, 4.74),
    ...
]
```

These regions correspond to wavelength intervals where the molecular opacity exceeds a predefined threshold.

---

# How the opacity regions were generated

The molecular database distributed with CRIRESViz was generated using **petitRADTRANS** in line-by-line (`lbl`) mode.

For each molecule,

- a high-resolution opacity spectrum was computed,
- the continuum was removed using a rolling median,
- the spectrum was smoothed,
- significant opacity regions were identified above a user-defined threshold,
- adjacent regions were merged.

The resulting wavelength intervals are stored as JSON files and loaded automatically by `Molecule.from_name()`.

---

# Adding new molecules

Additional molecular species can be generated using the tools included in the repository.

The script

```text
tools/compute_opacity.py
```

computes the opacity regions using petitRADTRANS and stores them inside

```text
resources/generated/opacity/
```

Once generated, the new molecule immediately becomes available through

```python
Molecule.from_name(...)
```

without requiring any modification to the plotting code.

To add a new molecule:

- modify the `MOLECULES` entry in `tools/config.py` adding the chemical formula of the molecule of interest (e.g. O3),
- run `python3 tools/compute_opacity.py`,
- call the new molecule using `Molecule.from_name(...)`.

**N.B.**: if you plan on using the `/tools/` scripts, run `pip install -e ".[all]"` when installing CRIRESViz.  

---

# Public interface

The `Molecule` class provides a small public interface.

| Method | Description |
|----------|-------------|
| `available()` | List all available molecular species |
| `from_name()` | Load one molecule from the database |

The most commonly used attributes are

| Attribute | Description |
|-----------|-------------|
| `name` | Molecular species |
| `active_regions` | Significant opacity intervals |
| `temperature` | Temperature used to generate the opacity |
| `pressure` | Pressure used to generate the opacity |
| `wavelength_range` | Wavelength range covered by the database |
| `opacity_mode` | petitRADTRANS opacity mode |
| `threshold` | Detection threshold used during preprocessing |
