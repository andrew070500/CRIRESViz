# Quick Start

This guide demonstrates the basic workflow of CRIRESViz.

In just a few lines of code you can load a CRIRES+ wavelength setting, overlay molecular opacity regions, generate an atmospheric model with ESO SkyCalc, and visualize everything together.

## Import the package

```python
import matplotlib.pyplot as plt

from criresviz import (
    plot,
    CRIRESSetting,
    CRIRESBand,
    Molecule,
    Sky,
)
```

---

## Load a CRIRES+ wavelength setting

Load one of the predefined CRIRES+ settings using its ESO identifier.

```python
setting = CRIRESSetting.from_name("M4368")
```

---

## Load one or more molecules

CRIRESViz includes a database of molecular opacity regions.

```python
co = Molecule.from_name("CO")
```

You can load as many molecules as required.

```python
h2o = Molecule.from_name("H2O")

co2 = Molecule.from_name("CO2")
```

---

## Generate an atmospheric model

Atmospheric transmission and thermal emission are computed using ESO SkyCalc.

```python
sky = Sky.from_skycalc()
```

The default SkyCalc parameters are suitable for most examples, but every SkyCalc parameter can be customized.

```python
sky = Sky.from_skycalc(
    airmass=1.3,
    pwv=2.5,
)
```

---

## Create the plot

The plotting interface automatically combines all supplied objects.

```python
plot(
    setting,
    co,
    sky=sky,
)

plt.show()
```

---

## Multiple objects

Multiple wavelength settings and molecules can be plotted simultaneously.

```python
setting1 = CRIRESSetting.from_name("L3262")
setting2 = CRIRESSetting.from_name("L3340")

co = Molecule.from_name("CO")
h2o = Molecule.from_name("H2O")

plot(
    setting1,
    setting2,
    co,
    h2o,
    sky=sky,
)

plt.show()
```

---

## Working with observing bands

Entire CRIRES+ observing bands can be loaded with a single command.

```python
band = CRIRESBand.from_name("M")

plot(band)
```

This visualizes every wavelength setting belonging to the selected observing band.

---

## Observation planning

CRIRESViz also provides utilities for evaluating wavelength settings.

Compute the wavelength coverage of a molecule

```python
setting.coverage(co)
```

Rank all CRIRES+ settings

```python
CRIRESSetting.rank(co)
```

Include atmospheric transmission

```python
CRIRESSetting.rank(
    co,
    sky=sky,
)
```

---

## Next steps

The following chapters describe each component of CRIRESViz in detail.

- CRIRES+ Settings
- Molecules
- Sky Models
- Plotting
- Observation Planning
- API Reference
