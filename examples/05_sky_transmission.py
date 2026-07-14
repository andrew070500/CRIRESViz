import matplotlib.pyplot as plt

from criresviz import plot
from criresviz.models import CRIRESSetting, Sky

setting = CRIRESSetting.from_name("M4368")
sky = Sky.from_skycalc()

plot(
    setting,
    sky=sky,
)

plt.show()
