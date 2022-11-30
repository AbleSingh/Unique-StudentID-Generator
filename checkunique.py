import pandas as pd
df = pd.read_csv ('uniqueID.csv')
print(df.head())
IDlist = df["StudentID"].tolist()
print(len(IDlist))
print(len(list(set(IDlist))))