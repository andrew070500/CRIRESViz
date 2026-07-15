import matplotlib.pyplot as plt

from criresviz import plot
from criresviz.models import CRIRESSetting, Sky

setting = CRIRESSetting.from_name("M4368")
sky = Sky.from_skycalc()

print(setting)
print()
print(sky)
print(f"Plotting {setting.name} and atmospheric thermal emission")
print()

plot(
    setting,
    sky=sky,
    sky_mode="radiance",
)

plt.show()
