import matplotlib.pyplot as plt

from criresviz import plot
from criresviz.models import CRIRESSetting, Molecule, Sky


L = CRIRESSetting.from_name("L3262")
M = CRIRESSetting.from_name("M4368")
K = CRIRESSetting.from_name("K2166") 

CO = Molecule.from_name("CO")
H2O = Molecule.from_name("H2O")
SiO = Molecule.from_name("SiO")
CH4 = Molecule.from_name("CH4")

#sky = Sky.from_file("../resources/generated/sky/output.fits")
sky = Sky.from_skycalc(airmass=1.5)
print(sky)

ax = plot(L)
plt.show()

ax=plot(CO)
plt.show()

ax = plot(L, M, K, layout='compact', sky=sky, sky_mode='radiance')
plt.show()

ax=plot(L, M,CO, H2O, sky=sky)
plt.show()

ax = plot(L, M, SiO, CH4, layout='compact', sky=sky)
plt.show()

ax = plot(M, sky=sky)
plt.show()
