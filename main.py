import matplotlib.pyplot as plt
import numpy as np


def __nrzl_nrzi__(input_steam):
    # getting datas for NRZ-L
    data_nrz = []
    for i in input_steam:
        if i == 1:
            x = 1
        else:
            x = -1
        data_nrz.append(x)
    data_nrz.append(1)

    # getting datas for NRZ-I
    data_nrz_i = []
    temp = True
    for i in range(len(input_steam)):
        x = None
        if input_steam[i] == 1 and temp == True:
            x = -1
            temp = False
        elif input_steam[i] == 1 and temp == False:
            x = 1
            temp = True
        elif input_steam[i] == 0 and temp == False:
            x = -1
        elif input_steam[i] == 0 and temp == True:
            x = 1
        x += 3
        data_nrz_i.append(x)
    if data_nrz_i[0] == 0:
        data_nrz_i[0] = 1 + 3
    data_nrz_i.append(1 + 3)

    xs = np.repeat(range(len(data_nrz)), 2)
    ys = np.repeat(data_nrz, 2)
    # print(xs[1:])
    # print(ys[:-1])

    # NRZ-L co-ordinates
    xs = xs[1:]
    ys = ys[:-1]

    # ------ Initializing in graph -------
    plt.grid()
    plt.title("NRZ-L(Blue), NRZ-I(Orange)")
    plt.xlabel(str(input_steam))
    plt.ylim(-2, 7)
    plt.xlim(0, 9)

    # plotting in graph NRZ-L
    plt.plot(xs, ys)

    xs = np.repeat(range(len(data_nrz_i)), 2)
    ys = np.repeat(data_nrz_i, 2)

    # NRZ-I co-ordinates
    xs = xs[1:]
    ys = ys[:-1]

    # plotting in graph NRZ-I
    plt.plot(xs, ys)
    plt.show()


def __get_input_number__(input_stream):
    input_data = input("Enter number : ")
    input_data = bin(int(input_data))
    binary_stream = str(input_data).replace('0b', '')
    for i in range(len(binary_stream)):
        input_stream[8 - len(binary_stream) + i] = int(binary_stream[i])


# @@@@@@@@@@@@@@@@@@@@ function call @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
data = [0, 0, 0, 0, 0, 0, 0, 0]
__get_input_number__(data)
print("Data in binary format: ", data)

__nrzl_nrzi__(data)
