import numpy as np
import matplotlib.pyplot as plt


def __ask__(input_message):
    low_amplitude = 1
    high_amplitude = 3
    f = 1
    y = np.array([])
    time = np.array([])
    start = 0
    for x in input_message:
        t_time = np.arange(start, start + 2, 0.001)
        if x == '0':
            ty = low_amplitude * np.sin(2 * np.pi * f * t_time)
        else:
            ty = high_amplitude * np.sin(2 * np.pi * f * t_time)
        y = np.append(y, ty)
        time = np.append(time, t_time)
        start = start + 2
    plt.grid()
    plt.title('ASK')
    plt.ylabel('Amplitude')
    plt.xlabel('Time')
    plt.plot(time, y)
    plt.show()


data = input('Enter Binary Message: ')
__ask__(data)
print('data in binary : ', data)
