# CRIRESViz

**CRIRESViz** is a Python package for visualizing the wavelength coverage of the **ESO CRIRES+** high-resolution near-infrared spectrograph together with molecular opacity bands and atmospheric transmission models.

It follows a simple object-oriented design: wavelength settings, molecules, and atmospheric models are represented by Python objects that can be combined naturally in the plotting interface.

The package combines:

- CRIRES+ wavelength settings
- detector footprints
- molecular absorption regions
- ESO SkyCalc atmospheric transmission and radiance

into a single, simple plotting interface.

CRIRESViz is designed for astronomers working with CRIRES+ observations, atmospheric retrievals, and observation planning, but can also serve as a lightweight visualization tool for high-resolution molecular spectroscopy.


## Contents

- Features
- Installation
- Quick Start
- Examples
- Citation
- License

## Features

- Complete database of all CRIRES+ wavelength settings
- Detector-by-detector wavelength coverage visualization
- Compact broken-axis layouts for comparing multiple settings
- Molecular opacity overlays
- Atmospheric transmission and thermal emission from ESO SkyCalc
- Publication-quality figures with minimal code
- Simple object-oriented API

## Installation

Clone the repository

```bash
git clone https://github.com/AndreaBarone/CRIRESViz.git
cd CRIRESViz
```

Install the package in editable mode

```bash
pip install -e .
```

To use the SkyCalc interface, install the ESO SkyCalc command-line client (`skycalc_cli`) and ensure it is available in your system PATH.

```
skycalc_cli
```

## Quick Start

```python
from criresviz import plot
from criresviz.models import (
    CRIRESSetting,
    Molecule,
    Sky,
)

setting = CRIRESSetting.from_name("M4368")
co = Molecule.from_name("CO")

sky = Sky.from_skycalc()

plot(
    setting,
    co,
    sky=sky,
)

plt.show()
```

## API examples

The plotting interface accepts any combination of CRIRES+ settings, molecular opacity regions, and atmospheric models.

```plot(setting)

plot(setting, molecule)

plot(setting, sky=sky)

plot(setting1, setting2)

plot(setting1, setting2, molecule)

plot(
    setting1,
    setting2,
    molecule1,
    molecule2,
    sky=sky,
)
```

Every object in CRIRESViz is independent and reusable. A `CRIRESSetting`, `Molecule`, or `Sky` instance can be created once and reused across multiple figures, making it easy to explore different combinations interactively.
This flexible object-oriented design makes it straightforward to build increasingly complex visualizations without changing the plotting API.


