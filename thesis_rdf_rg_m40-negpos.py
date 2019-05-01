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
linecolor1 = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
linecolor2 = ['lightsteelblue', 'lightskyblue', 'dodgerblue', 'royalblue', 'blue', 'darkblue', 'black']
plot_lines = []
legend1 = []
legend2 = []

fig, axs = plt.subplots(2, 1, sharex=True)
# Remove horizontal space between axes
fig.subplots_adjust(hspace=0)

# Plot each graph, and manually set the y tick values
errdown = []
errup = []
for p in sorted(Path('../alsi/polymer/quenchedpoly/0/m40nretry/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    d = mu.getDistribution(p, 'rg pa') 
    #e = mu.getDistribution(p, 'ree pa') 
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'neg, pH = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    
    errdown = np.zeros(len(d))
    errup = np.zeros(len(d))
    errdown[:] = d[:,1] - 0.5*d[:,2]
    errup[:] = d[:,1] + 0.5*d[:,2]
#    m40nree.append(d)  
#    m40nreelabel.append(labelstring)
    
    plt.figure(1)
    if int(p.parts[-2][2]) in [2, 3] :
        axs[0].plot(d[:,0], d[:,1], label = labelstring,\
                    color = '{:s}'.format(linecolor1[int(p.parts[-2][2])-2]), linestyle = '--')         
    
    elif int(p.parts[-2][2]) in [4] :
        axs[0].plot(d[:,0], d[:,1], label = labelstring,\
                    color = '{:s}'.format(linecolor1[int(p.parts[-2][2])-2]), linestyle = ':')         
 
    else:
        axs[0].plot(d[:,0], d[:,1], label = labelstring,\
                    color = '{:s}'.format(linecolor1[int(p.parts[-2][2])-2]), linestyle = '-')   
    axs[0].fill_between(d[:,0], errdown, errup, alpha=0.4, color = '{:s}'.format(linecolor1[int(p.parts[-2][2])-2]))
    axs[0].legend(fontsize = 8)



ph=[]
for p in sorted(Path('../alsi/polymer/quenchedpoly/0/m40pretry/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    e = mu.getDistribution(p, 'rg pa')    
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'pos, pH = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    reetemp = e
#    m40nree.append(d)  
#    m40nreelabel.append(labelstring)
    errdown = np.zeros(len(e))
    errup = np.zeros(len(e))
    errdown[:] = e[:,1] - 0.5*e[:,2]
    errup[:] = e[:,1] + 0.5*e[:,2]
    #fig1 = plt.plot()
    if int(p.parts[-2][2]) in [2, 3] :
        axs[1].plot(e[:,0], e[:,1], label = labelstring, \
                    color = '{:s}'.format(linecolor2[int(p.parts[-2][2])-2]), linestyle = '--')
    elif int(p.parts[-2][2]) in [4] :
        axs[1].plot(e[:,0], e[:,1], label = labelstring, \
                    color = '{:s}'.format(linecolor2[int(p.parts[-2][2])-2]), linestyle = ':')
    
    else: 
        axs[1].plot(e[:,0], e[:,1], label = labelstring, \
                    color = '{:s}'.format(linecolor2[int(p.parts[-2][2])-2]), linestyle = '-')      
    axs[1].fill_between(e[:,0], errdown, errup, alpha=0.4, color = '{:s}'.format(linecolor2[int(p.parts[-2][2])-2]))
    axs[1].legend(fontsize=8)
    

axs[0].set_ylim(0.0, 0.17)
axs[0].set_ylabel(r'$P(R_g)$')
axs[0].set_xlim(35, 75)

axs[1].set_ylim(0.0, 0.17)
axs[1].set_ylabel(r'$P(R_g)$')
axs[1].set_xlim(35, 75)
axs[1].set_xlabel(r'$R_g\ [Å]$')

fig.savefig('fig/rg_neg_pos_40_rev4.pdf')
