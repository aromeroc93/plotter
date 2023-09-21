import pandas as pd
import matplotlib.pyplot as plt
import sys

ftp = input("File to plot: ")

df = pd.read_csv(ftp + ".csv", sep=";", header=2)

plt.plot(df["ml"], df["mAU"], color="#0073b8")
plt.title(ftp)
plt.xlabel("ml")
plt.ylabel("mAU")

plt.show()
