# CRIRES+ Wavelength Settings

CRIRESViz represents every CRIRES+ wavelength setting as a `CRIRESSetting` object.

A setting contains all the information required to describe one CRIRES+ wavelength configuration, including

- observing band,
- reference wavelength,
- echelle orders,
- detector wavelength coverage.

The wavelength database is generated directly from the official ESO CRIRES+ User Manual and is included with the package.

---

# Loading a setting

Load a wavelength setting using its ESO name.

```python
from criresviz import CRIRESSetting

setting = CRIRESSetting.from_name("M4368")
```

The returned object can immediately be inspected or plotted.

```python
print(setting)
```

Example output

```text
CRIRES+ Setting
──────────────────────────────
Name:                 M4368
Band:                 M
Reference wavelength: 4.368 μm
Orders:               6
Wavelength range:     3.513–5.211 μm
```

---

# Inspecting the database

CRIRESViz includes the complete database of CRIRES+ wavelength settings.

Display every available setting

```python
CRIRESSetting.info()
```

Example

```text
Settings    Band    reference_wavelength [μm]    ...   
────────────────────────────────────────────────────────
Y1029       Y       ... 
J1226       J       ...
J1228       J       ... 
```

---

Display only one observing band

```python
CRIRESSetting.info("L")
```
---

Inspect a single setting

```python
CRIRESSetting.info("M4368")
```

This displays the metadata associated with that wavelength setting.

---

# Working with observing bands

Instead of loading a single wavelength setting, an entire observing band can be loaded as a `CRIRESBand`.

```python
from criresviz import CRIRESBand

band = CRIRESBand.from_name("M")
```

A `CRIRESBand` behaves similarly to a collection of wavelength settings.

```python
len(band)

for setting in band:
    print(setting.name)
```

---

# Detector layout

Each wavelength setting consists of several echelle orders.

Each order is composed of three detectors.

This hierarchy is represented directly inside CRIRESViz.

```
CRIRESSetting

└── Order

      ├── Detector 1

      ├── Detector 2

      └── Detector 3
```

To access individual detectors:

```python
order = setting.get_order(18)

for detector in order:
    print(detector)
```

---

# Coverage

The fraction of detector wavelength occupied by the opacity regions of one or more molecules can be computed directly.

```python
co = Molecule.from_name("CO")

setting.coverage(co)
```

Output

```text
Species      Coverage
─────────────────────
CO            55.69 %
```

Multiple molecules may be evaluated simultaneously.

```python
setting.coverage(
    co,
    h2o,
    co2,
)
```

If no molecules are provided, every available molecule is evaluated.

```python
setting.coverage()
```

---

# Ranking wavelength settings

CRIRESViz can rank every CRIRES+ wavelength setting according to the wavelength coverage of a molecular species.

```python
CRIRESSetting.rank(co)
```

The returned table contains every wavelength setting ordered from best to worst.

If a SkyCalc atmospheric model is provided,

```python
sky = Sky.from_skycalc()

CRIRESSetting.rank(
    co,
    sky=sky,
)
```

the ranking also includes atmospheric transmission and thermal emission.

---

# Selecting the best wavelength setting

The highest-ranked setting can be obtained directly.

```python
best = CRIRESSetting.find_best_setting(co)
```

or

```python
best = CRIRESSetting.find_best_setting(
    co,
    sky=sky,
)
```

This provides a convenient starting point for observation planning.

---

# Public interface

The main methods of `CRIRESSetting` are

| Method | Description |
|----------|-------------|
| `from_name()` | Load one wavelength setting |
| `info()` | Inspect the wavelength-setting database |
| `coverage()` | Compute molecular wavelength coverage |
| `rank()` | Rank all settings for a molecule |
| `find_best_setting()` | Return the highest-ranked setting |

The main methods of `CRIRESBand` are

| Method | Description |
|----------|-------------|
| `from_band()` | Load an observing band |
| `coverage()` | Compute molecular coverage across every setting |
| `rank()` | Rank settings belonging to the band |
| `find_best_setting()` | Return the highest-ranked setting in the band |
