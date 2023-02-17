import numpy as np
import matplotlib.pyplot as plt

# Define the carrier frequency and bit rate
fc = 100  # carrier frequency
br = 10   # bit rate

# Define the message signal
message = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 1])

# Define the time axis
t = np.linspace(0, len(message) / br, len(message))

# Generate the carrier signal
carrier = np.sin(2 * np.pi * fc * t)

# Generate the ASK signal
ask = np.zeros(len(message))
for i in range(len(message)):
    if message[i] == 1:
        ask[i] = carrier[i]
    else:
        ask[i] = 0

# Plot the signals
plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.title('Message signal')

plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title('Carrier signal')

plt.subplot(3, 1, 3)
plt.plot(t, ask)
plt.title('ASK signal')

plt.tight_layout()
plt.show()
