import matplotlib.pyplot as plt

from criresviz import plot
from criresviz.models import CRIRESSetting, Molecule

setting = CRIRESSetting.from_name("M4368")

co = Molecule.from_name("CO")
ch4 = Molecule.from_name("CH4")
sio = Molecule.from_name("SiO")

print(setting)
print()
print(co)
print()
print(ch4)
print()
print(sio)
print()
print(f"Plotting {setting.name}, {co.name}, {ch4.name}, and {sio.name}")
print()

plot(setting, ch4, co, sio)

plt.show()
