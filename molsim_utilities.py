import numpy as np
import mmap
import sys
import os.path
import scipy.constants as const
from matplotlib.transforms import Bbox

'''
Notes on functions and stuff:

x = np.fromstring(data.readline().decode(), dtype=float, count=3, sep=' '):
data.readline().decode() reads a _byteline_ from 'data', then decodes it into ascii.
The string is then converted into an array/list of three floats separated by a space
in the input string.
'''

# def getDir(base, runtype, nchains, nmon, pHmpK, control=False, alpha=-1):
#     ''' Return the correct dictionary name, given the root folder (base), type of run,
#         number of chains, number of monomers and pH - pK.'''

#     confdir = '{}/{}/{:d}x{:d}'.format(base, runtype, nchains, nmon)
#     if control:
#         confdir = '{}/{}/{}/{:d}'.format(base, runtype, 'control', nmon)

#     ''' Assumes integer pH-pK. Different statements as data has been saved as either
#         "+x" and "x" for, respectively, positive and negative pH-pKa, as "x" and "mx", or as "x" and "m/x".
#         Positive alpha sets the alpha value as the folder name, ignoring the pHmpK argument.'''

#     if alpha >= 0:
#         fdir = '{}/{:.2f}'.format(confdir, alpha)
#     elif (pHmpK < 0) and (os.path.isdir(confdir+'/m')):        # Neg. pH-pKa in their own folder ('m/x')
#         fdir = '{}/m/{}'.format(confdir, abs(pHmpK))
#     elif (pHmpK > 0) and (os.path.isdir(confdir+'/+{}'.format(pHmpK))): # Pos. pH-pKa saved as '+x'
#         fdir = '{}/+{}'.format(confdir, pHmpK)
#     else:                                                         # Pos. and neg. saved as 'x' and 'mx'
#         pHmpKstr = str(pHmpK) if pHmpK >= 0 else 'm{}'.format(abs(pHmpK))
#         fdir = '{}/{}'.format(confdir, pHmpKstr)

#     return fdir

def getDir(base, runtype, pHmpK, control=False, alpha=-1):
    ''' Return the correct directory name, given the root folder (base), type of run,
        and pH.'''
   
    confdir = '{}/{}'.format(base, runtype)
    if control:
        confdir = '{}/{}/{}/{:d}'.format(base, runtype, 'control', nmon)

    # ''' Positive alpha sets the alpha value as the folder name, ignoring the pH argument.'''
    
    # fdir = '{}/{:.1f}'.format(confdir, pH)
    # if alpha >= 0:
    #      fdir = '{}/{:.2f}'.format(confdir, alpha)

    if alpha >= 0:
        fdir = '{}/{:.2f}'.format(confdir, alpha)
    elif (pHmpK < 0) and (os.path.isdir(confdir+'/m')):        # Neg. pH-pKa in their own folder ('m/x')
        fdir = '{}/m/{}'.format(confdir, abs(pHmpK))
    elif (pHmpK > 0) and (os.path.isdir(confdir+'/+{}'.format(pHmpK))): # Pos. pH-pKa saved as '+x'
        fdir = '{}/+{}'.format(confdir, pHmpK)
    else:                                                         # Pos. and neg. saved as 'x' and 'mx'
        pHmpKstr = str(pHmpK) if pHmpK >= 0 else 'm{}'.format(abs(pHmpK))
        fdir = '{}/{}'.format(confdir, pHmpKstr)


    if os.path.isdir(fdir):
        return fdir
    else:
        print('Warning: {} is not found.'.format(fdir))
        return ''


def searchForString(fin, strsearch):
    ''' Checks if strsearch is found in fin    '''

    with open(fin, "r+b") as infile:
        data = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)  # Map file to memory, read only

        ind = data.find(strsearch)
        if ind == -1:
            #errmsg = "Error searching for \"{}\": Didn't find specified string".format(strsearch)
            return False

    return True



def full_extent(ax, pad=0.0):
    """Get the full extent of an axes, including axes labels, tick labels, and
    titles. Copied from https://stackoverflow.com/a/26432947 """
    # For text objects, we need to draw the figure first, otherwise the extents
    # are undefined.
    ax.figure.canvas.draw()
    items = ax.get_xticklabels() + ax.get_yticklabels()
    items += [ax, ax.title, ax.xaxis.label, ax.yaxis.label]
    
    bbox = Bbox.union([item.get_window_extent() for item in items])

    extent = bbox.expanded(1.0 + pad, 1.0 + pad)
    return extent.transformed(ax.get_figure().dpi_scale_trans.inverted())



