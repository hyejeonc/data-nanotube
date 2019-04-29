import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pandas as pd



plt.figure(1)
df = pd.read_csv("inout_table_rev0.csv")
barcolor = ['darkorange', 'gold', 'royalblue', 'lightblue']
df21 = df.pivot('ph', 'structure', 'reeavg')
df22 = df.pivot('ph', 'structure', 'reeerr')
print(df21)
print(df22)
df2 = df21.plot(kind='bar', color=barcolor, yerr=df22, \
                error_kw=dict(ecolor='gray',elinewidth=0.5) )
df2.set_ylim(100, 240)
df2.set_ylabel(r'$<R_{ee}>$')
df2.set_xlabel(r'$pH$')
df2.legend(['neg, in', 'neg, out', 'pos, in', 'pos, out'])
plt.savefig('fig/ree_bar_neg_pos_in_out_40_rev2.pdf')


plt.figure(2)
df = pd.read_csv("inout_table_rev0.csv")
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
plt.savefig('fig/bar_rg_neg_pos_in_out_40_rev2.pdf')

plt.show()