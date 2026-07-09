import matplotlib.pyplot as plt

from criresviz import plot
from criresviz.models import CRIRESSetting, Molecule


L = CRIRESSetting.from_name("L3262")
M = CRIRESSetting.from_name("M4318")
K = CRIRESSetting.from_name("K2166") 

CO = Molecule.from_name("CO")
H2O = Molecule.from_name("H2O")


ax = plot(L)
plt.show()

ax=plot(CO)
plt.show()

ax = plot(L, M, K, layout='compact')
plt.show()

ax=plot(L, M,CO, H2O)
plt.show()

ax = plot(L, M, CO, layout='compact')
plt.show()
