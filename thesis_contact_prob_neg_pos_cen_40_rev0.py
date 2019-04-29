import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pylab as py
import numpy as np

##fixing numbers, opposite charge : neg/pos

strtype = ['m40ncenxyz', 'm40pcenxyz'] 
chargeratio = ['0', '0','0', '0' ]

pathstring  = []
ph = []

linecolor = [['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown'],
              ['lightsteelblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']]
linecolor1 = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']

fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0)

for i in range(len(strtype)):
    pathstring.append('../alsi/polymer/quenchedpoly/{:s}'.format(str(chargeratio[i])) + '/{:s}/'.format(str(strtype[i])))
plotlines=[]
for j in range(len(pathstring)):
    ph = []
    for p in sorted(Path(str(pathstring[j])).glob('zero/ph*/cylinder_shell.list')):
        print(p)  
        d = mu.monAnalysis(p, 'iotube', 'tt')  
        
        e = mu.monAnalysis(p, 'itube', 'tt') 
        f = mu.monAnalysis(p, 'otube', 'tt')
        
        labelstring = 'pH = {:d}'.format(int(p.parts[-2][2]))
        
        print(p.parts)
        print(p.parts[-2])
        print(p.parts[-2][2])
        ph.append(p.parts[-2][2])
        
        d[:,1] = e[:,1] + f[:,1]
        for k in range(len(d)):
            d[k][2] = max(e[k][2], f[k][2])
         
        d_errdown = d[:,1] - 0.5*d[:,2]
        d_errup = d[:,1] + 0.5*d[:,2]       
        
        e_errdown = e[:,1] - 0.5*e[:,2]
        e_errup = e[:,1] + 0.5*e[:,2]       
        f_errdown = f[:,1] - 0.5*f[:,2]
        f_errup = f[:,1] + 0.5*f[:,2]            
        
        plt.figure(1)  # in out 
        if j == 0 :
            labelstring = 'neg, pH = {:d}'.format(int(p.parts[-2][2]))
            axs[0].plot(d[:,0], d[:,1], label=labelstring, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle='-')      
            #axs[0].legend(fontsize=8) 
        if j == 1 :
            labelstring = 'pos, pH = {:d}'.format(int(p.parts[-2][2]))
            axs[0].plot(d[:,0], d[:,1], label=labelstring, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle='-')      
            #axs[2].legend(fontsize=8) 
        if j == 2 :
            labelstring = 'neg, inner, pH = {:d}'.format(int(p.parts[-2][2]))
            axs[0].plot(d[:,0], d[:,1], label=labelstring, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle='-')      
            #axs[2].legend(fontsize=8)
        if j == 1 :
            labelstring = 'pos, outer, pH = {:d}'.format(int(p.parts[-2][2]))
            axs[0].plot(d[:,0], d[:,1], label=labelstring, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle='-')      
            #axs[2].legend(fontsize=8)    
            
        axs[0].fill_between(d[:,0], d_errdown, d_errup, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , alpha=0.2)
        axs[0].set_ylim(0.00, 0.5)  
        axs[0].set_ylabel(r'$P(d<7.1\AA)$', size=8)
        axs[0].set_xlim(0, 40.5)
       # 
        #axs[0].grid(True)
        
        #if j == 0:
        #    axs[0].legend(fontsize=8)

        axs[1].plot(e[:,0], e[:,1],  color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle=':'  )      
        axs[1].fill_between(e[:,0], e_errdown, e_errup, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , alpha=0.2)
        axs[1].set_ylim(0.00, 0.5)    
        axs[1].set_ylabel(r'$P(d<7.1\AA)$', size=8)
        axs[1].set_xlim(0, 40.5)
        
        if j == 0 and int(p.parts[-2][2]) == 2:
            axs[1].plot(d[:,0], np.zeros(len(d)), label = 'in+out', color = 'black', linestyle = '-')
            axs[1].plot(d[:,0], np.zeros(len(d)), label = 'in', color = 'black', linestyle = ':')    
            axs[1].plot(d[:,0], np.zeros(len(d)), label = 'out', color = 'black', linestyle = '--')
        else: 
            axs[1].plot(d[:,0], np.zeros(len(d)), color = 'black', linestyle = '-')
            axs[1].plot(d[:,0], np.zeros(len(d)), color = 'black', linestyle = ':')    
            axs[1].plot(d[:,0], np.zeros(len(d)), color = 'black', linestyle = '--')

        axs[1].legend(fontsize = 8)
        #axs[1].grid(True)
        
        axs[2].plot(f[:,0], f[:,1], label=labelstring, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , linestyle='--')      
        
        axs[2].fill_between(f[:,0], f_errdown, f_errup, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , alpha=0.2)
        axs[2].set_ylim(0.0, 0.5)        
        axs[2].set_ylabel(r'$P(d<7.1\AA)$', size=8)
        axs[2].set_xlim(0, 40.5)
        axs[2].set_xlabel(r'$Monomer\ index$')
        #axs[2].grid(True)
        #if j == 1:   
            #axs[2].legend(fontsize=8)


#plt.hold(True)
plotlines.append([axs[0], axs[1], axs[2]])
#legend1 = plt.legend(plotlines[0], ['in+out', 'in', 'out'], loc = 'center left')
#plt.legend([axs[0]])
#plt.plot(f[:,0], d[:,0], e[:,0], f[:,0], label=['in+out', 'in', 'out'])

fig.savefig("fig/contactprob_neg_pos_cen_40_r2_without_legend.pdf")    


