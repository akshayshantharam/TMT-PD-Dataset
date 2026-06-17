import pandas as pd
import sys
f=sys.argv[1]
df=pd.read_excel(f)
print(df.head())
print(df.columns.tolist())
