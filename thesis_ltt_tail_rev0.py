import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pylab as py

##fixing numbers, opposite charge : neg/pos

strtype = ['m40nretry', 'm40pretry']#, 'm10m20m10', 'm5m30m5', 'm30m10', 'm40nretry'] #'m10m10m10m10', 'm5m10m5'] 
chargeratio = ['0', '0']#, '1', '3', '3', '0']

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
    '''
    len_io_loop.append([])
    len_io_loop_errdown.append([])
    len_io_loop_errup.append([])
#    len_io_tail.append([])
#    len_io_train.append([])
    
    len_i_loop.append([])
    len_i_loop_errdown.append([])
    len_i_loop_errup.append([])
#    len_i_tail.append([])
#    len_i_train.append([])
    
    len_o_loop.append([])
    len_o_loop_errdown.append([])
    len_o_loop_errup.append([])
#    len_o_tail.append([])
#    len_o_train.append([])
    num_io_loop.append([])
    num_io_loop_errdown.append([])
    num_io_loop_errup.append([])
    
    num_i_loop.append([])
    num_i_loop_errdown.append([])
    num_i_loop_errup.append([])
    
    num_o_loop.append([])
    num_o_loop_errdown.append([])
    num_o_loop_errup.append([])
    
    seg_io_loop.append([])
    seg_io_loop_errdown.append([])
    seg_io_loop_errup.append([])
    
    seg_i_loop.append([])
    seg_i_loop_errdown.append([])
    seg_i_loop_errup.append([])
    
    seg_o_loop.append([])
    seg_o_loop_errdown.append([])
    seg_o_loop_errup.append([])
'''
    
    ph = []
    for p in sorted(Path(str(pathstring[j])).glob('zero/ph*/cylinder_shell.out')):
#    zip(pathstring, linecolor)    
        print(p)  
        #io_loops = mu.gettubeIOLTT(p, 'loops')  #choose itube/otube/iotube 
        #io_tails = mu.gettubeIOLTT(p, 'tails')
        #io_trains = mu.gettubeIOLTT(p, 'trains')        
        i_loops = mu.gettubeILTT(p, 'tails')  #choose itube/otube/iotube 
        i_tails = mu.gettubeILTT(p, 'tails')
        i_trains = mu.gettubeILTT(p, 'trains')   
        
        o_loops = mu.gettubeOLTT(p, 'tails')  #choose itube/otube/iotube 
        o_tails = mu.gettubeOLTT(p, 'tails')
        o_trains = mu.gettubeOLTT(p, 'trains')  
        
##    Input:  fin - file in
##            restype - type of result. Can be 'loops', 'tails', 'trains' or 'adsorbed'
##    Output: 2D array of results on the form
##                [number of x]                   [variation (fluctuation)],
##                [length of x]                   [variation],
##                [number of segments in x]       [variation]
##            in the case of x = 'loops', 'tails' or 'trains', or on the form
##                [number of adsorbed chains]     [variation],
##                [number of adsorbed segments]   [variation]
##            in the case of 'adsorbed'
##    Note: loops, tails and trains are average number per (adsorbed?) chain!
        
        print(p.parts[-4])
        if p.parts[-4] == 'm40nretry':
            titlestring = 'neg'
        else: 
            titlestring = 'pos'
            #titlestring = '{:s}'.format(str(p.parts[-4]))
            
        labelstring = 'pH = {:d}'.format(int(p.parts[-2][2]))
        
        print(p.parts)
        print(p.parts[-4])
        print(p.parts[-2])
        print(p.parts[-2][2])
        ph.append(p.parts[-2][2])
        
        len_io_loop.append(max(i_loops[1][0], o_loops[1][0]))
        len_io_loop_errdown.append\
        (min((i_loops[1][0]-0.5*i_loops[1][1]), (o_loops[1][0]-0.5*o_loops[1][1])))
        len_io_loop_errup.append\
        (max((i_loops[1][0]+0.5*i_loops[1][1]), (o_loops[1][0]+0.5*o_loops[1][1])))
 
        len_i_loop.append(i_loops[1][0])
        len_i_loop_errdown.append(i_loops[1][0]-0.5*i_loops[1][1])
        len_i_loop_errup.append(i_loops[1][0]+0.5*i_loops[1][1])
        
        len_o_loop.append(o_loops[1][0])
        len_o_loop_errdown.append(o_loops[1][0]-0.5*o_loops[1][1])
        len_o_loop_errup.append(o_loops[1][0]+0.5*o_loops[1][1])

        num_io_loop.append(max(i_loops[0][0], o_loops[0][0]))
        num_io_loop_errdown.append\
        (min((i_loops[0][0]-0.5*i_loops[0][1]), (o_loops[1][0]-0.5*o_loops[1][1])))
        num_io_loop_errup.append\
        (max((i_loops[0][0]+0.5*i_loops[0][1]), (o_loops[1][0]+0.5*o_loops[1][1])))

        num_i_loop.append(i_loops[0][0])
        num_i_loop_errdown.append(i_loops[0][0]-0.5*i_loops[0][1])
        num_i_loop_errup.append(i_loops[0][0]+0.5*i_loops[0][1])
        
        num_o_loop.append(o_loops[0][0])
        num_o_loop_errdown.append(o_loops[0][0]-0.5*o_loops[0][1])
        num_o_loop_errup.append(o_loops[0][0]+0.5*o_loops[0][1])
        
        seg_io_loop.append(max(i_loops[2][0], o_loops[2][0]))
        seg_io_loop_errdown.append\
        (min((i_loops[2][0]-0.5*i_loops[2][1]), (o_loops[2][0]-0.5*o_loops[2][1])))
        seg_io_loop_errup.append\
        (max((i_loops[2][0]+0.5*i_loops[2][1]), (o_loops[2][0]+0.5*o_loops[2][1])))

        seg_i_loop.append(i_loops[2][0])
        seg_i_loop_errdown.append(i_loops[2][0]-0.5*i_loops[2][1])
        seg_i_loop_errup.append(i_loops[2][0]+0.5*i_loops[2][1])
        
        seg_o_loop.append(o_loops[2][0])
        seg_o_loop_errdown.append(o_loops[2][0]-0.5*o_loops[2][1])
        seg_o_loop_errup.append(o_loops[2][0]+0.5*o_loops[2][1])        
