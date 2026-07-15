# Introduction

## What is CRIRESViz?

**CRIRESViz** is an open-source Python package for visualizing the wavelength coverage of the ESO CRIRES+ high-resolution near-infrared spectrograph together with molecular opacity regions and atmospheric transmission models.

The package was developed to simplify one of the most common tasks in high-resolution infrared spectroscopy: determining which wavelength range is best suited to observe a given molecular species under realistic atmospheric conditions.

Rather than working directly with instrument manuals, wavelength tables, and atmospheric transmission files, CRIRESViz provides a simple object-oriented interface that allows these different pieces of information to be combined into a single visualization.

---

## Motivation

Planning observations with CRIRES+ typically requires combining information from several independent sources:

- the CRIRES+ wavelength-setting tables from the ESO User Manual,
- molecular opacity spectra,
- atmospheric transmission,
- atmospheric thermal emission.

Although all of this information is publicly available, it is usually distributed across different files, software packages, or online tools, making observation planning unnecessarily time-consuming.

CRIRESViz brings all these components together into a unified Python interface.

---

## Structure

Every physical entity in CRIRESViz is represented by a Python object.

For example,

- a CRIRES+ wavelength setting is a `CRIRESSetting`,
- a collection of wavelength settings is a `CRIRESBand`,
- a molecular opacity profile is a `Molecule`,
- an atmospheric model is a `Sky`.

These objects can then be combined naturally:

```python
setting = CRIRESSetting.from_name("M4368")

co = Molecule.from_name("CO")

sky = Sky.from_skycalc()

plot(setting, co, sky=sky)
```

The plotting interface never needs to know where the data originated. It simply combines the objects provided by the user.

---

## Main capabilities

CRIRESViz currently provides

- complete database of all CRIRES+ wavelength settings and orders,
- molecular opacity overlays,
- atmospheric transmission and thermal emission from ESO SkyCalc,
- compact broken-axis layouts,
- molecular wavelength coverage calculations,
- automatic ranking of wavelength settings for a given molecule,
- observation-planning utilities.

---

## Typical workflow

A typical CRIRESViz workflow consists of four steps.

### 1. Load a wavelength setting

```python
setting = CRIRESSetting.from_name("M4368")
```

or load an entire observing band

```python
band = CRIRESBand.from_name("M")
```

---

### 2. Load one or more molecules

```python
co = Molecule.from_name("CO")

h2o = Molecule.from_name("H2O")
```

---

### 3. Generate or load an atmospheric model

```python
sky = Sky.from_skycalc()

sky = Sky.from_file('\path\to\file')
```

---

### 4. Visualize or evaluate the observation

```python
plot(setting, co, sky=sky)
```

```python
CRIRESSetting.rank(
    co,
    sky=sky,
)
```

---

## Package structure

The package is organized into a small number of independent modules.

| Module | Purpose |
|---------|---------|
| `models` | Scientific objects such as CRIRES settings, molecules, detectors, and sky models |
| `plotting` | Visualization routines |
| `database` | CRIRES+ wavelength-setting database |
| `skycalc` | Interface to ESO SkyCalc |
| `examples` | Complete usage examples |
| `tools` | Utilities used to generate the package databases |

---

## Design goals

CRIRESViz was designed to be

- easy to learn,
- easy to extend,
- publication-oriented,
- useful for observation planning,
- independent of any data-reduction pipeline.

Although originally developed for CRIRES+, the overall design could be adapted to other high-resolution spectrographs in the future.
