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
- Molecular opacity overlays
- Atmospheric transmission and thermal emission from ESO SkyCalc
- Compact broken-axis layouts for comparing multiple settings
- Publication-quality figures with minimal code
- Simple object-oriented API

## Installation

Create a virtual environment

```bash
python3 -m venv <name venv>
```

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

**SkyCalc requirement**: SkyCalc supports **setuptools v80.10.2**. This version is required to include in the download `pkg_resources`.


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

# Plot features
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

# Observations planning
```python
from criresviz import (
    CRIRESSetting,
    Molecule,
    Sky,
)

co = Molecule.from_name("CO")

# List all available settings
print(CRIRESSetting.info())

# Compute molecular coverage
setting = CRIRESSetting.from_name("M4368")
setting.coverage(co)

# Rank all settings
sky = Sky.from_skycalc()
CRIRESSetting.rank(co, sky=sky)
```

## Examples

The `examples/` directory contains a collection of self-contained scripts demonstrating the main features of CRIRESViz.

| Script | Description |
|--------|-------------|
| `01_single_setting.py` | Plot a single CRIRES+ wavelength setting |
| `02_multiple_settings.py` | Compare multiple wavelength settings |
| `03_single_molecule.py` | Overlay one molecular opacity region |
| `04_multiple_molecules.py` | Compare several molecular species |
| `05_sky_transmission.py` | Display atmospheric transmission from SkyCalc |
| `06_sky_emission.py` | Display atmospheric thermal emission from SkyCalc |
| `07_compact_layout.py` | Use the compact broken-axis layout |
| `08_everything_together.py` | Combine settings, molecules, and sky models in a single figure |
| `09_info.py` | Explore the CRIRES+ settings database and inspect individual settings | 
| `10_band.py` | Load and visualize all wavelength settings within a CRIRES+ band | 
| `11_coverage.py` | Compute molecular wavelength coverage for individual settings or complete bands |
| `12_rank.py` | Rank CRIRES+ settings according to molecular coverage and atmospheric conditions |

To execute all examples sequentially, simply run

```bash
cd examples
./run_examples.sh
```

The examples provide a quick overview of the package and serve as a starting point for building custom visualizations. 

Every object in CRIRESViz is independent and reusable. A `CRIRESSetting`, `Molecule`, or `Sky` instance can be created once and reused across multiple figures, making it easy to explore different combinations interactively.
This flexible object-oriented design makes it straightforward to build increasingly complex visualizations without changing the plotting API.







