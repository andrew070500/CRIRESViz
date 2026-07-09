from matplotlib import pyplot as plt

from criresviz.models.molecule import Molecule

co = Molecule.from_name("CO")
h2o = Molecule.from_name("H2O")
nh3 = Molecule.from_name("NH3")
sio = Molecule.from_name("SiO")
co2 = Molecule.from_name("CO2")
ch4 = Molecule.from_name("CH4")

ax = co.plot()
h2o.plot(ax)
nh3.plot(ax)
sio.plot(ax)
co2.plot(ax)
ch4.plot(ax)

plt.show()