def astr(atype):
    ''' Returns the string to search for in the output (.list) file for a given analysis type.
        Implemented as a dictionary, as a functioning replacement of a switch statement.'''
    return {
        'avg_contact'     : b'probability of chain bead-particle contacts',
        'contact'         : b'probability of chain bead-particle contacts',
        'avg_mon_chrg'    : b'Average charge of PE monomers',
        'chrg_mod'        : b'Charge modulus in a weak PE',
        'avg_part_chrg'   : b'Average charge of particles',
        'pe--pe-'         : b'rdf pe--pe-',  # hardcoded bullshit, could probably do better
        'pe--micelle'     : b'rdf pe--micelle',
        'pe--cion+'       : b'rdf pe--cion+',
        'pe--cion-'       : b'rdf pe--cion-',
        'cion+-cion+'     : b'rdf cion+-cion+',
        'cion+-cion-'     : b'rdf cion+-cion-',
        'cion+-micelle'   : b'rdf cion+-micelle',
        'micelle-micelle' : b'rdf micelle-micelle',
        'micelle-cion-'   : b'rdf micelle-cion-',
        'cion--cion-'     : b'rdf cion--cion-',
        'pe-'             : b'zden gr:1',
        'cion+'           : b'zden gr:2',
        'micelle'         : b'zden gr:3',
        'cion-'           : b'zden gr:4',
        'ree'             : b'ree ',
        'rg'              : b'rg ',
        'iotube'          : b'probability of chain bead-inner/outer tube',
        'itube'           : b'probability of chain bead-inner tube',
        'otube'           : b'probability of chain bead-outer tube',        
    }.get(atype, b'Unknown analysis type!')


    
def getDistribution(fin, dist=''):
    ''' Extracts distribution data from a given file.
    Input:  fin   - File in
            dist  - distribution type, as given in .list file
    Output: res   - 2D matrix of histogram data, in the form '[bin]  [value]  [std.dev.]'
    '''

    if not dist:
        errmsg = "Error in getDistribution(). dist-string is empty."
        sys.exit(errmsg)
    if not str(fin).endswith(('.list', '.listsim')):
        errmsg = "Not a .list file. Exiting getDistribution()."
        sys.exit(errmsg)


    with open(str(fin), "r+b") as infile:
        data = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)  # Map file to memory, read only

        #strsearch = astr(dist) if atype in ['rdf', 'zden']  else astr(atype)
        #strsearch = astr(dist) if len(dist) > 0 else astr(atype)

        ind = data.find(dist.encode())
        if ind == -1:
            errmsg = "getDistribution(): Error searching for \"{}\": Didn't find specified string.".format(dist)
            sys.exit(errmsg)

        data.seek(ind)
        data.readline()
        ndp = np.fromstring(data.readline().decode(), dtype=int, count=1, sep=' ')[0]
        nvals = 3
        res = np.zeros([ndp, nvals])
           
        for i in range(ndp):
            res[i] = np.fromstring(data.readline().decode(), dtype=float, count=3, sep=' ')

        return res


    
def distAnalysis(fin, atype, dist=''):
    ''' Extracts distribution data from a given file.
    Input:  fin   - File in
            atype - analysis type. Can be 'rdf', 'ree' or 'rg'.
            dist  - distribution type for atype = 'rdf'. See the function astr() for alternatives.
    Output: res   - 2D matrix of histogram data, in the form '[bin]  [value]  [std.dev.]'
    NOTE: Somewhat changed for use in 2NP-1PE project (strsearch, and first readline in case of rg)
    '''

    with open(fin, "r+b") as infile:
        data = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)  # Map file to memory, read only

        #strsearch = astr(dist) if atype in ['rdf', 'zden']  else astr(atype)
        strsearch = astr(dist) if len(dist) > 0 else astr(atype)

        if atype == 'rg':
            ind = data.find(b'chain type distribution functions')
            data.seek(ind)

        
        ind = data.find(strsearch)
        if ind == -1:
            errmsg = "Error searching for \"{}\": Didn't find specified string".format(strsearch)
            sys.exit(errmsg)

        data.seek(ind)
        data.readline()
        ndp = np.fromstring(data.readline().decode(), dtype=int, count=1, sep=' ')[0]
        nvals = 3
        res = np.zeros([ndp, nvals])
           
        for i in range(ndp):
            res[i] = np.fromstring(data.readline().decode(), dtype=float, count=3, sep=' ')

        return res


    
