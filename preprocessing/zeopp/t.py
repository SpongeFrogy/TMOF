import json
import pandas as pd

file = "zeo_data_.csv"

df = pd.read_csv(file, index_col=0)
print(df.shape)
new_ = pd.DataFrame(columns=df.columns)

for i in df.index:
    row = df.loc[i]["pld"].split()[1:]
    new_.loc[i] = [row[1], row[0]]
print(new_)
new_.to_csv("zeo_data_.csv")