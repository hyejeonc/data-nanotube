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

strtype = ['m40ncenxyz',  'm40pcenxyz', 'm40nretry', 'm40pretry', 'm40n-notube', 'm40p-notube',\
           'm5m10m5', 'm5m10m5-notube', 'm20m20newroutine','m20m20newroutine-notube', ' m10m20m10', 'm10m20m10-notube', 'm10m10m10m10','m10m10m10m10-notube', \
           'm5m20m5','m5m20m5-notube', 'm10m10m10-npn','m10m10m10-npn-notube', 'm20m10-np', 'm20m10-np-notube', \
           'm15m10m15-npn', 'm15m10m15-npn-notube', 'm5m30m5', 'm5m30m5-notube', 'm30m10','m30m10-np-notube', \
           'm5m20', 'm5m20-notube',\
           'm5m15m5m15-npn', 'm5m15m5m15-npn-notube', 'm5m30-npn-notube' ] # 2.5/17.5 = 5/35 = 1/7 = .142

tube = ['1', '1', '1', '1', '0', '0', \
        '1', '0', '1', '0', '1', '0', '1', '0', \
        '1', '0', '1', '0', '1', '0', \
        '1', '0', '1', '0', '1', '0', \
        '1', '0', \
        '1', '0', '0']
'''
chratio = ['1', '0', '1', '0', \
           '0.5', '0.5', '0.5', '0.5', \
           '0.6667', '0.6667', '0.6667', \
           '0.75', '0.75', '0.75', \
                \
           '0.8571' ]  # 30/35
'''
chnet = ['-40', '40', '-40', '40', '-40', '40', \
         '0', '0', '0', '0', '0', '0', '0', '0', \
         '-10', '-10', '-10', '-10', '-10', '-10', \
         '-20', '-20', '-20', '-20', '-20', '-20', \
         '-15', '-15', \
         '-20', '-20', '-25']

abs_chnet = ['40', '40', '40', '40', '40', '40',\
            '0', '0', '0', '0', '0', '0', '0', '0', \
            '10', '10', '10', '10', '10', '10', \
            '20', '20', '20', '20', '20', '20', \
             '15', '15', \
             '20', '20', '25']

ch_ratio = ['0', '0', '0', '0', '0', '0', \
            '1', '1', '1', '1', '1', '1', '1', '1', \
            '2', '2', '2', '2', '2', '2', \
            '3', '3', '3', '3', '3', '3', \
            '4', '4',\
            '6', '6', '6' ]

block = ['1', '1', '1', '1', '1', '1',\
         '3', '3', '2', '2', '3', '3', '4', '4', \
         '3', '3', '3', '3', '2', '2',\
         '3', '3', '3', '3', '2', '2',\
         '2', '2', \
         '4', '4', '3' ] 

mon = ['40', '40', '40', '40', '40', '40', \
       '20', '20', '40', '40', '40', '40', '40', '40', \
       '30', '30', '30', '30', '30', '30', \
       '40', '40', '40', '40', '40', '40', \
       '25', '25', \
       '40', '40', '35' ]
# 왜 해야하나 이건 . 위에 charge ratio 를 알면!                 
charge = ['1', '2', '1', '2', '1', '2', \
          '0', '0', '0', '0', '0', '0', '0', '0', \
          '1', '1', '1', '1', '1', '1', \
          '1', '1', '1', '1', '1', '1', \
          '1', '1',\
          '1', '1', '1']
'''
edgedist = ['1', '1', '1', '1', \
            '0.5', '0', '0.5', '0.5',\
            '0.6666', '0.3333', '0', \
            '0.25', '0.75', '0', \
            \
            '0.142']  # 2.5/17.5 = 5/35 = 1/7 = .142
'''
# 0인가 1 인가...
sym = ['1', '1', '1', '1', '1', '1', \
       '1', '1', '1', '1', '1', '1', '1', '1', \
       '1', '1', '1', '1', '2', '2', \
       '1', '1', '1', '1', '2', '2', \
       '2', '2',\
       '1', '1', '2']
 
pathstring  = []

ph = []
#ree = pd.DataFrame(data = [0,0,0,0,0,0,0], columns = ['Monomer index', 'Prob', 'Err', 'pH', 'Structure', 'Charge ratio', 'R-type'])
rg = [] 
#linecolor = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
#linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']

for i in range(len(strtype)):
    pathstring.append('../alsi/polymer/quenchedpoly/{:s}'.format(str(ch_ratio[i])) + '/{:s}/'.format(str(strtype[i])))

reesum = pd.DataFrame
startcount = 1

r = pd.DataFrame
allmatrix = []
      
for j in range(len(pathstring)):
    for p in sorted(Path(str(pathstring[j])).glob('zero/ph*/cylinder_shell.out')):
        
        print(p) 
        try : 
            r_single = mu.getAvgR(str(p))#, 'zero', 'cylinder_shell.out', p.parts[-2][2])
            inseg = mu.gettubeILTT(p, 'adsorbed')  # choose itube/otube/iotube 
            outseg = mu.gettubeOLTT(p, 'adsorbed') # [[# adsorbed chain, fluc], [# adsorbed seg, fluc]]
        except ValueError: 
            continue

        print(inseg)
        print('#adsorbed chain', inseg[0][0])
        print('#adsorbed chain fluc', inseg[0][1])
        print('#adsorbed seg', inseg[1][0])
        print('#adsorbed seg fluc', inseg[1][1])      
        print(outseg)

        labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
        print(p.parts)
        print(p.parts[-2])
        print(p.parts[-2][2])
        ph.append(p.parts[-2][2])

        d = {'reerms' : [r_single[0][4][1]], 'reeavg' : [r_single[0][4][0]]} 
        ree = pd.DataFrame(data = d)
        local = str(p.parts[-4])
        
        if inseg[1][0] < 1e-320:
            ree['inout'] = 2 # outside
        elif inseg[1][0] > 0:  
            ree['inout'] = 1 # inside
                    
        if local.find('cen') != -1:  
            ree['loc'] = 1 #'Inside'
        elif local.find('notube') != -1:  
            ree['loc'] = 0 #notube
        else:
            ree['loc'] = 2 #outside
        
      
        ree['rgrms'] = r_single[0][5][1]
        ree['rgavg'] = r_single[0][5][0]
        
        ree['inadschain'] = inseg[0][0]
        ree['inadsseg'] = inseg[1][0]
        ree['outadschain'] = outseg[0][0]
        ree['outadsseg'] = outseg[1][0]


        ree['structure'] = str(p.parts[-4]) #not use
        
        ree['chratio'] = chratio[j]
        ree['chtype'] = charge[j]
        ree['chnet'] = chnet[j]
        
        ree['ph'] = int(p.parts[-2][2])
        ree['block'] = block[j]
        ree['mon'] = mon[j]
        ree['edgedist'] = edgedist[j]
        ree['sym'] = sym[j]

        print(ree)
        '''   
        if startcount == 1:
            #reesum = ree
            ree.to_csv("spssdata/inout_spss_rev1.csv", mode="w")
            #rg.to_csv("spssdata/inout_spss_rev0_sym.csv", mode="a")
        else:    
            ree.to_csv("spssdata/inout_spss_rev1.csv", mode="a", header=False)
            #rg.to_csv("spssdata/rg_spss_rev3_sym.csv", mode="a", header=False)

            #pd.merge(reesum, ree, on = 'Monomer index')
        '''
        startcount += 1
