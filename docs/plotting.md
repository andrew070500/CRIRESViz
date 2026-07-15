# Plotting

The central plotting function of CRIRESViz is

```python
plot(...)
```

Every scientific object in the package can be passed directly to this function.

The plotting interface automatically recognizes the supplied objects and renders the corresponding visualization.

This object-oriented design allows increasingly complex figures to be created without changing the plotting syntax.

---

# Plotting a wavelength setting

The simplest figure contains only a CRIRES+ wavelength setting.

```python
setting = CRIRESSetting.from_name("M4368")

plot(setting)
```

This displays the wavelength coverage of every detector.

---

# Plotting multiple settings

Multiple wavelength settings can be displayed simultaneously.

```python
plot(
    setting1,
    setting2,
)
```

Each setting is automatically assigned a different color.

---

# Plotting an observing band

Entire observing bands can be plotted directly.

```python
band = CRIRESBand.from_name("M")

plot(band)
```

This visualizes every wavelength setting belonging to the selected CRIRES+ observing band.

---

# Adding molecules

Molecular opacity regions can be overlaid simply by passing one or more `Molecule` objects.

```python
plot(
    setting,
    Molecule.from_name("CO"),
)
```

Multiple molecules

```python
plot(
    setting,
    Molecule.from_name("CO"),
    Molecule.from_name("H2O"),
    Molecule.from_name("CO2"),
)
```

Each molecular species is automatically assigned its predefined color.

---

# Adding atmospheric transmission

Atmospheric transmission is displayed by supplying a `Sky` object.

```python
sky = Sky.from_skycalc()

plot(
    setting,
    sky=sky,
)
```

---

# Displaying thermal emission

The sky panel can also display atmospheric radiance.

```python
plot(
    setting,
    sky=sky,
    sky_mode="radiance",
)
```

---

# Combining everything

Any combination of supported objects can be plotted together.

```python
plot(
    setting1,
    setting2,
    Molecule.from_name("CO"),
    Molecule.from_name("H2O"),
    sky=sky,
)
```

This produces a complete observation-planning figure containing

- detector wavelength coverage,
- molecular opacity,
- atmospheric transmission or emission.

---

# Compact layout

When several wavelength settings are displayed, the compact layout removes the large wavelength gaps between them.

```python
plot(
    setting1,
    setting2,
    compact=True,
)
```

The wavelength scale remains correct for each setting while minimizing unused figure space.

This layout is particularly useful when comparing multiple settings from the same observing band.

---

# Figure customization

Because CRIRESViz uses standard Matplotlib axes, every figure can be customized after plotting.

For example,

```python
fig, ax = plot(setting)

ax.set_title("CO in M4368")

plt.show()
```

Standard Matplotlib commands can be used to modify.

---

# Typical plotting workflows



### Observation planning

```python
plot(
    setting,
    co,
    sky=sky,
)
```

---

### Compare wavelength settings

```python
plot(
    setting1,
    setting2,
    compact=True,
)
```

---

### Compare molecular tracers

```python
plot(
    setting,
    co,
    h2o,
    co2,
)
```

---

### Complete observation overview

```python
plot(
    setting1,
    setting2,
    co,
    h2o,
    sky=sky,
    compact=True,
)
```

---

# Supported objects

The plotting function currently accepts

| Object | Purpose |
|---------|---------|
| `CRIRESSetting` | Plot one wavelength setting |
| `CRIRESBand` | Plot every setting in an observing band |
| `Molecule` | Overlay molecular opacity regions |
| `Sky` | Display atmospheric transmission or radiance |

Objects may be supplied in any order.

---

# Philosophy

The plotting API intentionally consists of a single high-level function.

Rather than requiring separate plotting routines for settings, molecules, or sky models, every scientific object is responsible only for storing its data.

The plotting function simply combines those objects into a consistent visualization.

This keeps the public interface small while remaining highly flexible.
