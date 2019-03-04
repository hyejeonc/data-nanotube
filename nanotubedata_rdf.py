import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pylab as py

##fixing numbers, opposite charge : neg/pos

strtype = ['m40n', 'm40p', 'm40nretry', 'm40pretry', 'm40ncen', 'm40pcen'] 
chargeratio = ['0', '0', '0', '0', '0', '0']
#strtype = ['m30m10', 'm5m30m5','m15m10m15']

pathstring  = []

ph = []
linecolor = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']

for i in range(len(strtype)):
    pathstring.append('alsi/polymer/quenchedpoly/{:s}'.format(str(chargeratio[i])) + '/{:s}/'.format(str(strtype[i])))

for j in range(len(pathstring)):
    for p in sorted(Path(str(pathstring[j])).glob('zero/ph*/cylinder_shell.list')):
        print(p)  
        d = mu.getDistribution(p, 'ree pa') 
        e = mu.getDistribution(p, 'rg pa') 
        #f = mu.getDistribution(p, 'rg pa')

        labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
        print(p.parts)
        print(p.parts[-2])
        print(p.parts[-2][2])
        ph.append(p.parts[-2][2])
        
        plt.figure(1)
        plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2])) 
        plt.ylim(0.00, 0.5)
        plt.title('{:s}'.format(str(strtype[j])) + ' Ree')
        
        plt.figure(2)
        plt.plot(e[:,0], e[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2])) 
        plt.ylim(0.00, 0.5)       
        plt.title('{:s}'.format(str(strtype[j])) + ' Rg')

    plt.figure(1)
    plt.ylim(0.00, 0.5)
    plt.ylabel('$g(r)$')
    plt.xlabel('$r[Å]$')
    plt.legend()
    py.savefig('{:s}'.format(str(strtype[j])) + '-ree.pdf') 
    
    plt.figure(2)
    plt.ylim(0.00, 0.5)
    plt.ylabel('$g(r)$')
    plt.xlabel('$r$')
    plt.legend()
    py.savefig('{:s}'.format(str(strtype[j])) + '-rg.pdf')              
    
    plt.show()                                                              

