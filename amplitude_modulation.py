import matplotlib.pyplot as plt
import numpy as np

# time axis
t = 500
ts = np.arange(0, 2, (1 / t))

# carrier signal
fc = 100
ac = 1
yc = ac * np.cos(2 * np.pi * fc * ts)
# Showing carrier signal
plt.subplot(5, 1, 3)
plt.title('Carrier Signal')
plt.plot(ts, yc)
plt.ylabel('Amplitude')
plt.xlabel('Time')

# input signal
fi = 2
ai = .5
yi = ai * np.sin(2 * np.pi * fi * ts)
# Showing input signal
plt.subplot(5, 1, 1)
plt.title('Input Signal')
plt.plot(ts, yi)
plt.ylabel('Amplitude')
plt.xlabel('Time')


# Modulated signal
ym = yc * (1 + (yi / ac))
# Showing Modulated signal
plt.subplot(5, 1, 5)
plt.title('Modulated Signal')
plt.plot(ts, ym)
plt.ylabel('Amplitude')
plt.xlabel('Time')

plt.show()
