import numpy as np
import matplotlib.pyplot as plt


def __differential_manchester_version__(input_steam):
    y = list()
    if input_steam[0] == '0':
        y.append(-1)
        y.append(1)
    else:
        y.append(1)
        y.append(-1)
    for i in range(1, len(input_steam)):
        if input_steam[i] is '1':
            y.append(y[-1])
            y.append(-1 * y[-2])
        else:
            y.append(-1 * y[-1])
            y.append(y[-2])

    xs = np.repeat(range(len(y)), 2)
    ys = np.repeat(y, 2)
    xs = xs[1:]
    ys = ys[:-1]
    # For  representation
    plt.title('Differential Manchester')
    plt.plot(xs, ys)
    plt.ylabel('Amplitude')
    plt.xlabel('Time')
    plt.show()


data = input('Enter Binary Message: ')
__differential_manchester_version__(data)
print('data in binary : ', data)
