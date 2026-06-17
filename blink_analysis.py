import pandas as pd, sys
f=sys.argv[1]; df=pd.read_excel(f)
b=df[df['Category'].astype(str).str.contains('Blink', case=False, na=False)]
print('Blink count',len(b)); print('Mean duration', b['Event Duration [ms]'].mean())
