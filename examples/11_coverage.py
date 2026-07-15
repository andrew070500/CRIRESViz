from criresviz import (
    CRIRESSetting,
    CRIRESBand,
    Molecule,
)

setting = CRIRESSetting.from_name("M4368")

co = Molecule.from_name("CO")
h2o = Molecule.from_name("H2O")

setting.coverage(co)

print()

setting.coverage(co, h2o)

print()

setting.coverage()

print()

band = CRIRESBand.from_band("M")

band.coverage(co)

print()

band.coverage()

print()
