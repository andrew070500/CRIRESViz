from criresviz import (
    CRIRESSetting,
    Molecule,
    Sky,
)

co = Molecule.from_name("CO")

print("Coverage only")
CRIRESSetting.rank(co)

print()

sky = Sky.from_skycalc()

print("Including atmospheric transmission and radiance")
CRIRESSetting.rank(
    co,
    sky=sky,
)

print("Best setting including atmospheric transmission and radiance")
best = CRIRESSetting.find_best_setting(
    co,
    sky=sky,
)

print()