#        len_i_tail.append(i_tails[1][0])
#        len_i_tail_errdown.append(i_tails[1][0]-i_tails[1][1])
#        len_i_tail_errup.append(i_tails[1][0]+i_tails[1][1])
        
#        len_i_train.append(i_trains[1][0]) 
#        len_i_train_errdown.append(i_trains[1][0]-i_trains[1][1]) 
#        len_i_train_errup.append(i_trains[1][0]+i_trains[1][1])        
        
#        len_o_tail.append(o_tails[1][0])
#        len_o_train.append(o_trains[1][0]) 
        
        #num_io_loop.append(io_loops[0][0])
        #num_io_tail.append(io_tails[0][0])
        #num_io_train.append(io_trains[0][0]) 
        '''        
        num_i_loop.append(i_loops[0][0])
        num_i_tail.append(i_tails[0][0])
        num_i_train.append(i_trains[0][0]) 
        
        num_o_loop.append(o_loops[0][0])
        num_o_tail.append(o_tails[0][0])
        num_o_train.append(o_trains[0][0])
        
        #seg_io_loop.append(io_loops[2][0])
        #seg_io_tail.append(io_tails[2][0])
        #seg_io_train.append(io_trains[2][0]) 
        
        seg_i_loop.append(i_loops[2][0])
        seg_i_tail.append(i_tails[2][0])
        seg_i_train.append(i_trains[2][0]) 
        
        seg_o_loop.append(o_loops[2][0])
        seg_o_tail.append(o_tails[2][0])
        seg_o_train.append(o_trains[2][0])

       # io_ads = mu.gettubeIOLTT(p, 'adsorbed')  #choose itube/otube/iotube 
        i_ads = mu.gettubeILTT(p, 'adsorbed')
        o_ads = mu.gettubeOLTT(p, 'adsorbed')
        
       # numads_io_chain.append(io_ads[0][0])
        numads_i_chain.append(i_ads[0][0])
        numads_o_chain.append(o_ads[0][0])
        
       # numads_io_seg.append(io_ads[1][0])
        numads_i_seg.append(i_ads[1][0])
        numads_o_seg.append(o_ads[1][0])
        '''
    plt.figure(1)
    axs[0].plot(ph, len_o_loop, label = titlestring,\
                    color = linecolor1[j], linestyle = '-')         
    axs[0].fill_between(ph, len_o_loop_errdown, len_io_loop_errup, color = linecolor1[j], alpha = 0.2 )
    axs[0].legend(fontsize = 8)
    axs[0].set_ylim(-0.2, 30)
   # axs[0].gca().yaxis.grid(True)
    axs[0].set_ylabel(r'$<l_{tail}>$')
    
    #axs[0].set_xlim(50, 270)
    
    axs[1].plot(ph, num_o_loop, label = titlestring,\
                    color = linecolor1[j] , linestyle = '-')         
    axs[1].fill_between(ph, num_o_loop_errdown, num_o_loop_errup, color = linecolor1[j], alpha = 0.2 )
    #axs[1].legend(fontsize = 8)
    axs[1].set_ylabel(r'$<N_{tail}>$'+'\n')
    axs[1].set_ylim(-0.2, 3.0)
    #axs[1].yaxis.grid()    
    
    axs[2].plot(ph, seg_o_loop, label = titlestring,\
                    color = linecolor1[j], linestyle = '-')         
    axs[2].fill_between(ph, seg_o_loop_errdown, seg_o_loop_errup, color = linecolor1[j], alpha = 0.2 )
    #axs[2].legend(fontsize = 8)
    axs[2].set_ylabel(r'$<N_{seg,tail}>$')
    axs[2].set_ylim(-0.2, 39)
    
    

   # axs[2].yaxis.grid()  
