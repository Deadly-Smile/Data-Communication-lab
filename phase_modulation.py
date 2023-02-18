import numpy as np
import matplotlib.pyplot as plt

# Generate carrier signal
ac=2
fc = 100 # Carrier frequency
fs = 200 # Sampling frequency
t = np.linspace(0, 0.1, fs, endpoint=False)
carrier = ac*np.sin(2 * np.pi * fc * t)

# Generate modulating signal
am = 10
fm = 50  # Modulating frequency
modulator = am*np.sin(2 * np.pi * fm * t)

# Phase modulation
k = .5  # Modulation index
phase_modulated = np.sin(2 * np.pi * fc * t + k * modulator)

# Plot signals
fig, axs = plt.subplots(3)

axs[0].plot(t, carrier)
axs[0].set_title("Carrier Signal")

axs[1].plot(t, modulator)
axs[1].set_title("Modulating Signal")

axs[2].plot(t, phase_modulated)
axs[2].set_title("Phase Modulated Signal")

plt.tight_layout()
plt.show()