import numpy as np
import matplotlib.pyplot as plt

# Function to get the timestamps of the waveform
def getTime(time,dt):
    return time + dt

# Set the path to the data file
dir_name = 'waveforms/RefCurve_2023-12-10_11_045341'
#dir_name = 'waveforms/RefCurve_2023-12-08_2_022855'

waveforms = np.load(dir_name+'/waveforms.npy')
time = np.load(dir_name+'/time.npy')
ttime = np.load(dir_name+'/ttime.npy')
charge = np.array([])

tdist = np.diff(ttime)

# histogram on log scale. 
plt.subplot(211)
hist, bins, _ = plt.hist(tdist, bins=100)
# Use non-equal bin sizes, such that they look equal on log scale.
logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
plt.subplot(212)
plt.hist(tdist, bins=logbins)
plt.xscale('log')
plt.show()

for i in range(len(waveforms)):
    #print(wfm)
    # Plot the first waveform
    if (waveforms[i]==waveforms[0]).all():
        plt.figure()
        plt.plot(getTime(time,ttime[i]),waveforms[i])
        plt.xlabel('Time (s)')
        plt.ylabel('Current (A')
        plt.show()

    charge = np.append(charge,np.sum(waveforms[i])*(time[1]-time[0])/50) # charge in C
    avalanches = charge/1.6e-19/1e6
    intensity = avalanches/0.3


plt.figure()
plt.hist(charge,bins=100)
plt.show()