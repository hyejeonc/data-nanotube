import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pylab as py
import numpy as np
import matplotlib
##fixing numbers, opposite charge : neg/pos
#matplotlib.rcParams['figure.figsize'] = (9,6)

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
            #axs[0].legend(fontsize=8) 
        if j == 1 :
            labelstring = 'pos, pH = {:d}'.format(int(p.parts[-2][2]))
        '''
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
        '''
        
        if int(p.parts[-2][2]) in [2, 3] :
            axs[0].plot(d[:,0], d[:,1], label=labelstring, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle='--')            
            axs[1].plot(e[:,0], e[:,1],  color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle='--'  )
            axs[2].plot(f[:,0], f[:,1], color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , linestyle='--')   

        elif int(p.parts[-2][2]) in [4] :
            axs[0].plot(d[:,0], d[:,1], label=labelstring, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle=':')            
            axs[1].plot(e[:,0], e[:,1],  color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle=':'  )
            axs[2].plot(f[:,0], f[:,1], color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , linestyle=':')   

        else :
            axs[0].plot(d[:,0], d[:,1], label=labelstring, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle='-')            
            axs[1].plot(e[:,0], e[:,1],  color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle='-'  )
            axs[2].plot(f[:,0], f[:,1],  color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , linestyle='-')   

        
        axs[0].fill_between(d[:,0], d_errdown, d_errup, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , alpha=0.2)
        axs[0].set_ylim(0.00, 0.5)  
        axs[0].set_ylabel(r'$P_{in+out}(d<7.1\AA)$', size=8)
        axs[0].set_xlim(0, 40.5)

              
        axs[1].fill_between(e[:,0], e_errdown, e_errup, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , alpha=0.2)
        axs[1].set_ylim(0.00, 0.5)    
        axs[1].set_ylabel(r'$P_{in}(d<7.1\AA)$', size=8)
        axs[1].set_xlim(0, 40.5)
        

            
        axs[2].fill_between(f[:,0], f_errdown, f_errup, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , alpha=0.2)
        axs[2].set_ylim(0.0, 0.5)        
        axs[2].set_ylabel(r'$P_{out}(d<7.1\AA)$', size=8)
        axs[2].set_xlim(0, 40.5)
        axs[2].set_xlabel(r'$Monomer\ index$')
        #axs[2].grid(True)
        #if j == 1:   
            #axs[2].legend(fontsize=8)
box = axs[0].get_position()
axs[0].set_position([box.x0, box.y0, box.width * 0.9, box.height])
box = axs[1].get_position()
axs[1].set_position([box.x0, box.y0, box.width * 0.9, box.height])
box = axs[2].get_position()
axs[2].set_position([box.x0, box.y0, box.width * 0.9, box.height])
#axs[1].set_position([box.x0, box.y0, box.width * 0.8, box.height])
#axs[2].set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
fig.legend(loc='center right', bbox_to_anchor=(1.005, 0.5), fontsize=8)


#fig.legend(fontsize = 8, loc='upper right', bbox_to_anchor=(0.5, -0.05))#, bbox_to_anchor=(1, 0))

#fig.legend(fontsize=8)
#plt.hold(True)
plotlines.append([axs[0], axs[1], axs[2]])
#legend1 = plt.legend(plotlines[0], ['in+out', 'in', 'out'], loc = 'center left')
#plt.legend([axs[0]])
#plt.plot(f[:,0], d[:,0], e[:,0], f[:,0], label=['in+out', 'in', 'out'])

fig.savefig("fig/contactprob_neg_pos_cen_40_r2_with_legend.pdf")    


