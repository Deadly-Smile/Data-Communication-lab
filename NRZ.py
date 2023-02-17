import matplotlib.pyplot as plt
import numpy as np


def __print_nrzl__(input_stream):
    data_narl = []
    for i in range(len(input_stream)):
        if input_stream[i] == '1':
            x = 1
        else:
            x = -1
        data_narl.append(x)
    xs = np.repeat(range(len(data_narl)), 2)
    ys = np.repeat(data_narl, 2)
    xs = xs[1:]
    ys = ys[:-1]

    plt.subplot(3, 1, 1)
    plt.title('NRZ-L')
    plt.plot(xs, ys)
    plt.ylabel('Amplitude')
    plt.xlabel('Time')


def __print_nrzi__(input_stream):
    data_nrji = []
    is_hight = True
    for i in range(len(input_stream)):
        x = None
        if input_stream[i] == '1' and is_hight == True:
            x = -1
            is_hight = False
        elif input_stream[i] == '1' and is_hight == False:
            x = 1
            is_hight = True
        elif input_stream[i] == '0' and is_hight == True:
            x = 1
        elif input_stream[i] == '0' and is_hight == False:
            x = -1
        data_nrji.append(x)

    xs = np.repeat(range(len(data_nrji)), 2)
    ys = np.repeat(data_nrji, 2)
    xs = xs[1:]
    ys = ys[:-1]

    plt.subplot(3, 1, 3)
    plt.title('NRZ-I')
    plt.plot(xs, ys)
    plt.ylabel('Amplitude')
    plt.xlabel('Time')


data = input('Enter Binary Message: ')
__print_nrzl__(data)
__print_nrzi__(data)
plt.show()
print('data in binary : ', data)
