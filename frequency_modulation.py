import matplotlib.pyplot as plt
import matplotlib.pylab as pyl
# import numpy as np

# time gap
sample_gap = 0.0001
ts = pyl.arange(0, 1, sample_gap)


# Input signal
yi = pyl.sin(2 * pyl.pi * ts * 1)

# Showing input signal
plt.subplot(5, 1, 1)
plt.title('Input Signal')
plt.plot(ts, yi)
plt.ylabel('Amplitude')
plt.xlabel('Time')

# Carrier signal
fc = 10
yc = pyl.sin(2 * pyl.pi * ts * fc)

# Showing carrier signal
plt.subplot(5, 1, 3)
plt.title('Carrier Signal')
plt.plot(ts, yc)
plt.ylabel('Amplitude')
plt.xlabel('Time')

# Modulated signal
mod_factor = 15
updated_y = pyl.sin(2 * pyl.pi * (fc + (yi*mod_factor)) * ts)

# Showing Modulated signal
plt.subplot(5, 1, 5)
plt.title('Modulated Signal')
plt.plot(ts, updated_y)
plt.ylabel('Amplitude')
plt.xlabel('Time')

plt.show()
