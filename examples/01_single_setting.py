import matplotlib.pyplot as plt

from criresviz import plot
from criresviz.models import CRIRESSetting

setting = CRIRESSetting.from_name("M4368")

print(setting)
print()
print(f"Plotting {setting.name}...")
print()

plot(setting)

plt.show()
