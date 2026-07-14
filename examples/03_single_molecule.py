import matplotlib.pyplot as plt

from criresviz import plot
from criresviz.models import CRIRESSetting, Molecule

setting = CRIRESSetting.from_name("M4368")

co = Molecule.from_name("CO")

plot(setting, co)

plt.show()



