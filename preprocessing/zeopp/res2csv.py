import os
import pandas as pd
import fnmatch


folder = "cifs/"


zeo_data = pd.DataFrame(columns=["pld", "lcd"])
for file in os.listdir(folder):
    if fnmatch.fnmatch(file, "*.res"):
        with open(os.path.join(folder, file)) as f:
            zeo_data.los[file[:-4]] = f.readline()[1:-1]
zeo_data.to_csv("zeo_data.csv")