def monAnalysis(fin, atype, restype=''):
    ''' Extracts monomer data from a given file. Made for .listsim file, not tested with .outsim.
    Input:  fin     - File in
            atype   - analysis type. Can be 'contact', 'avg_mon_chrg' or 'chrg_mod'.
            restype - type of result to return. Can be '0m', '1m', '2m' or 'tt'
    Output: res     - 2D matrix of data, in the form '[mon]/[chrg]  [value]  [std.dev.]'
    '''

    with open(fin, "r+b") as infile:
        data = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)  # Map file to memory, read only

        strsearch = astr(atype)

        ind = data.find(strsearch)
        if ind == -1:
            errmsg = "Error searching for \"{}\": Didn't find specified string".format(strsearch)
            sys.exit(errmsg)

        data.seek(ind)
        data.readline()
        nchains = np.fromstring(data.readline().decode(), dtype=int, count=1, sep=' ')[0]
        nvals = 3
        ndp_max = 0 # data points to extract
        res = np.zeros([nchains, ndp_max, nvals])
        avgres = np.zeros([ndp_max, nvals])

        for i in range(nchains):
            data.readline()  # Skip line giving chain number and micelle particle number
            ndp = np.fromstring(data.readline().decode(), dtype=int, count=1, sep=' ')[0]

            if ndp > ndp_max:
                ndp_max = ndp
                res.resize([nchains, ndp_max, nvals])
                avgres.resize([ndp_max, nvals])

            chres = np.zeros([ndp, nvals])
            for j in range(ndp):
                # Write to res. Reads byteline from data,
                # decodes to ascii-string, converts to floats.
                # np.genfromtxt might be easier, but needs line number
                chres[j] = np.fromstring(data.readline().decode(), dtype=float, count=3, sep=' ')
                avgres[j][0] = chres[j][0]      # Monomer index
                avgres[j][1] += chres[j][1]     # Value
                avgres[j][2] += chres[j][2]**2  # Averaging variances

            res[i] = chres

        avgres[:,1] = avgres[:,1]/nchains
        avgres[:,2] = np.sqrt(avgres[:,2]/nchains)   # Standard deviation

    if atype == 'avg_contact':
        return avgres
    else:
        if restype == 'tt':
            return res[0,:]
        elif restype == '2m':
            return res[1,:]
        elif restype == '1m':
            return res[2,:]
        elif restype == '0m':
            return res[3,:]
        else:
            return res


def partCharge(fin, atype, ptype):
    ''' Extracts monomer data from a given file. Made for .list file, not tested with .outsim.
    Input:  fin     - File in
            atype   - analysis type. Can be 'avg_part_chrg'.
            ptype   - particle type.
    Output: res     - 2D matrix of data, in the form '[mon]/[chrg]  [value]  [std.dev.]'
    '''

    with open(fin, "r+b") as infile:
        data = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)  # Map file to memory, read only

        strsearch = astr(atype)
        ind = data.find(strsearch)
        if ind == -1:
            errmsg = "Error searching for \"{}\": Didn't find specified string".format(strsearch)
            sys.exit(errmsg)

        ind = data.find(ptype.encode())
        data.seek(ind)
        data.readline()
        
        ndp = np.fromstring(data.readline().decode(), dtype=int, count=1, sep=' ')[0] # data points to extract
        res = np.zeros([ndp, 3])

        for i in range(ndp):
            temp_res = np.fromstring(data.readline().decode(), dtype=float, count=3, sep=' ')
            res[i][0] = temp_res[0]
            res[i][1] = temp_res[1]
            res[i][2] = temp_res[2]
            
            ######
        return res


