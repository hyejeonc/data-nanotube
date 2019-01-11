import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt 
ph = np.array([2, 3, 4, 5, 6, 7, 8])

#first row = Al, second row = Si
alsi_100 = np.array([[1, 1, 1, 1, 0.998, 0.986, 0.928],[0, 0.016, 0.108, 0.338, 0.73, 0.975, 0.998]])
alsi_180 = np.array([[1, 1, 1, 0.989, 0.997, 0.966, 0.729],[0,	0.01,	0.107, 0.428, 0.818, 0.987, 0.996]])
alsi_240 = np.array([[1, 1, 1, 0.999, 0.993, 0.890, 0.619],[0,	0.007, 0.110, 0.487, 0.880, 0.983, 0.999]])
alsi_500 = np.array([[1, 1, 1, 0.986, 0.928, 0.683, 0.352],[0,	0.006, 0.115, 0.623, 0.931, 0.989, 1.000]])

alsi_100_ch = np.array([[1, 1, 1, 1, 0.999, 0.990, 0.852],[0.001, 0.026, 0.161, 0.493, 0.849, 0.972, 0.999]])
alsi_180_ch = np.array([[1, 1, 1, 0.989, 0.997, 0.966, 0.729],[0, 0.01,	0.107, 0.428, 0.818, 0.987, 0.996]])
alsi_240_ch = np.array([[1, 1, 1, 0.999, 0.974, 0.923, 0.661],[0,	0.006, 0.103, 0.423, 0.846, 0.978, 0.999]])
alsi_500_ch = np.array([[1, 1, 1, 0.997, 0.947, 0.721, 0.395],[0,	0.003, 0.075, 0.447, 0.866, 0.985, 0.999]])

al_60_si_180 = np.array([[1, 1, 1, 0.997, 0.976, 0.717, 0.304],[0.006,	0.003, 0.051, 0.286, 0.721, 0.945, 0.996]])
'''
#marker='o', markersize=2, 
plt.plot(ph[:], al_60_si_180[0, :], color='royalblue', label='dcap180, Al only')
plt.plot(ph[:], al_60_si_180[1, :], color = 'darkorange', label='dcap180, Si only')
plt.xlabel('pH')
plt.ylabel('fractional charge')
plt.ylim(-0.1, 1.1)
plt.legend(loc="left")
#plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
plt.show()

plt.plot(ph[:], al_60_si_180[0, :], color='royalblue', label='dcap180, Al only', linestyle='--')
plt.plot(ph, alsi_100[0, :], color='lightskyblue', label='dcap100, Al')
plt.plot(ph, alsi_180[0, :], color='royalblue', label='dcap180, Al') 
plt.plot(ph, alsi_240[0, :], color='blue', label='dcap240, Al')
plt.plot(ph, alsi_500[0, :], color='darkblue', label='dcap500, Al')
plt.xlabel('pH')
plt.ylabel('fractional charge')
plt.legend(loc="left")
plt.ylim(-0.1, 1.1)
plt.show()


plt.plot(ph[:], al_60_si_180[1, :], color='darkorange', label='dcap180, Si only', linestyle='--')
plt.plot(ph, alsi_100[1, :], color='orange', label='dcap100, Si')
plt.plot(ph, alsi_180[1, :], color='darkorange', label='dcap180, Si') 
plt.plot(ph, alsi_240[1, :], color='chocolate', label='dcap240, Si')
plt.plot(ph, alsi_500[1, :], color='saddlebrown', label='dcap500, Si')
plt.xlabel('pH')
plt.ylabel('fractional charge')
plt.legend(loc="left")
plt.ylim(-0.1, 1.1)
plt.show()


plt.plot(ph[:], al_60_si_180[0, :], color='royalblue', label='dcap180, Al only', linestyle='--')
plt.plot(ph[:], al_60_si_180[1, :], color='darkorange', label='dcap180, Si only', linestyle='--')
plt.plot(ph, alsi_100_ch[0, :], color='lightskyblue', label='dcap100, Al', linestyle='-.')
plt.plot(ph, alsi_100[1, :], color='orange', label='dcap100, Si', linestyle='-.')
plt.plot(ph, alsi_500[0, :], color='darkblue', label='dcap500, Al')
plt.plot(ph, alsi_500[1, :], color='saddlebrown', label='dcap500, Si')
plt.xlabel('pH')
plt.ylabel('fractional charge')
plt.legend(loc="left")
plt.ylim(-0.1, 1.1)
plt.show()


plt.plot(ph[:], al_60_si_180[0, :], color='royalblue', label='dcap180, Al only', linestyle='--')
plt.plot(ph, alsi_100_ch[0, :], color='lightskyblue', label='dcap100, $\sigma$, Al')
plt.plot(ph, alsi_180_ch[0, :], color='royalblue', label='dcap180, $\sigma$, Al') 
plt.plot(ph, alsi_240_ch[0, :], color='blue', label='dcap240, $\sigma$, Al')
plt.plot(ph, alsi_500_ch[0, :], color='darkblue', label='dcap500, $\sigma$, Al')
plt.xlabel('pH')
plt.ylabel('fractional charge')
plt.legend(loc="left")
plt.ylim(-0.1, 1.1)
plt.show()

plt.plot(ph[:], al_60_si_180[1, :], color='darkorange', label='dcap180, Si only', linestyle='--')
plt.plot(ph, alsi_100_ch[1, :], color='orange', label='dcap100, $\sigma$, Si')
plt.plot(ph, alsi_180_ch[1, :], color='darkorange', label='dcap180, $\sigma$, Si') 
plt.plot(ph, alsi_240_ch[1, :], color='chocolate', label='dcap240, $\sigma$, Si')
plt.plot(ph, alsi_500_ch[1, :], color='saddlebrown', label='dcap500, $\sigma$, Si')
plt.xlabel('pH')
plt.ylabel('fractional charge')
plt.legend(loc="left")
plt.ylim(-0.1, 1.1)
plt.show()
'''

