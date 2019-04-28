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
linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']
plot_lines = []
for p in sorted(Path('../alsi/polymer/quenchedpoly/0/m40nretry/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    d = mu.getDistribution(p, 'rg pa') 
    e = mu.getDistribution(p, 'ree pa') 
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    
#    m40nree.append(d)  
#    m40nreelabel.append(labelstring)
    
    plt.figure(1)
    fig1 = plt.plot(d[:,0], d[:,1], label = labelstring,\
                    color = '{:s}'.format(linecolor1[int(p.parts[-2][2])-2]), linestyle = '-')         
    fig2 = plt.plot(e[:,0], e[:,1], label = labelstring,\
                    color = '{:s}'.format(linecolor1[int(p.parts[-2][2])-2]), linestyle = '-.')         

    plot_lines.append([fig1, fig2])

lines = axes.get_lines()   
legend1 = plt.legend([lines[i] for i in [0,1,2]], ["algo1", "algo2", "algo3"], loc=1)
legend2 = plt.legend([lines[i] for i in [0,3,6]], parameters, loc=4)
axes.add_artist(legend1)
axes.add_artist(legend2)    
#legend1 = plt.legend(plot_lines[0], ["algo1", "algo2", "algo3"], loc=1)
#plt.legend([l[0] for l in plot_lines], ph, loc=4)
plt.gca().add_artist(legend1)

plt.ylim(0.000, 0.150)
plt.xlim(0, 250)
#plt.ylabel('[Å]')
plt.title(r'$R_g$ and $R_{ee}$')
#l1 = plt.legend([fig1], [ph], loc=1)
#fig.append(fig1)
#legend1 = plt.legend(fig)

'''
ph=[]
for p in sorted(Path('../alsi/polymer/quenchedpoly/0/m40pretry/zero/').glob('ph*/cylinder_shell.list')):
    print(p)  
    e = mu.getDistribution(p, 'rg pa')    
#    labelstring = 'ph = {:d}'.format( int(p.parts[1][2]) )
    labelstring = 'ph = {:d}'.format(int(p.parts[-2][2])) 
    print(p.parts)
    print(p.parts[-2])
    print(p.parts[-2][2])
    ph.append(p.parts[-2][2])
    reetemp = e
#    m40nree.append(d)  
#    m40nreelabel.append(labelstring)
    
    fig1 = plt.plot()
    fig2 = plt.plot(e[:,0], e[:,1], label = labelstring, color = '{:s}'.format(linecolor1[int(p.parts[-2][2])-2]), linestyle = '-')         
#legend2 = plt.legend(fig2)
#legend1 = plt.legend(plot_lines[0], ["algo1", "algo2", "algo3"], loc=1)
#l2 = plt.legend([fig2], [ph], loc=4)
'''
plt.ylim(0.000, 0.150)
plt.legend()
plt.xlim(0, 250)
#plt.ylabel('[Å]')
plt.title(r'$R_g$ and $R_{ee}$') 


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