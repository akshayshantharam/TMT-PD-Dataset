import pandas as pd, matplotlib.pyplot as plt
import sys
f=sys.argv[1]
df=pd.read_excel(f)
df=df.dropna(subset=['Fixation Position X [px]','Fixation Position Y [px]'])
plt.hist2d(df['Fixation Position X [px]'],df['Fixation Position Y [px]'],bins=50)
plt.gca().invert_yaxis(); plt.savefig('heatmap.png')
