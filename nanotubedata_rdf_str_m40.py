import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu

##fixing numbers, opposite charge : neg/pos
iotubeprob = []

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

for p in sorted(Path('alsi/polymer/quenchedpoly/m30m10/zero/').glob('ph*/cylinder_shell.list')):
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
    
    plt.figure(1)    
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]), linestyle = '-')         
plt.legend()
plt.ylim(0.000, 0.150)
#plt.ylabel('[Å]')
plt.title('m30m10 Rg') 

for p in sorted(Path('alsi/polymer/quenchedpoly/m30m10/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    d = mu.getDistribution(p, 'ree pa')    
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    reetemp = d
#    m40nree.append(d)  
#    m40nreelabel.append(labelstring)
    
    plt.figure(2)    
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]), linestyle = '-')         
plt.legend()
plt.ylim(0.000, 0.150)
#plt.ylabel('[Å]')
plt.title('m30m10 Ree') 

#############################################
#############################################

for p in sorted(Path('alsi/polymer/quenchedpoly/m5m30m5/zero/').glob('ph*/cylinder_shell.list')):
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
    
    plt.figure(1)    
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]), linestyle = '-')         
plt.legend()
plt.ylim(0.000, 0.150)
#plt.ylabel('[Å]')
plt.title('m5m30m5 Rg') 

for p in sorted(Path('alsi/polymer/quenchedpoly/m5m30m5/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    d = mu.getDistribution(p, 'ree pa')    
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    reetemp = d
#    m40nree.append(d)  
#    m40nreelabel.append(labelstring)
    
    plt.figure(2)    
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]), linestyle = '-')         
plt.legend()
plt.ylim(0.000, 0.150)
#plt.ylabel('[Å]')
plt.title('m5m30m5 Ree')