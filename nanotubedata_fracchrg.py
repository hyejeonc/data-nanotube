import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu



# Extracting charge data from .out files
aln = []
sin = []
alnstdev = []
sinstdev = []
ph = []

linecolor = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']

for p in sorted(Path('alsi/polymer/quenchedpoly/m40n/zero/').glob('ph*/cylinder_shell.out')):
    print(p)  
    # mu.getAvgPartCharge() returns three values: average charge fraction, precision and fluctuation
    # Input arguments are: mu.getAvgPartCharge( [path to file in], [particle type] )
    # Note that the particle type must be given as a string
    charge_1 = mu.getAvgPartCharge(p, 'alumina')
    charge_2 = mu.getAvgPartCharge(p, 'silica')

    aln.append( charge_1[0] )
    sin.append( charge_2[0] )

    alnstdev.append( charge_1[2] )
    sinstdev.append( charge_2[2] )
    ph.append( int(p.parts[-2][2]) )
    
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2]))   

alp = []
sip = []
alpstdev = []
sipstdev = []
ph = []


for p in sorted(Path('alsi/polymer/quenchedpoly/m40p/zero/').glob('ph*/cylinder_shell.out')):
    print(p)  
    # mu.getAvgPartCharge() returns three values: average charge fraction, precision and fluctuation
    # Input arguments are: mu.getAvgPartCharge( [path to file in], [particle type] )
    # Note that the particle type must be given as a string
    charge_1 = mu.getAvgPartCharge(p, 'alumina')
    charge_2 = mu.getAvgPartCharge(p, 'silica')

    alp.append( charge_1[0] )
    sip.append( charge_2[0] )

    alpstdev.append( charge_1[2] )
    sipstdev.append( charge_2[2] )
    ph.append( int(p.parts[-2][2]) )
    
 
plt.figure(2)    
plt.errorbar(ph, aln, alnstdev, label = 'Alumina, m40n', color = 'royalblue', marker ='o', linestyle = ':', ) 
plt.errorbar(ph, sin, sinstdev, label = 'Silica, m40n', color = 'darkorange', marker ='o', linestyle = ':')  
plt.errorbar(ph, alp, alpstdev, label = 'Alumina, m40p', color = 'royalblue', marker ='*', linestyle = '--') 
plt.errorbar(ph, sip, sipstdev, label = 'Silica, m40p', color = 'darkorange', marker ='*', linestyle = '--')

'''
plt.fill_between(ph, aln - alnstdev, aln + alnstdev)     
plt.fill_between(ph, sin - sinstdev, sin + alnstdev)     
plt.fill_between(ph, alp - alpstdev, alp + alpstdev)     
plt.fill_between(ph, sip - sinstdev, sip + alnstdev)        
'''
plt.legend()
plt.ylim(-0.1000, 1.100)
plt.title('fractional charge') 
plt.show()


    
  