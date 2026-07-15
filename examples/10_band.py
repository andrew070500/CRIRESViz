import matplotlib.pyplot as plt
from criresviz import (
    CRIRESBand,
    Molecule,
    plot,
)

L = CRIRESBand.from_band("L")
h2o = Molecule.from_name("H2O")

print(L)
print()
print(h2o)
print()
print(f"Plotting {L.name} and {h2o.name}...")
print()

plot(L, h2o)
plt.show()
