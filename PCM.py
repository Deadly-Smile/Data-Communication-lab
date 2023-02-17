import numpy as np

freq = 100 # signal frequency in Hz
duration = 1 # signal duration in seconds
sample_rate = 44100 # sample rate in Hz
t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
signal = np.sin(2 * np.pi * freq * t)

# Quantize the signal
quantized_signal = np.round(signal * 127 + 127)

# Convert the quantized signal to binary
binary_signal = np.unpackbits(quantized_signal.astype(np.uint8))

# Print the binary signal
print(binary_signal)
