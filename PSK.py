import numpy as np
import matplotlib.pyplot as plt


def __psk__(input_stream):
    am = 5
    f = 1

    y = np.array([])
    time = np.array([])
    start = 0
    for x in data:

        t_time = np.arange(start, start + 2, 0.001)
        if x == '0':
            t_y = am * np.sin(2 * np.pi * f * t_time)
        else:
            t_y = am * np.sin(2 * np.pi * f * t_time * (-1))
        y = np.append(y, t_y)
        time = np.append(time, t_time)
        start = start + 2
    plt.grid()
    plt.title('PSK')
    plt.ylabel('Amplitude')
    plt.xlabel('Time')
    plt.plot(time, y)
    plt.show()


data = input('Enter Binary Message: ')
__psk__(data)
print('data in binary : ', data)
