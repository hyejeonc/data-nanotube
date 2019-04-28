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
    
#    m40nree.append(d)  
#    m40nreelabel.append(labelstring)
    
    plt.figure(1)
    axs[0].plot(d[:,0], d[:,1], label = labelstring,\
                    color = '{:s}'.format(linecolor1[int(p.parts[-2][2])-2]), linestyle = '-')         
    axs[0].legend(fontsize = 8)
#    axs[0].text(31,0.14, '(a)', fontsize=10)
#   axs[0].legend([(a)], loc= upper left)
#    fig2 = plt.plot(e[:,0], e[:,1], label = labelstring,\
#                    color = '{:s}'.format(linecolor1[int(p.parts[-2][2])-2]), linestyle = '-.')         

#    plot_lines.append([fig1, fig2])
#legend1.append(plt.legend(fig1))
#plt.legend(fig1)


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
    
    #fig1 = plt.plot()
    axs[1].plot(e[:,0], e[:,1], label = labelstring, \
                    color = '{:s}'.format(linecolor2[int(p.parts[-2][2])-2]), linestyle = '-')         
    axs[1].legend(fontsize=8)
    
    
    
        
#    axs[1].text(31,0.14, '(b)', fontsize=10)
#plt.legend(fig2)
#plt.legend([legend2])
#legend1 = plt.legend(plot_lines[0], ["algo1", "algo2", "algo3"], loc=1)
#l2 = plt.legend([fig2], [ph], loc=4)

#axs[0].set_yticks(np.arange(-0.9, 1.0, 0.4))
axs[0].set_ylim(0.0, 0.17)
axs[0].set_ylabel(r'$g(r)$')
axs[0].set_xlim(30, 80)
axs[0].set_title(r'$R_g$')

#axs[1].set_yticks(np.arange(0.1, 1.0, 0.2))
axs[1].set_ylim(0.0, 0.17)
axs[1].set_ylabel(r'$g(r)$')
axs[1].set_xlim(30, 80)
axs[1].set_xlabel(r'$r\ [Å]$')

fig.savefig('fig/rg_neg_pos_40_forlegend1.pdf')
'''
axs[2].plot(t, s3)
axs[2].set_yticks(np.arange(-0.9, 1.0, 0.4))
axs[2].set_ylim(-1, 1)
'''
#plt.ylim(0.000, 0.150)

#plt.ylabel('[Å]')
#plt.title(r'$R_g$') 


#plt.ylabel('[Å]')
#plt.title('m30m10 Ree') 

#############################################
#############################################
'''
for p in sorted(Path('alsi/polymer/quenchedpoly/m5m30m5/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    d = mu.getDistribution(p, 'rg pa')    
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    reetemp = d
#    m40nree.append(d)  
#    m40nreelabel.append(labelstring)
    
    plt.figure(1)    
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]), linestyle = '-')         
plt.legend()
plt.ylim(0.000, 0.150)
#plt.ylabel('[Å]')
plt.title('m5m30m5 Rg') 

for p in sorted(Path('alsi/polymer/quenchedpoly/m5m30m5/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    d = mu.getDistribution(p, 'ree pa')    
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    reetemp = d
#    m40nree.append(d)  
#    m40nreelabel.append(labelstring)
    
    plt.figure(2)    
    plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]), linestyle = '-')         
plt.legend()
plt.ylim(0.000, 0.150)
#plt.ylabel('[Å]')
plt.title('m5m30m5 Ree')
'''