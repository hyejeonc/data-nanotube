import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pylab as py

##fixing numbers, opposite charge : neg/pos


strtype = ['m40nretry', 'm40ncen'] 
chargeratio = ['0', '0']

#strtype = ['m40ncen', 'm40pcen'] 
#chargeratio = ['0', '0']
#strtype = ['m30m10', 'm5m30m5','m15m10m15']

pathstring  = []

linecolor = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']
linecolor3 = ['orange', 'saddlebrown', 'royalblue']
a = zip(strtype, linecolor)

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
    pathstring.append('alsi/polymer/quenchedpoly/{:s}'.format(str(chargeratio[i])) + '/{:s}/'.format(str(strtype[i])))

for j in range(len(pathstring)):
    len_io_loop = []
    len_io_tail = []
    len_io_train = []
    
    len_i_loop = []
    len_i_tail = []
    len_i_train = []
    
    len_o_loop = []
    len_o_tail = []
    len_o_train = []
    
    num_io_loop = []
    num_io_tail = []
    num_io_train = []
    
    num_i_loop = []
    num_i_tail = []
    num_i_train = []
    
    num_o_loop = []
    num_o_tail = []
    num_o_train = []   
    
    seg_io_loop = []
    seg_io_tail = []
    seg_io_train = []
    
    seg_i_loop = []
    seg_i_tail = []
    seg_i_train = []
    
    seg_o_loop = []
    seg_o_tail = []
    seg_o_train = []
    
    ph = []
    
    for p in sorted(Path(str(pathstring[j])).glob('zero/ph*/cylinder_shell.out')):