fig.savefig('fig/tail_neg_pos_40_rev1.pdf') 

    
'''
    plt.figure(10)       
   # plt.plot(ph[:], numads_io_chain[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor1[j]))   
    plt.plot(ph[:], numads_i_chain[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor1[j])) 
    plt.plot(ph[:], numads_o_chain[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor1[j])) 

    plt.figure(11)       
   # plt.plot(ph[:], numads_io_seg[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor1[j]))   
    plt.plot(ph[:], numads_i_seg[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor1[j])) 
    plt.plot(ph[:], numads_o_seg[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor1[j]))  

    
    plt.figure(1)       
   # plt.plot(ph[:], len_io_loop[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor1[j]))   
    plt.plot(ph[:], len_i_loop[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor1[j])) 
    plt.plot(ph[:], len_o_loop[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor1[j])) 

    plt.figure(2)       
   # plt.plot(ph[:], num_io_loop[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor1[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], num_i_loop[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor1[j]))   #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], num_o_loop[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor1[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     

    plt.figure(3)       
   # plt.plot(ph[:], seg_io_loop[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor1[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], seg_i_loop[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor1[j]))  
    plt.plot(ph[:], seg_o_loop[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor1[j]))   #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     

    plt.figure(4)       
   # plt.plot(ph[:], len_io_tail[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor1[j]))   
    plt.plot(ph[:], len_i_tail[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor1[j])) 
    plt.plot(ph[:], len_o_tail[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor1[j])) 

    plt.figure(5)       
   # plt.plot(ph[:], num_io_tail[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor1[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], num_i_tail[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor1[j]))   #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], num_o_tail[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor1[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     

    plt.figure(6)       
   # plt.plot(ph[:], seg_io_tail[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor1[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], seg_i_tail[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor1[j]))  
    plt.plot(ph[:], seg_o_tail[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor1[j]))   #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     

    plt.figure(7)       
   # plt.plot(ph[:], len_io_train[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor1[j]))   
    plt.plot(ph[:], len_i_train[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor1[j])) 
    plt.plot(ph[:], len_o_train[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor1[j])) 

    plt.figure(8)       
   # plt.plot(ph[:], num_io_train[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor1[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], num_i_train[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor1[j]))   #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], num_o_train[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor1[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     

    plt.figure(9)       
   # plt.plot(ph[:], seg_io_train[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor1[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], seg_i_train[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor1[j]))  
    plt.plot(ph[:], seg_o_train[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor1[j]))   #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
'''
'''    
plt.figure(11)
#plt.title('\nLoop Analysis, inner+outer')
plt.ylim(0.0, 40.0)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{ads}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'ads_num' + '-io.pdf')   

plt.figure(10)
#plt.title('\nLoop Analysis, inner')
plt.ylim(0.0, 1.0)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{ads, chain}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'ads_chain' + '-io.pdf')

plt.figure(1)
#plt.title('\nLoop Analysis, inner+outer')
plt.ylim(0.0, 40.0)
#    plt.xlim(0, 40)
plt.ylabel(r'$<l_{loop}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'loop-len' + '-io.pdf')   

plt.figure(2)
#plt.title('\nLoop Analysis, inner')
plt.ylim(0.0, 1.5)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{loop}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'loop-num' + '-io.pdf')   

plt.figure(3)
#plt.title('\nLoop Analysis, inner')
plt.ylim(0.0, 40.0)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{seg-in-loop}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'loop-seg' + '-io.pdf')   

plt.figure(4)
#plt.title('\nLoop Analysis, inner+outer')
plt.ylim(0.0, 40.0)
#    plt.xlim(0, 40)
plt.ylabel(r'$<l_{tail}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'tail-len' + '-io.pdf')   

plt.figure(5)
#plt.title('\nLoop Analysis, inner')
plt.ylim(0.0, 2.0)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{tail}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'tail-num' + '-io.pdf')   

plt.figure(6)
#plt.title('\nLoop Analysis, inner')
plt.ylim(0.0, 40.0)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{seg-in-tail}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'tail-seg' + '-io.pdf')   

plt.figure(7)
#plt.title('\nLoop Analysis, inner+outer')
plt.ylim(0.0, 10.0)
#    plt.xlim(0, 40)
plt.ylabel(r'$<l_{train}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'train-len' + '-io.pdf')   

plt.figure(8)
#plt.title('\nLoop Analysis, inner')
plt.ylim(0.0, 10.0)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{train}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'train-num' + '-io.pdf')   

plt.figure(9)
#plt.title('\nLoop Analysis, inner')
plt.ylim(0.0, 10.0)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{seg-in-train}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'train-seg' + '-io.pdf')  
'''
