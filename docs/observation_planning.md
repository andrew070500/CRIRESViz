# Observation Planning

Beyond visualization, CRIRESViz provides tools to evaluate CRIRES+ wavelength settings for specific molecular species.

These utilities allow users to estimate

- molecular wavelength coverage,
- atmospheric transmission,
- thermal background,

and rank the available CRIRES+ settings accordingly.

---

# Molecular coverage

The simplest metric is the wavelength coverage.

```python
setting.coverage(co)
```

returns

```text
Species      Coverage
─────────────────────
CO            55.69 %
```

If no molecule is specified,

```python
setting.coverage()
```

coverage is computed for every available molecular species.

---

# Coverage for an observing band

Coverage can also be evaluated across an entire observing band.

```python
band.coverage(co)
```

This returns the molecular coverage for every wavelength setting belonging to that band.

---

# Ranking wavelength settings

The `rank()` method evaluates every CRIRES+ wavelength setting and orders them according to their suitability for observing a given molecule.

```python
CRIRESSetting.rank(co)
```

Example

```text
Setting    Coverage    Score

M4368      55.69       55.69

M4318      49.32       49.32

...
```

Without a sky model, the score corresponds to the molecular wavelength coverage.

---

# Including atmospheric transmission

A SkyCalc model can be incorporated directly.

```python
sky = Sky.from_skycalc()

CRIRESSetting.rank(
    co,
    sky=sky,
)
```

The ranking now includes

- molecular coverage,
- atmospheric transmission,
- atmospheric thermal emission.

This produces a ranking that better reflects real observing conditions.

---

# Best wavelength setting

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

The returned object is a normal `CRIRESSetting` and can immediately be plotted.

```python
plot(
    best,
    co,
    sky=sky,
)
```

---

# Typical workflow

A typical observation-planning workflow is

```python
co = Molecule.from_name("CO")

sky = Sky.from_skycalc()

ranking = CRIRESSetting.rank(
    co,
    sky=sky,
)

best = CRIRESSetting.find_best_setting(
    co,
    sky=sky,
)

plot(
    best,
    co,
    sky=sky,
)
```

This sequence

1. evaluates every CRIRES+ wavelength setting,
2. identifies the optimal setting,
3. visualizes the result.