#    zip(pathstring, linecolor)    
        
        print(p)  
  
        io_loops = mu.gettubeIOLTT(p, 'loops')  #choose itube/otube/iotube 
        io_tails = mu.gettubeIOLTT(p, 'tails')
        io_trains = mu.gettubeIOLTT(p, 'trains')        

        i_loops = mu.gettubeILTT(p, 'loops')  #choose itube/otube/iotube 
        i_tails = mu.gettubeILTT(p, 'tails')
        i_trains = mu.gettubeILTT(p, 'trains')   
        
        o_loops = mu.gettubeOLTT(p, 'loops')  #choose itube/otube/iotube 
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
            titlestring = 'm40n'
        else: 
            titlestring = '{:s}'.format(str(p.parts[-4]))
        labelstring = 'ph = {:d}'.format(int(p.parts[-2][2]))
        
        print(p.parts)
        print(p.parts[-4])
        print(p.parts[-2])
        print(p.parts[-2][2])
        ph.append(p.parts[-2][2])
        
        #p.parts[-4].append(p.parts[-2][2])
        len_io_loop.append(io_loops[0, 0])
        len_io_tail.append(io_tails[0, 0])
        len_io_train.append(io_trains[0, 0]) 
        
        len_i_loop.append(i_loops[0, 0])
        len_i_tail.append(i_tails[0, 0])
        len_i_train.append(i_trains[0, 0]) 
        
        len_o_loop.append(o_loops[0, 0])
        len_o_tail.append(o_tails[0, 0])
        len_o_train.append(o_trains[0, 0]) 
        
        num_io_loop.append(io_loops[1, 0])
        num_io_tail.append(io_tails[1, 0])
        num_io_train.append(io_trains[1, 0]) 
        
        num_i_loop.append(i_loops[1, 0])
        num_i_tail.append(i_tails[1, 0])
        num_i_train.append(i_trains[1, 0]) 
        
        num_o_loop.append(o_loops[1, 0])
        num_o_tail.append(o_tails[1, 0])
        num_o_train.append(o_trains[1, 0])
        
        seg_io_loop.append(io_loops[2, 0])
        seg_io_tail.append(io_tails[2, 0])
        seg_io_train.append(io_trains[2, 0]) 
        
        seg_i_loop.append(i_loops[2, 0])
        seg_i_tail.append(i_tails[2, 0])
        seg_i_train.append(i_trains[2, 0]) 
        
        seg_o_loop.append(o_loops[2, 0])
        seg_o_tail.append(o_tails[2, 0])
        seg_o_train.append(o_trains[2, 0])
 
    plt.figure(1)       
    plt.plot(ph[:], len_io_loop[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor3[j]))   
    plt.plot(ph[:], len_i_loop[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor3[j])) 
    plt.plot(ph[:], len_o_loop[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor3[j])) 

    plt.figure(2)       
    plt.plot(ph[:], num_io_loop[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor3[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], num_i_loop[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor3[j]))   #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], num_o_loop[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor3[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     

    plt.figure(3)       
    plt.plot(ph[:], seg_io_loop[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor3[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], seg_i_loop[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor3[j]))  
    plt.plot(ph[:], seg_o_loop[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor3[j]))   #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     

    plt.figure(4)       
    plt.plot(ph[:], len_io_tail[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor3[j]))   
    plt.plot(ph[:], len_i_tail[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor3[j])) 
    plt.plot(ph[:], len_o_tail[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor3[j])) 

    plt.figure(5)       
    plt.plot(ph[:], num_io_tail[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor3[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], num_i_tail[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor3[j]))   #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], num_o_tail[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor3[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     

    plt.figure(6)       
    plt.plot(ph[:], seg_io_tail[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor3[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], seg_i_tail[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor3[j]))  
    plt.plot(ph[:], seg_o_tail[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor3[j]))   #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     

    plt.figure(7)       
    plt.plot(ph[:], len_io_train[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor3[j]))   
    plt.plot(ph[:], len_i_train[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor3[j])) 
    plt.plot(ph[:], len_o_train[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor3[j])) 

    plt.figure(8)       
    plt.plot(ph[:], num_io_train[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor3[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], num_i_train[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor3[j]))   #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], num_o_train[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor3[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     

    plt.figure(9)       
    plt.plot(ph[:], seg_io_train[:], linestyle = ':', marker = 'x', label = '{:s}'.format(titlestring)+' in/out', color = '{:s}'.format(linecolor3[j]))    #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.plot(ph[:], seg_i_train[:], linestyle = ':', marker = '+', label = '{:s}'.format(titlestring)+' in', color = '{:s}'.format(linecolor3[j]))  
    plt.plot(ph[:], seg_o_train[:], linestyle = ':', marker = '.', markersize = '6', label = '{:s}'.format(titlestring)+' out', color = '{:s}'.format(linecolor3[j]))   #, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     

plt.figure(1)
#plt.title('\nLoop Analysis, inner+outer')
#    plt.ylim(0.00, 1.00)
#    plt.xlim(0, 40)
plt.ylabel(r'$<l_{loop}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'loop-len' + '-io.pdf')   

plt.figure(2)
#plt.title('\nLoop Analysis, inner')
#    plt.ylim(0.00, 1.00)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{loop}}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'loop-num' + '-io.pdf')   

plt.figure(3)
#plt.title('\nLoop Analysis, inner')
#    plt.ylim(0.00, 1.00)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{seg-in-loop}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'loop-seg' + '-io.pdf')   

plt.figure(4)
#plt.title('\nLoop Analysis, inner+outer')
#    plt.ylim(0.00, 1.00)
#    plt.xlim(0, 40)
plt.ylabel(r'$<l_{train}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'tail-len' + '-io.pdf')   

plt.figure(5)
#plt.title('\nLoop Analysis, inner')
#    plt.ylim(0.00, 1.00)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{tail}}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'tail-num' + '-io.pdf')   

plt.figure(6)
#plt.title('\nLoop Analysis, inner')
#    plt.ylim(0.00, 1.00)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{seg-in-tail}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'tail-seg' + '-io.pdf')   

plt.figure(7)
#plt.title('\nLoop Analysis, inner+outer')
#    plt.ylim(0.00, 1.00)
#    plt.xlim(0, 40)
plt.ylabel(r'$<l_{train}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'train-len' + '-io.pdf')   

plt.figure(8)
#plt.title('\nLoop Analysis, inner')
#    plt.ylim(0.00, 1.00)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{train}}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'train-num' + '-io.pdf')   

plt.figure(9)
#plt.title('\nLoop Analysis, inner')
#    plt.ylim(0.00, 1.00)
#    plt.xlim(0, 40)
plt.ylabel(r'$<N_{seg-in-train}>$')
plt.xlabel(r'pH')
plt.legend()
py.savefig('{:s}'.format(titlestring) + 'train-seg' + '-io.pdf')  
'''
    plt.figure(2)        
    plt.plot(p.parts[-2][2], i_loops[0, 0], linestyle = '--', label = titlestring)#, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.title('{:s}'.format(titlestring)+'\nLoop Analysis, inner')

    plt.figure(3)        
    plt.plot(p.parts[-2][2], o_loops[0, 0], linestyle = '-.', label = titlestring)#, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
    plt.title('{:s}'.format(titlestring)+'\nLoop Analysis, outer')
'''

        
'''        
        plt.figure(2)
        #plt.subplot(312)        
        plt.plot(e[:,0], e[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
        plt.title('{:s}'.format(titlestring)+'\nProbability of inner tube surface')
        
        
        plt.figure(3)
        #plt.subplot(313)        
        plt.plot(d[:,0], f[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
        plt.title('{:s}'.format(titlestring)+'\nProbability of outer tube surface')
       
    #for k in range(len(pathstring)):   
    plt.figure(1)
    plt.ylim(0.000, 1.000)
    plt.ylabel('Prob(d<7.1Å)')
    plt.xlabel('Monomer index')
    plt.legend()
    
    plt.figure(2)
    plt.ylim(0.000, 1.000)
    plt.ylabel('Prob(d<7.1Å)')
    plt.xlabel('Monomer index')
    plt.legend()
    
    plt.figure(3)
    plt.ylim(0.000, 1.000)
    plt.ylabel('Prob(d<7.1Å)')
    plt.xlabel('Monomer index')
    plt.legend()

    plt.show()

    #    plt.title('{:s}'.format(titlestring)+'\nProbability of inner/outer tube surface')
'''    
    
    
    
    

