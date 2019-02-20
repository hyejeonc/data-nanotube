import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu

##fixing numbers, opposite charge : neg/pos
m40nree = [] # [[bin],[value],[stdev]]
m40pree = []
m40nrg = [] # [[bin],[value],[stdev]]
m40prg = []
m40nrdf = [] # [[bin],[value],[stdev]]
m40prdf = []

ph = []
bin = []
ree = []
reeerr = []
rg = []
rgerr = []
rdf = []
rdferr = []




for p in sorted(Path('alsi/polymer/quenchedpoly/m40n/zero/').glob('ph*/cylinder_shell.out')):
    print(p)  
    # mu.getAvgPartCharge() returns three values: average charge fraction, precision and fluctuation
    # Input arguments are: mu.getAvgPartCharge( [path to file in], [particle type] )
    # Note that the particle type must be given as a string
    reetemp = mu.distAnalysis(p, 'ree')
    rgtemp = mu.distAnalysis(p, 'rg')
    rdftemp = mu.distAnalysis(p, 'rdf')    

    bin.append( reetemp[0] )
    ree.append( reetemp[1] )
    reeerr.append( reetemp[2])
    
    rg.append( rgtemp[1] )
    rgerr.append( rgtemp[2])
    
    rdf.append( rdftemp[1] )
    rdferr.append( rdftemp[2])

    ph.append( int(p.parts[-2][2]) )
    m40nree.append()
    m40nrg.append()
    m40nrdf.append()


print('\n pH: ', ph, '\n alpha_1: ', alpha_1, '\n alpha_error: ', alpha_error_1)
print('\n pH: ', ph, '\n alpha_2: ', alpha_2, '\n alpha_error: ', alpha_error_2)
'''
m5m30m5_al = alpha_1[0:7] 
m5m30m5_si = alpha_2[0:7]
m5m30m5_al_err = alpha_error_1[0:7]
m5m30m5_si_err = alpha_error_1[0:7]


###############################################################
#plot data with different polymers
plt.plot(ph, m10m20m10_al, label='m10m20m10, Al', color='lightskyblue', linestyle='--')
plt.plot(ph, m10m10m10m10_al, label='m10m10m10m10, Al', color='royalblue', linestyle='-')
plt.plot(ph, m20m20_al, label='m20m20, Al', color='blue', linestyle='-')
plt.plot(ph, m5m30m5_al, label='m5m30m5, Al', color='darkblue', linestyle='-')
plt.xlabel('pH')
plt.ylabel('fractional charge')
plt.legend(loc="left")
plt.ylim(-0.1, 1.1)
plt.show()

plt.plot(ph, m10m20m10_si, label='m10m20m10, Si', color='orange', linestyle='--')
plt.plot(ph, m10m10m10m10_si, label='m10m10m10m10, Si', color='darkorange', linestyle='-')
plt.plot(ph, m20m20_si, label='m20m20, Si', color='chocolate', linestyle='-')
plt.plot(ph, m5m30m5_si, label='m5m30m5, Si', color='saddlebrown', linestyle='-')
plt.xlabel('pH')
plt.ylabel('fractional charge')
plt.legend(loc="left")
plt.ylim(-0.1, 1.1)
plt.show()
'''




'''
print()
print('Using Path.glob to search for *.list files in test/:')
for p in sorted(Path('test/').glob('*.list')):
    print('  p:\t ', p)
    print('  p.parts: ', p.parts)
    print('  p.parts[0]: ', p.parts[0])
    print('  p.parts[1]: ', p.parts[1])
    print('  p.parts[1][2:5]: ', p.parts[1][2:5])
    print('  p.parts[1][:-5]: ', p.parts[1][:-5])
    print('  p.parts[1][-4:]: ', p.parts[1][-4:])

    
# Path.rglob recursively searches for files (i.e. it includes all sub-folders)
print()
print('Using Path.glob to _recursively_ search for *.list files in test/:')
for p in sorted(Path('test/').rglob('*.list')):
    print('  p:\t ', p, '    p.parts: ', p.parts)
    #print('  p.parts: ', p.parts)

print()

# only search for .list files in foldes which start with ph
print('Using Path.glob to _recursively_ search for *.list files in test/ph*:')
for p in sorted(Path('test/').glob('ph*/*.list')):
    print('  p:\t ', p, '    p.parts: ', p.parts, )#'  pH: ', int(p.parts[1][2]))

print()
'''











'''
 #Plot charge data


fig1, ax1 = plt.subplots(1,1)

ax1.set_xlabel('pH')
ax1.set_ylabel('Fractional charge')

ax1.plot(ph, alpha_1, marker='o', markersize=10, label='alumina (Al100)')#linestyle='None')
ax1.plot(ph, alpha_2, marker='v', markersize=10, label='silica (Si100)')
ax1.plot(ph, alpha_al, color='tab:orange', marker='o', markersize=10, label='alumina (Al240)')#linestyle='None')
ax1.plot(ph, alpha_si, color='tab:orange', marker='v', markersize=10, label='silica (Si240)')
ax1.plot(ph, alpha_al500, linestyle='--', marker='o', markersize=10, label='alumina (Al500)')#linestyle='None')
ax1.plot(ph, alpha_si500, linestyle='--', marker='v', markersize=10, label='silica (Si500)')

ax1.legend()


#fig1.savefig('alumina_silicatitration.pdf')


#Extract distributions from .list files and plot them

fig2, ax2 = plt.subplots(1,1)

for p in sorted(Path('test/').glob('pH*/*.list')):
    d = mu.getDistribution(p, 'rdf ion-counterion')    
    labelstring = 'pH = {:d}'.format( int(p.parts[1][2]) )
    ax2.plot( d[:,0], d[:,1], label=labelstring )  # d[:,0] extracts the first column from d, d[:,1] the second

ax2.legend()   # Show legend/labels in ax2


plt.show()
'''