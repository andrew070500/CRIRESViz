import pandas as pd
import matplotlib.pyplot as plt

from criresviz.common import OPACITY


df = pd.read_csv(f"{OPACITY}/CO.csv")

plt.figure(figsize=(12,4))

plt.plot(
    df["wavelength_um"],
    df["normalized_opacity"]
)

plt.xlabel("Wavelength (μm)")
plt.ylabel("Normalized opacity")

plt.xlim(4,5)

plt.show()
