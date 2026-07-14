import matplotlib.pyplot as plt

from criresviz import plot
from criresviz.models import CRIRESSetting

L = CRIRESSetting.from_name("L3262")
M = CRIRESSetting.from_name("M4368")
K = CRIRESSetting.from_name("K2166")

plot(L, M, K)

plt.show()
