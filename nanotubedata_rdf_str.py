import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu

##fixing numbers, opposite charge : neg/pos
m40nree = [] # [[bin,value,stdev], [bin,value,stdev], [bin,value,stdev]]
m40nreelabel = []


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

ph = []
linecolor = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']


for p in sorted(Path('alsi/polymer/quenchedpoly/m20m10/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    d = mu.getDistribution(p, 'ree pa')    
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    reetemp = d
    m40nree.append(d)  
    m40nreelabel.append(labelstring)
    
    plt.figure(1)
#    plt.subplot(211)
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
plt.legend()
plt.ylim(0.000, 0.250)
#plt.ylabel('[Å]')
plt.title('m20m10 Ree')
plt.show()

for p in sorted(Path('alsi/polymer/quenchedpoly/m20m10/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    d = mu.getDistribution(p, 'rg pa')    
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    reetemp = d
    m40nree.append(d)  
    m40nreelabel.append(labelstring)
    
    plt.figure(1)
#    plt.subplot(211)
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
plt.legend()
plt.ylim(0.000, 0.250)
#plt.ylabel('[Å]')
plt.title('m20m10 Rg')
plt.show()
    
for p in sorted(Path('alsi/polymer/quenchedpoly/m10m10m10m10/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    d = mu.getDistribution(p, 'ree pa')    
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    reetemp = d
    m40nree.append(d)  
    m40nreelabel.append(labelstring)
    
    plt.figure(2)    
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]), linestyle = '-')         
plt.legend()
plt.ylim(0.000, 0.250)
#plt.ylabel('[Å]')
plt.title('m10m10m10m10 Ree') 


for p in sorted(Path('alsi/polymer/quenchedpoly/m10m10m10m10/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    d = mu.getDistribution(p, 'rg pa')    
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    reetemp = d
#    m40nrg.append(d)  
#    m40nrglabel.append(labelstring)
    
    plt.figure(3)
#    plt.subplot(211)
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
plt.legend()
plt.ylim(0.000, 0.250)
#plt.ylabel('[Å]')
plt.title('m10m10m10m10 Rg')
plt.show()

for p in sorted(Path('alsi/polymer/quenchedpoly/m10m20m10/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    d = mu.getDistribution(p, 'ree pa')    
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    reetemp = d
    m40nree.append(d)  
    m40nreelabel.append(labelstring)
    
    plt.figure(2)    
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]), linestyle = '-')         
plt.legend()
plt.ylim(0.000, 0.250)
#plt.ylabel('[Å]')
plt.title('m10m20m10 Ree')
    
for p in sorted(Path('alsi/polymer/quenchedpoly/m10m20m10/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    d = mu.getDistribution(p, 'rg pa')    
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    reetemp = d
#    m40nree.append(d)  
#    m40nreelabel.append(labelstring)
    
    plt.figure(4)    
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]), linestyle = '-')         
plt.legend()
plt.ylim(0.000, 0.250)
#plt.ylabel('[Å]')
plt.title('m10m20m10 Rg') 
'''
# Extracting charge data from .out files
alpha_1 = []
alpha_2 = []
alpha_error_1 = []
alpha_error_2 = []
ph = []
for p in sorted(Path('alsi/polymer/quenchedpoly/m40n/zero/').glob('ph*/cylinder_shell.out')):
    print(p)  
    # mu.getAvgPartCharge() returns three values: average charge fraction, precision and fluctuation
    # Input arguments are: mu.getAvgPartCharge( [path to file in], [particle type] )
    # Note that the particle type must be given as a string
    charge_1 = mu.getAvgPartCharge(p, 'alumina')
    charge_2 = mu.getAvgPartCharge(p, 'silica')

    alpha_1.append( charge_1[0] )
    alpha_2.append( charge_2[0] )

    alpha_error_1.append( charge_1[2] )
    alpha_error_2.append( charge_2[2] )
    ph.append( int(p.parts[-2][2]) )
        
    plt.figure(5)    
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]), linestyle = '-')         
plt.legend()
plt.ylim(0.000, 0.020)
plt.title('m40p rg') 
    

print('\n pH: ', ph, '\n alpha_1: ', alpha_1, '\n alpha_error: ', alpha_error_1)
print('\n pH: ', ph, '\n alpha_2: ', alpha_2, '\n alpha_error: ', alpha_error_2)
'''