def getAvgPartCharge(fin, ptype):
    ''' Extract the final fractional charge of a given particle type
    Input:  fin     - File in
            ptype   - particle type.
    Output: res     - 1D vector of data, in the form '[chrg]  [precision]  [std.dev.]'
    '''

    with open(str(fin), "r+b") as infile:
        data = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)  # Map file to memory, read only

        strsearch = 'fractional charge: {}'.format(ptype).encode()
        ind = data.rfind(strsearch)
        if ind == -1:
            errmsg = "Error searching for \"{}\": Didn't find specified string".format(strsearch)
            sys.exit(errmsg)

        data.seek(ind)
        s = data.readline()

        ch_str = s[s.find(b'=')+1:].strip()
        res = np.fromstring(ch_str.decode(), dtype=np.float, count=3, sep=' ')

        return res


def extractLines(fin, valstr, nretvals, headstr=' ', stripstring='=', fres=True, valtype=np.float):
    ''' Utility function to extract lines of data from a .out(sim) file.
    Input:  fin         - file in
            valstr      - string or list of strings of values to search for
            nretvals    - number of values being returned
            headstr     - head string to search for, e.g. 'loop, tail, and train characteristics'
            stripstring - strip stripstring and everything to it's left. Is usually '=' or valstr
            fres        - if True, start searching for stripstring after final result
            valtype     - type of values
    Output: out_vals    - values of string or list of values for each string
    
    Note: Currently allows for list of valstr and stripstring, but assumes single value for 
          nretvals and valtype. Might need to include check for lists for these values,
          and if so update parameters for each valstr item.
          (Elements of) valstr are assumed to be strings, not byte arrays.
    '''

    if not fin.endswith(('.out', '.outsim')):
        errmsg = "Not an outsim file. Exiting extractLines()."
        sys.exit(errmsg)
    

    with open(fin, "r+b") as infile:
        data = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)  # Map file to memory, read only
        
        if fres:
            ind = data.find(b'f i n a l   r e s u l t')
            data.seek(ind)

        data.seek(data.find(headstr.encode()))

        if type(valstr) == str and type(stripstring) == str:
            data.seek(data.find(valstr.encode()))
            s = data.readline()
            out_val_str = s[s.find(stripstring.encode())+len(stripstring):].strip()
            out_vals = np.fromstring(out_val_str.decode(), dtype='|S6', count=nretvals, sep=' ')
        elif type(valstr) == list and type(stripstring) == str:
            out_vals = []
            for vs in valstr:
                data.seek(data.find(vs.encode()))
                s = data.readline()
                out_val_str = s[s.find(stripstring.encode())+len(stripstring):].strip()
                out_vals.append( np.fromstring(out_val_str.decode(), dtype=valtype, count=nretvals, sep=' ') )
        elif type(valstr) == list and type(stripstring) == list:
            out_vals = []
            for vs, ss in zip(valstr, stripstring):
                data.seek(data.find(vs.encode()))
                s = data.readline()
                out_val_str = s[s.find(ss.encode())+len(ss):].strip()
                out_vals.append( np.fromstring(out_val_str.decode(), dtype=valtype, count=nretvals, sep=' ') )
        else:
            errmsg = "Exiting extractLine(), only supports valstr and stripstring of type list or str\n\t\
            Input: valstr of type {:}, stripstring of type {:}".format(type(valstr), type(stripstring))
            sys.exit(errmsg)

    return out_vals
            

