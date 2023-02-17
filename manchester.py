import numpy as np
import matplotlib.pyplot as plt


def __manchester_version__(input_steam):
    y = list()
    for bit in input_steam:
        if bit is '1':
            y.append(-1)
            y.append(1)
        else:
            y.append(1)
            y.append(-1)

    xs = np.repeat(range(len(y)), 2)
    ys = np.repeat(y, 2)
    xs = xs[1:]
    ys = ys[:-1]
    # For  representation
    plt.title('Manchester')
    plt.plot(xs, ys)
    plt.ylabel('Amplitude')
    plt.xlabel('Time')
    plt.show()


data = input('Enter Binary Message: ')
__manchester_version__(data)
print('data in binary : ', data)
