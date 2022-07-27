import pandas as pd

df = pd.read_csv("APPA data merged.csv")
df = df.sort_values(by=["Stazione", "Inquinante", "Data", "Ora"])
