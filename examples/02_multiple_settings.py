import matplotlib.pyplot as plt

from criresviz import plot
from criresviz.models import CRIRESSetting

L = CRIRESSetting.from_name("L3262")
M = CRIRESSetting.from_name("M4368")
K = CRIRESSetting.from_name("K2166")

print(L)
print()
print(M)
print()
print(K)
print()
print(f"Plotting {L.name}, {M.name}, and {K.name}...")
print()

plot(L, M, K)

plt.show()
