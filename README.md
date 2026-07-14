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

## Features

- Complete database of all CRIRES+ wavelength settings
- Detector-by-detector wavelength coverage visualization
- Compact broken-axis layouts for comparing multiple settings
- Molecular opacity overlays
- Atmospheric transmission and thermal emission from ESO SkyCalc
- Publication-quality figures with minimal code
- Simple object-oriented API

## Installation

Create a virtual environment

```bash
python3.12 -m venv .venv
```

**Python requirement**: CRIRESViz currently supports **Python 3.12**. This version is required for compatibility with the SkyCalc interface.
Activate it

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Upgrade pip

```bash
pip install --upgrade pip
```

To use the SkyCalc interface, install the ESO SkyCalc command-line client (`skycalc_cli`) and ensure it is available in your system PATH.

```
pip install skycalc_cli 
pip install "setuptools==80.10.2"
```

Clone the repository

```bash
git clone https://github.com/andrew070500/CRIRESViz.git
cd CRIRESViz
```

Install the package in editable mode

### Install CRIRESViz
```bash
pip install -e .
```

### Install developer tools
```bash
pip install -e ".[tools]"
```

### Install opacity-generation tools
```bash
pip install -e ".[opacity]"
```

### Install everything
```bash
pip install -e ".[all]"
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

## Examples

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


