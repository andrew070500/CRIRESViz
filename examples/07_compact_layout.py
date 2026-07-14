import matplotlib.pyplot as plt

from criresviz import plot
from criresviz.models import CRIRESSetting

M = CRIRESSetting.from_name("M4368")
L = CRIRESSetting.from_name("L3262")
K = CRIRESSetting.from_name("K2166")

plot(
    L,
    M,
    K,
    layout="compact",
)

plt.show()
