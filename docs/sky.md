# Sky Models

CRIRESViz represents atmospheric models with the `Sky` class.

A `Sky` object contains both the atmospheric transmission and thermal sky emission computed with **ESO SkyCalc**. These models can be displayed together with CRIRES+ wavelength settings and molecular opacity regions, or used to rank wavelength settings for observation planning.

Unlike CRIRES+ settings and molecules, sky models are generated on demand and can be customized using the full set of SkyCalc parameters.

---

# Creating a sky model

The simplest way to generate an atmospheric model is

```python
from criresviz import Sky

sky = Sky.from_skycalc()
```

This uses the default SkyCalc configuration distributed with CRIRESViz.

The generated model is automatically stored locally and loaded into a `Sky` object.

---

# Custom SkyCalc parameters

Any SkyCalc parameter can be overridden.

For example

```python
sky = Sky.from_skycalc(
    airmass=1.5,
    pwv=2.5,
)
```

creates a sky model for an airmass of 1.5 and a precipitable water vapour content of 2.5 mm.

The complete list of supported parameters is available in the SkyCalc documentation.

---

# Loading an existing model

Previously generated SkyCalc models can also be loaded directly.

```python
sky = Sky.from_file("sky_model.fits")
```

This avoids recomputing the atmospheric model.

---

# Plotting atmospheric transmission

The atmospheric transmission can be displayed together with CRIRES+ wavelength settings.

```python
plot(
    setting,
    sky=sky,
)
```

This is particularly useful for identifying wavelength regions strongly affected by telluric absorption.

---

# Plotting thermal emission

Thermal sky emission can also be visualized.

```python
plot(
    setting,
    sky=sky,
    sky_mode="radiance",
)
```

This displays the atmospheric radiance predicted by SkyCalc.

---

# Combining with molecules

Sky models can be combined naturally with molecular opacity regions.

```python
plot(
    setting,
    Molecule.from_name("CO"),
    sky=sky,
)
```

This allows molecular bands to be inspected together with the expected atmospheric transmission.

---

# Mean transmission

The average atmospheric transmission over a wavelength interval can be computed directly.

```python
sky.mean_transmission(
    wavelength_range=setting.wavelength_range,
)
```

This quantity is used internally when ranking CRIRES+ wavelength settings.

---

# Mean radiance

Similarly, the average thermal emission over a wavelength interval can be obtained with

```python
sky.mean_radiance(
    wavelength_range=setting.wavelength_range,
)
```

This provides a simple estimate of the thermal background expected within a given wavelength range.

---

# Observation planning

The atmospheric model can be incorporated directly into the ranking of wavelength settings.

```python
CRIRESSetting.rank(
    Molecule.from_name("CO"),
    sky=sky,
)
```

When a sky model is supplied, CRIRESViz evaluates each wavelength setting using

- molecular wavelength coverage,
- atmospheric transmission,
- atmospheric thermal emission.

This produces a ranking that is more representative of real observing conditions than wavelength coverage alone.

---

# Public interface

The `Sky` class provides the following public constructors.

| Method | Description |
|----------|-------------|
| `from_skycalc()` | Generate a SkyCalc model |
| `from_file()` | Load an existing SkyCalc FITS file |

The most commonly used methods are

| Method | Description |
|----------|-------------|
| `mean_transmission()` | Mean atmospheric transmission over a wavelength range |
| `mean_radiance()` | Mean atmospheric radiance over a wavelength range |

The most commonly used attributes are

| Attribute | Description |
|-----------|-------------|
| `wavelength` | Wavelength grid |
| `transmission` | Atmospheric transmission |
| `radiance` | Atmospheric thermal emission |

---

# Notes

CRIRESViz requires the ESO **SkyCalc command-line client** (`skycalc_cli`) to generate new atmospheric models.

Once a model has been computed, it can be reused indefinitely without calling SkyCalc again.
