from numpy import *
import matplotlib.pyplot as plt

# Load non-hydrophone gauge (change gauge number to change plot)
t, p = loadtxt('a-pgauge2_non.dat', unpack=True, usecols=[0,1])
# Load hydrophone gauge (change gauge number to change plot)
th, ph = loadtxt('a-pgauge2_hyd.dat', unpack=True, usecols=[0,1])

#Set vapor pressure line
xcav = [-3.0,300]
ycav = [-14.334351113,-14.334351113]

#Change units to Psi and microseconds
p = p*0.000145038 - 14.6959488
ph = ph*0.000145038 - 14.6959488
t = t*1000000
th = th*1000000


# Set plotting parameters
plt.xlabel("Time (microseconds)",fontsize=20)
plt.ylabel("Pressure (psi)",fontsize=20)
plt.xlim([40,150])
plt.ylim([-20,35])
plt_non, = plt.plot(t,p,'k-',linewidth=2.0)
plt_hyd, = plt.plot(th,ph,'r--',linewidth=3.0)
plt_vap, = plt.plot(xcav,ycav,'b--',linewidth=5.0)
plt.legend([plt_non, plt_hyd, plt_vap], ["Original", "Hydrophone", "Vapor pressure"])
plt.show()


