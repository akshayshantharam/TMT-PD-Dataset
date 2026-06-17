import pandas as pd, matplotlib.pyplot as plt, sys
f=sys.argv[1]; df=pd.read_excel(f)
d=df.dropna(subset=['Fixation Position X [px]','Fixation Position Y [px]']).head(100)
plt.plot(d['Fixation Position X [px]'],d['Fixation Position Y [px]'], marker='o'); plt.gca().invert_yaxis(); plt.savefig('scanpath.png')
