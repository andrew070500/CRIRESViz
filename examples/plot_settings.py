from matplotlib import pyplot as plt

from criresviz import CRIRESSetting

setting = CRIRESSetting.from_name("M4368")

setting.plot()

plt.show()

