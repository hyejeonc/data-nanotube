import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pandas as pd



plt.figure(1)
df = pd.read_csv("neg_pos_40_table_rev0.csv")
barcolor = ['darkorange', 'royalblue']
df21 = df.pivot('ph', 'structure', 'reeavg')
df22 = df.pivot('ph', 'structure', 'reeerr')
print(df21)
print(df22)
df2 = df21.plot(kind='bar', color=barcolor, yerr=df22, \
                error_kw=dict(ecolor='gray',elinewidth=0.5) )
df2.set_ylim(100, 240)
df2.set_ylabel(r'$<R_{ee}>$')
df2.set_xlabel(r'$pH$')
df2.set_xticklabels(['2','3','4','5','6','7','8'], rotation=0)
df2.legend(['neg', 'pos'])

#plt.savefig('fig/reebar_neg_pos_40_rev1.pdf')


plt.figure(2)
df = pd.read_csv("neg_pos_40_table_rev0.csv")
barcolor = ['darkorange', 'royalblue']
#barcolor = ['darkorange', 'gold', 'royalblue', 'lightblue']
df11 = df.pivot('ph', 'structure', 'rgavg')
df12 = df.pivot('ph', 'structure', 'rgerr')
df1 = df11.plot(kind='bar', color=barcolor, yerr=df12, \
                error_kw=dict(ecolor='gray',elinewidth=0.5) )
#df1.setp(elinewidth=0.5, ecolor='gray' )
print(df11)
print(df12)

'''
df1.set_ylim(40, 70)
df1.set_ylabel(r'$<R_{g}>$')
df1.set_xlabel(r'$pH$')
df1.set_xticklabels(['2','3','4','5','6','7','8'], rotation=0)
df1.legend(['neg','pos'])
#df1.legend(['neg, in', 'neg, out', 'pos, in', 'pos, out'])
plt.savefig('fig/rgbar_neg_pos_40_rev1.pdf')

plt.show()
'''