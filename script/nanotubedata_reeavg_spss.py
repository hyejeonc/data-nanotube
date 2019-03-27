import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pandas as pd

##fixing numbers, opposite charge : neg/pos

#strtype = ['m20m20newroutine']
#chargeratio = ['1']
#monomernumber = ['40']
#polymer = ['2']
strtype = ['m20m20newroutine', 'm40ncen', 'm20m20', 'm10m20m10', 'm10m10m10m10', 'm5m10m5', 'm5m20m5', 'm10m10m10', 'm20m10', 'm5m30m5', 'm15m10m15', 'm30m10', 'm10m5m10', 'm15m5m15' ] 
chargeratio = ['1', '0', '1', '1', '1', '1', '2', '2', '2', '3', '3', '3' , '4', '6' ]
monomernumber = ['40', '40', '40', '40', '40', '20', '30', '30', '30', '40', '40', '40', '25', '35' ]
polymer = ['1', '2', '3', '4', '3', '3', '3', '3', '2', '3', '3', '2', '3', '3' ] 
#strtype = ['m30m10', 'm5m30m5','m15m10m15']

pathstring  = []


ph = []
#ree = pd.DataFrame(data = [0,0,0,0,0,0,0], columns = ['Monomer index', 'Prob', 'Err', 'pH', 'Structure', 'Charge ratio', 'R-type'])
rg = [] 
#linecolor = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
#linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']

for i in range(len(strtype)):
    pathstring.append('alsi/polymer/quenchedpoly/{:s}'.format(str(chargeratio[i])) + '/{:s}/'.format(str(strtype[i])))

reesum = pd.DataFrame
startcount = 1

r = pd.DataFrame
      
for j in range(len(pathstring)):
    for p in sorted(Path(str(pathstring[j])).glob('zero/ph*/cylinder_shell.out')):
        
       # print(p) 
        r_single = mu.getAvgR(str(p))#, 'zero', 'cylinder_shell.out', p.parts[-2][2])
        #ree_avg = mu.getAvgR(p, 'ree pa', 2, 'chain type distribution functions', [2:3] )
       # print(r_single)

        #r_avg.append(r_avg)
        #f = mu.getDistribution(p, 'rg pa')

        labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
       # print(p.parts)
        #print(p.parts[-2])
        #print(p.parts[-2][2])
        ph.append(p.parts[-2][2])

        
       # a = [r_single[0][4][1], r_single[0][4][0]]
       # b = ['Rms', 'Avg']
        d = {'Rms' : [r_single[0][4][1]], 'Avg' : [r_single[0][4][0]]} 
        ree = pd.DataFrame(data = d)
       # print(ree)

        ree['pH'] = int(p.parts[-2][2])
        ree['Structure'] = str(p.parts[-4])
        ree['Polymer_type'] = polymer[j]
        ree['Charge_ratio'] = str(p.parts[-5])
        ree['Monomer_number'] = monomernumber[j]
        ree['R_type'] = 'Ree'  
        
        #print(ree)
           
        e = {'Rms' : [r_single[0][5][1]], 'Avg' : [r_single[0][5][0]]} 
        rg = pd.DataFrame(data = e)
        #print(rg)
 
        rg['pH'] = int(p.parts[-2][2])
        rg['Structure'] = str(p.parts[-4])
        rg['Polymer_type'] = polymer[j]
        rg['Charge_ratio'] = str(p.parts[-5])
        rg['Monomer_number'] = monomernumber[j]
        rg['R_type'] = 'Rg' 
        
        local = str(p.parts[-4])
        if local.find('cen') == -1: ##이 부분이 안됨!!!!! 
            ree['Location'] = 'Inside'
            rg['Location'] = 'Inside'
        else:
            ree['Location'] = 'Outside'
            rg['Location'] = 'Outside'
    
        if startcount == 1:
            #reesum = ree
            ree.to_csv("ree_spss_avg.csv", mode="w")
            rg.to_csv("rg_spss_avg.csv", mode="a", header=False)
        else:    
            ree.to_csv("ree_spss_avg.csv", mode="a", header=False)
            rg.to_csv("rg_spss_avg.csv", mode="a", header=False)

            #pd.merge(reesum, ree, on = 'Monomer index')

        startcount += 1

            
 
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