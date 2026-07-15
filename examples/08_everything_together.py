import matplotlib.pyplot as plt

from criresviz import plot
from criresviz.models import CRIRESSetting, Molecule, Sky

M = CRIRESSetting.from_name("M4368")
L = CRIRESSetting.from_name("L3262")
K = CRIRESSetting.from_name("K2166")

co = Molecule.from_name("CO")
ch4 = Molecule.from_name("CH4")
sio = Molecule.from_name("SiO")

sky = Sky.from_skycalc(
    airmass=1.5,
)


print(L)
print()
print(M)
print()
print(K)
print()
print(co)
print()
print(ch4)
print()
print(sio)
print()
print(f"Plotting {L.name}, {M.name}, {K.name}, {co.name}, {ch4.name}, {sio.name}, and atmospheric transmission in 'compact' layout...")
print()

plot(
    L,
    M,
    K,
    co,
    sio,
    ch4,
    sky=sky,
    layout="compact",
)

plt.show()