def checkpH(fin, pHmpK):
    ''' Checks if pH-pK of pe- and cion+ in outsim file are the same, and if they correspond to the input
        pHmpK. Returns pH value for pe- and cion+ given in outsim file. To ensure pH values given for
        folders are correct. '''
    
    if not fin.endswith(('.out', '.outsim')):
        errmsg = "Not an outsim file. Exiting extractLines()."
        sys.exit(errmsg)
    
    out_vals = np.array([100, 100], dtype=np.float)
    passed_test = True
    with open(fin, "r+b") as infile:
        data = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)  # Map file to memory, read only
        
        data.seek(data.find(b'particle data'))
        data.seek(data.find(b'bead'))
        s1 = data.readline()   # line with pe- bead information
        data.readline()        # line between
        s2 = data.readline()   # line with cion+ information
        out_val_str = s1[s1.find(b'bead')+4:].strip()
        out_vals[0] = np.array(out_val_str.decode().split())[5]
        out_val_str = s2[s2.find(b'cion+')+5:].strip()
        out_vals[1] = np.array(out_val_str.decode().split())[5]

        
    if not np.isclose(out_vals[0], out_vals[1]):
        print('==== WARNING! ====  pH-pK of pe- and cion+ differs in outsim file!')
        print('\t pe-: {:.1f}    cion+: {:.1f}'.format(out_vals[0], out_vals[1]))
        print('\t File: {:}'.format(fin))
        passed_test = False
    if not all( np.isclose([out_vals[0], out_vals[1]], [pHmpK]) ):
        print('==== WARNING! ====  pH-pK of pe- and/or cion+ in outsim file does not equal input pH (folder)!')
        print('\t Expected pH-pK: {:.1f}    pH-pK of pe-: {:.1f}    cion+: {:.1f}'.format(pHmpK, out_vals[0], out_vals[1]))
        print('\t File: {:}'.format(fin))
        passed_test = False

    return out_vals, passed_test


def getMeanForce(basedir, runtype, fname, pHrange, value_fields=[]):

    
    # If value_fields is not specified on input, select standard fields to extract
    # While the typical check for (non-)empty lists in python is to use if-else, this does
    # not hold for numpy arrays, hence why we check for it. Currently (30.10.17), extractLines()
    # will fail if anything but a string or Python list is given as input.
    if not value_fields and type(value_fields) != np.ndarray:
        value_fields = ['ucorr/kT', 'fcorr_z/kT', 'ubond/kT', 'fbond_z/kT', 'fhs/kT', 'area*diff(density)', 'f/kT']

    val_list = []
    for i, ph in enumerate(pHrange):
        confdir = getDir(basedir, runtype, ph)
        if not confdir:
            print('  Directory not found. Skipping.')
            continue

        fin = '{}/{}'.format(confdir, fname)
        if not os.path.isfile(fin):
            print('  File {} not found. Skipping'.format(fin))
            continue
        
        fin = '{}/{}'.format(confdir, fname)
       
        val_list.append( extractLines(fin, value_fields, 5, 'mean energies and forces') )
        
    return val_list


def getAdsChainFraction(basedir, runtype, fname, pHrange):

    headstr = 'Ratio of Fraction of chains adsorbed'
    value_fields = ['X_2m', 'X_1m', 'X_0m', 'mon of chain 1 in np1', 'mon of chain 1 in np2']
    sstring = ['=', '=', '=', value_fields[3], value_fields[4]]

    val_list = []
    for i, ph in enumerate(pHrange):
        confdir = getDir(basedir, runtype, ph)
        if not confdir:
            print('  Directory not found. Skipping.')
            continue

        fin = '{}/{}'.format(confdir, fname)
        if not os.path.isfile(fin):
            print('  File {} not found. Skipping'.format(fin))
            continue
        
        fin = '{}/{}'.format(confdir, fname)
        
        val_list.append( extractLines(fin, value_fields, 5, headstr, stripstring=sstring) )
        
    return val_list


def getLTT(fin, restype=''):

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

    if 'outsim' not in fin:
        errmsg = "Not an outsim file. Exiting getLTT()."
        sys.exit(errmsg)

    if 'tail' in restype.lower():
        strsearch = b'tail'
    elif 'train' in restype.lower():
        strsearch = b'train'
    elif 'loop' in restype.lower():
        strsearch = b'loop'
    elif 'ads' in restype.lower():
        strsearch = b'adsorbed'
    else:
        print('getLTT(): Can not find restype')
        return 0


    with open(fin, "r+b") as infile:
        data = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)  # Map file to memory, read only

        ind = data.seek(data.find(b'loop, tail, and train characteristics'))
        if ind == -1:
            errmsg = "Error searching for \"{}\": Didn't find specified string".format(strsearch)
            sys.exit(errmsg)
        data.readline()  # Ensure we're at the beginning of the next line,
                         # so e.g. data.seek(loop) doesn't find 'loop' in 'loop, tail, and train characteristics'

        if strsearch == b'adsorbed':
            ind = data.find(strsearch)
            data.seek(ind)

            s = data.readline()
            ch_str = s[s.find(b'=')+1:].strip()
            ads_ch = np.fromstring(ch_str.decode(), dtype=np.float, count=5, sep=' ')
            s = data.readline()
            seg_str = s[s.find(b'=')+1:].strip()
            ads_seg = np.fromstring(seg_str.decode(), dtype=np.float, count=5, sep=' ')

            return np.array([[ads_ch[0], ads_ch[2]], [ads_seg[0], ads_seg[2]]])


        data.seek(data.find(strsearch))
        s = data.readline()
        num_str = s[s.find(b'=')+1:].strip()
        num = np.fromstring(num_str.decode(), dtype=np.float, count=5, sep=' ')

        data.seek(data.find(strsearch))
        s = data.readline()
        len_str = s[s.find(b'=')+1:].strip()
        length = np.fromstring(len_str.decode(), dtype=np.float, count=5, sep=' ')

        data.seek(data.find(strsearch))
        s = data.readline()
        num_seg_str = s[s.find(b'=')+1:].strip()
        num_seg = np.fromstring(num_seg_str.decode(), dtype=np.float, count=5, sep=' ')

        return np.array([ [num[0], num[2]], [length[0], length[2]], [num_seg[0], num_seg[2]] ])


