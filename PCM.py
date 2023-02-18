import numpy as np
import matplotlib.pyplot as plt
# Define the analog signal parameters
freq = 2
amp = 1.2
phase = 0.2
dur = 5
Fs = 1000
T = 1/Fs

# Time array
t = np.arange(0, dur, T)

# Analog signal
A = 1.2 # Amplitude
y = amp * np.sin(2 * np.pi * freq * t + phase)

# Plotting the analog signal
plt.figure(figsize=(8, 2.5))
plt.plot(t, y)
plt.title('Analog Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid(False)
plt.show()

# Sampling the analog signal
sampling_rate = 20
sampling_times = np.arange(0, dur, 1/sampling_rate)
ys = np.interp(sampling_times, t, y)

# Plotting the sampling signal
plt.figure(figsize=(8, 2.5))
plt.stem(sampling_times, ys, 'r', )
plt.title('Sampling Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid(False)
plt.show()

# Quantizing the sampled signal
levels = 8
V_max = 2
quant_step = V_max/levels
quant_levels = np.arange(-V_max, V_max + quant_step, quant_step)
quant_ys = np.round(ys/quant_step) * quant_step

# Plotting the quantized signal
plt.figure(figsize=(8, 2.5))
plt.step(sampling_times, quant_ys, 'g', where='post')
plt.title('Quantized Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid(False)
plt.show()

# Implementing NRZ-L
digital_signal = np.zeros(len(quant_ys))
digital_signal[quant_ys >= 0] = 1

# Plotting the NRZ-L signal
# plt.figure(figsize=(8, 2.5))
plt.step(sampling_times, digital_signal, 'b', where='post')
plt.title('NRZ-L Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid(False)
plt.ylim(-0.2, 1.2)
plt.show()