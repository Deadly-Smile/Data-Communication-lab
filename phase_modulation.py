import numpy as np
import matplotlib.pyplot as plt

# time axis
ts = np.arange(0, 1, 1 / 1000)

# carrier signal
fc = 100
carrier = np.sin(2 * np.pi * fc * ts)

# modulation signal
fm = 2
modulation = np.sin(2 * np.pi * fm * ts)

# phase-modulated signal
phase_modulated = np.sin(2 * np.pi * fc * ts + np.pi * modulation)

# Plot the signals
plt.subplot(3, 1, 1)
plt.plot(ts, carrier)
plt.title('Carrier signal')

plt.subplot(3, 1, 2)
plt.plot(ts, modulation)
plt.title('Modulation signal')

plt.subplot(3, 1, 3)
plt.plot(ts, phase_modulated)
plt.title('Phase-modulated signal')

plt.tight_layout()
plt.show()
