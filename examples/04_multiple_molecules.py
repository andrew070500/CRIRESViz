import matplotlib.pyplot as plt

from criresviz import plot
from criresviz.models import CRIRESSetting, Molecule

setting = CRIRESSetting.from_name("M4368")

co = Molecule.from_name("CO")
ch4 = Molecule.from_name("CH4")
sio = Molecule.from_name("SiO")

plot(setting, ch4, co, sio)

plt.show()
