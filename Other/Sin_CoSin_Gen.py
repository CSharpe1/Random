import numpy as np
import matplotlib.pyplot as plot

# step 1 Generate sine wave curve
# step 2 Plot onto graph
# step 3 Generate cosine wave
# step 4 Plot cosine onto graph
# step 5 

# Get x values of the sine wave 
time        = np.arange(0,3*np.pi,0.1);    #np.arange = 0,0.1,0.2,0.3 ... 10

# A sin(Omeage time)
# Frequency = 1/Time
# Time = 1/Frequency

# Amplitude of the sine wave is sine of a variable like time from above
amplitude1   = np.sin(time)
amplitude2   = np.cos(time)
plot.plot(time, amplitude1, time, amplitude2)

##########
plot.title('Wave')
plot.xlabel('Time')
plot.ylabel('Amplitude = sin(time)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()