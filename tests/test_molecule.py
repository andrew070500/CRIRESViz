from matplotlib import pyplot as plt

from criresviz.models.molecule import Molecule

co = Molecule.from_name("CO")

co.plot(threshold=0.30)
print(co.active_regions())

plt.show()
