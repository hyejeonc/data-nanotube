import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pylab as py
import pandas as pd

##fixing numbers, opposite charge : neg/pos

strtype = ['m40nretry', 'm40pretry', 'm40ncenxyz', 'm40pcenxyz'] #, 'm10m20m10', 'm5m30m5', 'm30m10', 'm40nretry'] #'m10m10m10m10', 'm5m10m5'] 
chargeratio = ['0', '0', '0', '0'] #, '1', '3', '3', '0']

#strtype = ['m40nretry', 'm40ncen', '] 
#chargeratio = ['0', '0']

#strtype = ['m40ncen', 'm40pcen'] 
#chargeratio = ['0', '0']
#strtype = ['m30m10', 'm5m30m5','m15m10m15']
fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0)

pathstring  = []

linecolor3 = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']
linecolor1 = ['orange', 'royalblue', 'green', 'purple', 'gray', 'yellow', 'navy' 'saddlebrown']
a = zip(strtype, linecolor3)

''' Extracts data about loops, tails, trains and adsorbed chains/monomers from Molsim's out-file.
Input:  fin - file in
        restype - type of result. Can be 'loops', 'tails', 'trains' or 'adsorbed'
Output: 2D array of results on the form
            [number of x]                   [variation (fluctuation)],
            [length of x]                   [variation],
            [number of segments in x]       [variation]
        in the case of x = 'loops', 'tails' or 'trains', or on the form
            [number of adsorbed chains]     [variation],
            [number of adsorbed segments]   [variation]
        in the case of 'adsorbed'
        Note: loops, tails and trains are average number per (adsorbed?) chain!
'''


    
for i in range(len(strtype)):
    pathstring.append('../alsi/polymer/quenchedpoly/{:s}'.format(str(chargeratio[i])) + '/{:s}/'.format(str(strtype[i])))


for j in range(len(pathstring)):
    len_io_loop = []
    len_io_loop_errdown = []
    len_io_loop_errup = []
    
    #len_io_tail = []
    #len_io_train = []
    
    len_i_loop = []
    len_i_loop_errdown = []
    len_i_loop_errup = []
    
    len_o_loop = []
    len_o_loop_errdown = []
    len_o_loop_errup = []
    
    seg_i_loop = []
    seg_i_loop_errdown = []
    seg_i_loop_errup = []
    
    num_i_loop = []
    num_i_loop_errdown = []
    num_i_loop_errup = []
    
    seg_o_loop = []
    seg_o_loop_errdown = []
    seg_o_loop_errup = []
    
    num_o_loop = []
    num_o_loop_errdown = []
    num_o_loop_errup = []
    
    seg_io_loop = []
    seg_io_loop_errdown = []
    seg_io_loop_errup = []
    
    num_io_loop = []
    num_io_loop_errdown = []
    num_io_loop_errup = []                                                                          

    
    ph = []
    for p in sorted(Path(str(pathstring[j])).glob('zero/ph*/cylinder_shell.out')):
#    zip(pathstring, linecolor)    
        print(p)  
        #io_loops = mu.gettubeIOLTT(p, 'loops')  #choose itube/otube/iotube 
        #io_tails = mu.gettubeIOLTT(p, 'tails')
        #io_trains = mu.gettubeIOLTT(p, 'trains')        
        i_loops = mu.gettubeILTT(p, 'adsorbed')  #choose itube/otube/iotube 
        o_loops = mu.gettubeOLTT(p, 'adsorbed')  #choose itube/otube/iotube 
        io_loops = i_loops + o_loops
               
        if j == 0:
            titlestring = 'neg, out'
        elif j == 1:
            titlestring = 'pos, out'
        elif j == 2:
            titlestring = 'neg, in'
        elif j == 3:
            titlestring = 'pos, in'
            
            #titlestring = '{:s}'.format(str(p.parts[-4]))
            
        labelstring = 'pH = {:d}'.format(int(p.parts[-2][2]))
        
        print(p.parts)
        print(p.parts[-4])
        print(p.parts[-2])
        print(p.parts[-2][2])
        ph.append(p.parts[-2][2])
        
        #adsorbed chain
        len_io_loop.append(io_loops[1][0])
        len_io_loop_errdown.append(io_loops[1][0]-0.5*io_loops[1][1])
        len_io_loop_errup.append(io_loops[1][0]+0.5*io_loops[1][1])
    
        len_i_loop.append(i_loops[1][0])
        len_i_loop_errdown.append(i_loops[1][0]-0.5*i_loops[1][1])
        len_i_loop_errup.append(i_loops[1][0]+0.5*i_loops[1][1])
        
        len_o_loop.append(o_loops[1][0])
        len_o_loop_errdown.append(o_loops[1][0]-0.5*o_loops[1][1])
        len_o_loop_errup.append(o_loops[1][0]+0.5*o_loops[1][1])

        #adsorbed segments
        seg_io_loop.append(io_loops[0][0])
        seg_io_loop_errdown.append(io_loops[0][0]-0.5*io_loops[0][1])
        seg_io_loop_errup.append(io_loops[0][0]+0.5*io_loops[0][1])
        
        seg_i_loop.append(i_loops[0][0])
        seg_i_loop_errdown.append(i_loops[0][0]-0.5*i_loops[0][1])
        seg_i_loop_errup.append(i_loops[0][0]+0.5*i_loops[0][1])
        
        seg_o_loop.append(o_loops[0][0])
        seg_o_loop_errdown.append(o_loops[0][0]-0.5*o_loops[0][1])
        seg_o_loop_errup.append(o_loops[0][0]+0.5*o_loops[0][1])        

        lendata = {}

    plt.figure(1)
    axs[0].plot(ph, len_io_loop, label = titlestring,\
                    color = linecolor1[j], linestyle = '-')         
    axs[0].fill_between(ph, len_io_loop_errdown, len_io_loop_errup, color = linecolor1[j], alpha = 0.2 )
    axs[0].legend(fontsize = 8)
   # axs[0].get_legend().set_legend_coords(7.5, 1.5)
    #axs[0].set_ylim(-0.2, 5.5)
   # axs[0].gca().yaxis.grid(True)
    axs[0].set_ylabel(r'$<l_{train}>$')
    axs[0].get_yaxis().set_label_coords(-0.07, 0.5)
    axs[0].set_xlabel(r'$pH$')
    #axs[0].set_xlim(50, 270)
    
    axs[1].plot(ph, num_io_loop, label = titlestring,\
                    color = linecolor1[j] , linestyle = '-')         
    axs[1].fill_between(ph, num_io_loop_errdown, num_io_loop_errup, color = linecolor1[j], alpha = 0.2 )
    #axs[1].legend(fontsize = 8)
    axs[1].set_ylabel(r'$<N_{train}>$')
    axs[1].get_yaxis().set_label_coords(-0.07, 0.5)
    #axs[1].set_ylim(-0.2, 5)
    axs[1].set_xlabel(r'$pH$')
    #axs[1].yaxis.grid()    
    
    axs[2].plot(ph, seg_io_loop, label = titlestring,\
                    color = linecolor1[j], linestyle = '-')         
    axs[2].fill_between(ph, seg_io_loop_errdown, seg_io_loop_errup, color = linecolor1[j], alpha = 0.2 )
    #axs[2].legend(fontsize = 8)
    axs[2].set_ylabel(r'$<N_{seg,train}>$')
    axs[2].get_yaxis().set_label_coords(-0.07, 0.5)
    #axs[2].set_ylim(-0.2, 19)
    axs[2].set_xlabel(r'$pH$')
    

    
fig.savefig('fig/train_neg_pos_inout_40_rev0.pdf') 
