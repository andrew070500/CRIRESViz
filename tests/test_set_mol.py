from matplotlib import pyplot as plt

from criresviz.models import (
    CRIRESSetting,
    Molecule,
)

setting = CRIRESSetting.from_name("M4368")
co = Molecule.from_name("CO")

fig, ax = plt.subplots(figsize=(12,6))

setting.plot(ax=ax)

co.plot(ax=ax, threshold=0.50)


plt.show()
