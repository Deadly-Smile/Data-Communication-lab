import matplotlib.pyplot as plt
import numpy as np


def __print_rz__(input_stream):
    data_rz = []
    for i in range(len(input_stream)):
        if input_stream[i] == '1':
            x = 1
        else:
            x = 0
        data_rz.append(x)
    xs = np.repeat(range(len(data_rz)), 2)
    ys = np.repeat(data_rz, 2)
    xs = xs[1:]
    ys = ys[:-1]

    plt.plot(xs, ys)
    plt.title('RZ')
    plt.ylabel('Amplitude')
    plt.xlabel('Time')


data = input('Enter Binary Message: ')
__print_rz__(data)
plt.show()
print('data in binary : ', data)
