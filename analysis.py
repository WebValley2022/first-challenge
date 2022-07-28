import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("APPA data merged.csv")

print(type(df["Data"][0]))

"""
plt.bar(df["Data"], df["Valore"])
plt.title('Prova')
plt.show()
"""