alsi_240_ch = np.array([[1, 1, 1, 0.999, 0.974, 0.923, 0.661],[0,	0.006, 0.103, 0.423, 0.846, 0.978, 0.999]])
alsi_240_ch_d = np.array([[1, 1, 1, 1,0.999, 0.990, 0.907],[0,	0, 0.386, 0.862, 0.984, 0.998, 0.907]])
al_60_si_240_d = np.array([1,1,1,1, .999, .990,.907],[.006,.059,.386,.836,.984,.998,1])



plt.plot(ph[:], al_60_si_240_d[0, :], color='royalblue', label='dcap240, Al only, debye 10Å', linestyle='--')
#plt.plot(ph, alsi_100_ch[0, :], color='lightskyblue', label='dcap100, $\sigma$, Al')
#plt.plot(ph, alsi_180_ch[0, :], color='royalblue', label='dcap180, $\sigma$, Al') 
plt.plot(ph, alsi_240_ch[0, :], color='blue', label='dcap240, $\sigma$, Al')
plt.plot(ph, alsi_240_ch_d[0, :], color='darkblue', label='dcap500, $\sigma$, Al, debye 10Å')
plt.xlabel('pH')
plt.ylabel('fractional charge')
plt.legend(loc="left")
plt.ylim(-0.1, 1.1)
plt.show()

plt.plot(ph[:], al_60_si_240_d[1, :], color='darkorange', label='dcap240, Si only, debye 10Å', linestyle='--')
#plt.plot(ph, alsi_100_ch[1, :], color='orange', label='dcap100, $\sigma$, Si')
#plt.plot(ph, alsi_180_ch[1, :], color='darkorange', label='dcap180, $\sigma$, Si') 
plt.plot(ph, alsi_240_ch[1, :], color='chocolate', label='dcap240, $\sigma$, Si')
plt.plot(ph, alsi_240_ch_d[1, :], color='saddlebrown', label='dcap240, $\sigma$, Si, debye 10Å')
plt.xlabel('pH')
plt.ylabel('fractional charge')
plt.legend(loc="left")
plt.ylim(-0.1, 1.1)
plt.show()



'''
fig1, ax1 = plt.subplots(1,1)

ax1.set_xlabel('pH')
ax1.set_ylabel('Fractional charge')

ax1.plot(ph, alpha_1, marker='o', markersize=10, label='alumina (Al100)')#linestyle='None')
ax1.plot(ph, alpha_2, marker='v', markersize=10, label='silica (Si100)')
ax1.plot(ph, alpha_al, color='tab:orange', marker='o', markersize=10, label='alumina (Al240)')#linestyle='None')
ax1.plot(ph, alpha_si, color='tab:orange', marker='v', markersize=10, label='silica (Si240)')
ax1.plot(ph, alpha_al500, linestyle='--', marker='o', markersize=10, label='alumina (Al500)')#linestyle='None')
ax1.plot(ph, alpha_si500, linestyle='--', marker='v', markersize=10, label='silica (Si500)')
'''
