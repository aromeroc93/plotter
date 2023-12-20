import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme()

ftp = input("File to plot: ")
route = "/mnt/c/Users/Laboratorio/Desktop/"

df = pd.read_excel("/mnt/c/Users/Laboratorio/Desktop/Cromatogramas/" + ftp + ".xls", sheet_name="Curves", header=2, decimal=',')
print(df)

sns.lineplot(
    data=df,
    x=df["ml"], y=df[" mAU"],
)
plt.show()