# Small conversion functions
# 1 C/m^2 = 6.24151 e/nm^2

def get_C_from_meqg(x, Ad, z=1):
    return 1e-3*x*z*const.N_A*const.e/Ad

def get_meqg_from_C(x, Ad, z=1):
    return 1e3*x*Ad/(z*const.N_A*const.e)



def titrationCurve(ax, ptype, basedir, runtype, fname, lbl, pHrange):
    ''' Plot titration curves to axes object.
        Input: ax      : axes object
               ptype   : string of particle/chain to analyze
               basedir : string of base directory
               runtype : string of runtype
               lbl     : label
               pHrange : range of pH-values '''
    
    alpha = np.zeros([pHrange.size])
    for i, ph in enumerate(pHrange):
        confdir = getDir(basedir, runtype, ph)
        if not confdir:
            print('  Directory not found. Skipping.')
            continue

        fin = '{}/{}'.format(confdir, fname)
        if not os.path.isfile(fin):
            print('  File {} not found. Skipping'.format(fin))
            continue
       
        #alpha[i] = avgCharge(fin, ptype)[0]

        fin = '{}/{}'.format(confdir, 'titr_sil.list')
        res = partCharge(fin, 'avg_part_chrg', ' ion')
        alpha[i] = np.average(res[:,1])
        
    ax.plot(pHrange, alpha, label=lbl)
    ax.set_ylabel('$\\alpha$')
    ax.set_xlabel('pH')


def micelleCArea(x, R, origin):
    ''' Finds the crossectional area covered by a micelle of radius R at position origin.
        Returns a poly1d object giving the upper limit of the curve.
    '''

    A = np.pi*R**2*np.sin(np.arccos(x/R))**2
    fit = np.polyfit(x+origin,A,2)
    pol = np.poly1d(fit)

    return (pol, A)


def drawMicelleCrossArea(ax, R, origin, color='C0', alpha='.25', vlines=False):
    ''' Draws the crossectional area covered by a micelle of radius R at position origin on axes ax.
        If vline == True, vertical lines are drawn from llim to ulim at (origin-R) and (origin+R)
    '''
    
    x = np.linspace(-R,R,1000)
    pol, A = micelleCArea(x, R, origin)

    lines = ax.get_lines()
    if lines:   # if there are other lines in the plot, scale the upper/lower limits accordingly
        maxval = 0
        minval = np.inf
        for l in lines:
            if np.max( l.get_data()[1] ) > maxval:
                maxval = np.max( l.get_data()[1] )

            if np.min( l.get_data()[1] ) < minval:
                minval = np.min( l.get_data()[1] )
                
    else:       # if lines is empty, i.e. we have no lines to scale after
        maxval = np.max(pol(x))
        minval = 0
            
    x = x + origin
    scale = maxval / np.max(pol(x))

    ulim = pol(x)*scale
    np.copyto(ulim, minval, where = ulim < minval)

    llim = minval
    ax.fill_between(x, ulim, llim, color=color, alpha=alpha)

    if vlines:
        ax.vlines([origin-R, origin+R], ymin=minval, ymax=maxval,  linestyle=':', lw=.8)
