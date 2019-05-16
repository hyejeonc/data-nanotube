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
linecolor = ['royalblue', 'orange', 'green', 'red', 'gray', 'black', 'cyan', 'navy', 'wine']
linecolor1 = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']

strtype = ['m40ncenxyz',  'm40pcenxyz', 'm40n-notube', 'm40p-notube', 'm40n', 'm40p',\
           'm5m10m5', 'm20m20newroutine', 'm10m20m10', 'm10m10m10m10', \
           'm5m20m5', 'm10m10m10', 'm20m10', \
           'm15m10m15', 'm5m30m5', 'm30m10', \
            \
           'm15m5m15' ] # 2.5/17.5 = 5/35 = 1/7 = .142

chratio = ['0', '0', '0', '0', '0', '0', \
               '1', '1', '1', '1', \
               '2', '2', '2', \
               '3', '3', '3', \
                \
               '6' ]

block = ['1', '1', '1', '1', '1', '1', \
           '3', '2', '3', '4', \
           '3', '3', '2', \
           '3', '3', '3', \
            \
           '3' ] 

symmetry = ['0', '0', '0', '0', '0', '0', \
            '1', '1', '1', '1', \
            '1', '1', '2', \
            '1', '1', '2', \
            \
            '1' ]

mon = [ '40', '40', '40', '40', '40', '40',\
                 '20', '40', '40', '40', \
                 '30', '30', '30', \
                 '40', '40', '30', \
                  \
                 '35' ]
                 
charge = ['1', '2', '1', '2', '1', '2',\
          '0', '0', '0', '0', \
          '1', '1', '1', \
          '1', '1', '1', \
          \
          '1']

edgedist = ['1', '1', '1', '1', '1', '1',\
        '0.5', '0', '0.5', '0.5',\
        '0.6666', '0.3333', '0', \
        '0.25', '0.75', '0', \
        \
        '0.142']  # 2.5/17.5 = 5/35 = 1/7 = .142

# 0인가 1 인가...
sym = ['1', '1', '1', '1', '1', '1', \
            '1', '2', '1', '1', \
            '1', '1', '2', \
            '1', '1', '2', \
            \
            '1']
 
pathstring  = []

ph = []
#ree = pd.DataFrame(data = [0,0,0,0,0,0,0], columns = ['Monomer index', 'Prob', 'Err', 'pH', 'Structure', 'Charge ratio', 'R-type'])
rg = [] 
#linecolor = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
#linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']

for i in range(len(strtype)):
    pathstring.append('../alsi/polymer/quenchedpoly/{:s}'.format(str(chratio[i])) + '/{:s}/'.format(str(strtype[i])))

reesum = pd.DataFrame
startcount = 1

r = pd.DataFrame
      
for j in range(len(pathstring)):
    for p in sorted(Path(str(pathstring[j])).glob('zero/ph*/cylinder_shell.out')):
        
        print(p) 
        try : r_single = mu.getAvgR(str(p))#, 'zero', 'cylinder_shell.out', p.parts[-2][2])
        except ValueError: 
            continue
        #ree_avg = mu.getAvgR(p, 'ree pa', 2, 'chain type distribution functions', [2:3] )
       # print(r_single)

        #r_avg.append(r_avg)
        #f = mu.getDistribution(p, 'rg pa')

        labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
        print(p.parts)
        print(p.parts[-2])
        print(p.parts[-2][2])
        ph.append(p.parts[-2][2])

        
       # a = [r_single[0][4][1], r_single[0][4][0]]
       # b = ['Rms', 'Avg']
        d = {'rms' : [r_single[0][4][1]], 'avg' : [r_single[0][4][0]]} 
        ree = pd.DataFrame(data = d)
       # print(ree)



        ree['structure'] = str(p.parts[-4]) #not use
        
        ree['chratio'] = str(p.parts[-5])
        ree['chtype'] = charge[j]
        
        ree['ph'] = int(p.parts[-2][2])
        ree['block'] = block[j]
        ree['mon'] = mon[j]
        ree['edgedist'] = edgedist[j]
        ree['sym'] = symmetry[j]
        ree['r'] = 'ree'  
        
        #print(ree)
           
        e = {'rms' : [r_single[0][5][1]], 'avg' : [r_single[0][5][0]]} 
        rg = pd.DataFrame(data = e)
        #print(rg)
 
        rg['structure'] = str(p.parts[-4]) #not use
        
        rg['chratio'] = str(p.parts[-5])
        rg['chtype'] = charge[j]
        
        rg['ph'] = int(p.parts[-2][2])
        rg['block'] = block[j]
        rg['mon'] = mon[j]
        rg['edgedist'] = edgedist[j]
        rg['sym'] = symmetry[j]
        rg['r'] = 'rg'
        
        local = str(p.parts[-4])
        if local.find('cen') != -1:  
            ree['loc'] = 2 #'Inside'
            rg['loc'] = 2
        elif local.find('notube') != -1:  
            ree['loc'] = 0 #notube
            rg['loc'] = 0
        else:
            ree['loc'] = 1 #outside
            rg['loc'] = 1
    
        if startcount == 1:
            #reesum = ree
            ree.to_csv("spssdata/ree_spss_rev3_sym.csv", mode="w")
            rg.to_csv("spssdata/rg_spss_rev3_sym.csv", mode="w")
        else:    
            ree.to_csv("spssdata/ree_spss_rev3_sym.csv", mode="a", header=False)
            rg.to_csv("spssdata/rg_spss_rev3_sym.csv", mode="a", header=False)

            #pd.merge(reesum, ree, on = 'Monomer index')

        startcount += 1
