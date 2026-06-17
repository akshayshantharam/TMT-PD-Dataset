import pandas as pd, sys
f=sys.argv[1]; df=pd.read_excel(f)
print(df['Event Duration [ms]'].describe())
