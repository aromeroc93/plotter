import pandas as pd
import matplotlib.pyplot as plt
import sys

ftp = input("File to plot: ")
route = "/mnt/c/Users/Laboratorio/Desktop/"

df = pd.read_excel("/mnt/c/Users/Laboratorio/Desktop/Cromatogramas/" + ftp + ".xls", sheet_name="Curves", header=2, decimal=',')
print(df)

plt.plot(df["ml"], df[" mAU"], color="#0073b8")
name = input("Insert plot name: ")
for ml, frac in zip(df["ml.1"], df["(Fractions)"]):
    plt.axvline(x = ml, ymax= 0.05, label=frac)
plt.title(name)
plt.xlabel("ml")
plt.ylabel("mAU")

plt.show()
