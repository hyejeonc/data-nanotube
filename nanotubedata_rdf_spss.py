import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pandas as pd

##fixing numbers, opposite charge : neg/pos


strtype = ['m20m20', 'm10m20m10', 'm10m10m10m10'] 
#strtype = ['m30m10', 'm5m30m5','m15m10m15']



pathstring  = []


ph = []
#ree = pd.DataFrame(data = [0,0,0,0,0,0,0], columns = ['Monomer index', 'Prob', 'Err', 'pH', 'Structure', 'Charge ratio', 'R-type'])
rg = [] 
#linecolor = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
#linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']

for i in range(len(strtype)):
    pathstring.append('alsi/polymer/quenchedpoly/{:s}/'.format(str(strtype[i])))

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
                
        dd = pd.DataFrame(d, columns = ['Monomer index', 'Prob', 'Err'])
        dd['pH'] = int(p.parts[-2][2])
        dd['Structure'] = str(p.parts[-4])
        dd['Charge ratio'] = str(p.parts[-5])
        dd['R-type'] = 'Ree'  

        ee = pd.DataFrame(d, columns = ['Monomer index', 'Prob', 'Err'])
        ee['pH'] = int(p.parts[-2][2])
        ee['Structure'] = str(p.parts[-4])
        ee['Charge ratio'] = str(p.parts[-5])
        ee['R-type'] = 'Rg'         
    
    ree = pd.merge(ree, dd, how = 'outer')
     

        
        
  '''      
        plt.figure(1)
        plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2])) 
        plt.title('{:s}'.format(str(strtype[j])) + 'Ree')
        
        plt.figure(2)
        plt.plot(e[:,0], e[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2])) 
        plt.title('{:s}'.format(str(strtype[j])) + 'Rg')

    plt.figure(1)
    plt.ylim(0.000, 1.000)
    plt.ylabel('Prob(Ree)')
    plt.xlabel('Ree [Å]')
    plt.legend()
    
    plt.figure(2)
    plt.ylim(0.000, 1.000)
    plt.ylabel('Prob(Rg)')
    plt.xlabel('Rg [Å]')
    plt.legend()
            
    plt.show()                                                              

'''