import numpy as np    
          # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import seaborn as sns
# Say, "the default sans-serif font is COMIC SANS"
#matplotlib.rcParams['font.sans-serif'] = "Comic Sans MS"
# Then, "ALWAYS use sans-serif fonts"
#matplotlib.rcParams['font.family'] = "sans-serif"


plt.figure(1)

df = pd.read_csv("spssdata/all_spss_rev1.csv")
#df.head()
#df.info()
#df.describe()
#df.columns
dfscatter = df[['block', 'chnet', 'abs_chnet', 'coredist', 'mon', 'ph', 'tube', 'sym']]
sns.pairplot(dfscatter)


'''
barcolor = ['darkorange', 'gold', 'royalblue', 'lightblue']
df21 = df.pivot('ph', 'structure', 'reeavg')
#df22 = df.pivot('ph', 'reeerr')
print(df21)
#print(df22)
df2 = df.plot.scatter(x='ph', y='rgavg')#, color=barcolor)#, yerr=df22, \
#                error_kw=dict(ecolor='gray',elinewidth=0.5) )
#df2.set_ylim(100, 240)

df2.set_ylabel(r'$<R_{ee}>$')
df2.set_xlabel(r'$pH$')
#df2.legend(['neg, in', 'neg, out', 'pos, in', 'pos, out'])
#plt.savefig('fig/scatter_ph_rev0.pdf')
'''

'''
df3 = df.plot.scatter(x='block', y='reeavg')
df3.text(79,0.037, r'(b)', fontsize=10)
df4 = df.plot.scatter(x='chnet', y='reeavg')
df5 = df.plot.scatter(x='abs_chnet', y='reeavg')
df6 = df.plot.scatter(x='coredist', y='reeavg')
df7 = df.plot.scatter(x='mon', y='reeavg')
df8 = df.plot.scatter(x='ph', y='reeavg')

df9 = df.plot.scatter(x='tube', y='reeavg')
df10 = df.plot.scatter(x='sym', y='reeavg')
'''
'''
df3 = df.plot.scatter(x='block', y='inadschain')
df4 = df.plot.scatter(x='chnet', y='inadschain')
df5 = df.plot.scatter(x='abs_chnet', y='inadschain')
df6 = df.plot.scatter(x='coredist', y='inadschain')
df7 = df.plot.scatter(x='mon', y='inadschain')
df8 = df.plot.scatter(x='ph', y='inadschain')

df9 = df.plot.scatter(x='tube', y='inadschain')
df10 = df.plot.scatter(x='sym', y='inadschain')
'''
'''
plt.figure(2)
df = pd.read_csv("inout_spss_rev6.csv")
barcolor = ['darkorange', 'gold', 'royalblue', 'lightblue']
df11 = df.pivot('ph', 'structure', 'rgavg')
df12 = df.pivot('ph', 'structure', 'rgerr')
df1 = df11.plot(kind='bar', color=barcolor, yerr=df12, \
                error_kw=dict(ecolor='gray',elinewidth=0.5) )
#df1.setp(elinewidth=0.5, ecolor='gray' )
df1.set_ylim(40, 70)
df1.set_ylabel(r'$<R_{g}>$')
df1.set_xlabel(r'$pH$')
df1.legend(['neg, in', 'neg, out', 'pos, in', 'pos, out'])
plt.savefig('fig/scatter_ph_rev0.pdf.pdf')
'''
plt.show()