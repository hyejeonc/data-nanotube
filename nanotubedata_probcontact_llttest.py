import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pylab as py

##fixing numbers, opposite charge : neg/pos


strtype = ['m10m10m10', 'm5m20m5' ] 
chargeratio = ['2', '2']

#strtype = ['m40ncen', 'm40pcen'] 
#chargeratio = ['0', '0']
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
        d = mu.monAnalysis(p, 'iotube', 'tt')   #choose itube/otube/iotube 
        e = mu.monAnalysis(p, 'itube', 'tt') 
        f = mu.monAnalysis(p, 'otube', 'tt')

        titlestring = '{:s}'.format(p.parts[-4]) 
        labelstring = 'ph = {:d}'.format(int(p.parts[-2][2]))
        
        print(p.parts)
        print(p.parts[-2])
        print(p.parts[-2][2])
        ph.append(p.parts[-2][2])
        #reetemp = d

        
        plt.figure(1)
        #plt.subplot(311)        
        plt.errorbar(d[:,0], d[:,1], d[:,2], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
        plt.title('{:s}'.format(titlestring)+'\nProbability of inner/outer tube surface')
        plt.ylim(0.00, 1.00)        
        plt.xlim(0, 40)
        
        plt.figure(2)
        #plt.subplot(312)        
        plt.errorbar(e[:,0], e[:,1], e[:,2], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
        plt.title('{:s}'.format(titlestring)+'\nProbability of inner tube surface')
        plt.ylim(0.00, 1.00)
        plt.xlim(0, 40)
        
        
        plt.figure(3)
        #plt.subplot(312)        
        plt.errorbar(f[:,0], f[:,1], f[:,2], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
        plt.title('{:s}'.format(titlestring)+'\nProbability of outer tube surface')
        plt.ylim(0.00, 1.00) 
        plt.xlim(0, 40)
        
    plt.figure(1)
    plt.ylim(0.00, 1.00)
    plt.xlim(0, 40)
    plt.ylabel(r'$Prob(d<7.1\AA)$')
    plt.xlabel(r'$Monomer\ index$')
    plt.legend()
    py.savefig('{:s}'.format(titlestring) + '-prob' + '-io.pdf')        
     
    plt.figure(2)
    plt.ylim(0.00, 1.00)
    plt.xlim(0, 40)
    plt.ylabel(r'$Prob(d<7.1\AA)$')
    plt.xlabel(r'$Monomer\ index$')
    plt.legend()
    py.savefig('{:s}'.format(titlestring) + '-prob' + '-i.pdf')
    
    plt.figure(3)
    plt.ylim(0.00, 1.00)
    plt.xlim(0, 40)
    plt.ylabel(r'$Prob(d<7.1\AA)$')
    plt.xlabel(r'$Monomer\ index$')
    plt.legend()
    py.savefig('{:s}'.format(titlestring) + '-prob' + '-o.pdf')    

    plt.show()

    #    plt.title('{:s}'.format(titlestring)+'\nProbability of inner/outer tube surface')
plt.figure(4) 
#y = [0.25546, 0.26873, 0.27580, 0.25980, 0.25955, 0.25982, 0.27091, 0.26251, 0.26117, 0.25232, 0.24820, 0.25587, 
#         0.26452, 0.26695, 0.25728, 0.24996, 0.24036, 0.25415, 0.26207, 0.26480, 0.25217, 0.25935]
#z = [0.17228, 0.15982, 0.15508, 0.15216, 0.15751, 0.15706, 0.16135, 0.15694, 0.15940, 0.16288, 0.15837, 0.15563, 
#          0.15897, 0.15760, 0.16046, 0.15971, 0.15874, 0.15525, 0.15716, 0.15945, 0.15767, 0.15806]

y = [0.26873, 0.27580, 0.25980, 0.25955, 0.25982, 0.27091, 0.26251, 0.26117, 0.25232, 0.24820, 0.25587, 
         0.26452, 0.26695, 0.25728, 0.24996, 0.24036, 0.25415, 0.26207, 0.26480, 0.25217]
yy = 0.25935 * np.ones(20)
z = [0.15982, 0.15508, 0.15216, 0.15751, 0.15706, 0.16135, 0.15694, 0.15940, 0.16288, 0.15837, 0.15563, 
          0.15897, 0.15760, 0.16046, 0.15971, 0.15874, 0.15525, 0.15716, 0.15945, 0.15767]
zz = 0.15806 * np.ones(20)

plt.plot(np.linspace(1, 20, 20), y, 'b.:', label = 'from outside') 
plt.plot(np.linspace(1, 20, 20), yy , 'b_-', label = 'from outside(final)')
plt.plot(np.linspace(1, 20, 20), z, 'g.:', label = 'from inside(center)')
plt.plot(np.linspace(1, 20, 20), zz, 'g_-', label = 'from inside(final)')
  
plt.ylabel(r'$U_{total}$')
plt.xlabel(r'$Macrostep \ number$')
plt.legend()
py.savefig('m40n-m40ncen-u.pdf')   
plt.show()  
    
    
    

