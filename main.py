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


def analog_signal(a, f, t, delta):
    return a * np.sin(2 * np.pi * f * t + delta)


def phase_shifting(input_stream):
    time = np.arange(0, len(input_stream), .001)

    y = np.array([])

    size = 1000
    start = 0
    delta_1 = np.pi / 2
    delta_2 = np.pi / 4

    plt.grid()
    plt.title("Phase Shifting")
    plt.xlabel(str(input_stream))
    plt.ylim(-7, 7)
    plt.xlim(0, 9)

    for x in input_stream:
        if x == 0:
            y = np.append(y, analog_signal(a=5, f=1, t=time[start: size], delta=delta_1))
        if x == 1:
            y = np.append(y, analog_signal(a=5, f=1, t=time[start:size], delta=delta_2))

    plt.plot(time, y)
    plt.show()


def amplitude_modulation():
    time = np.linspace(0, 10, 1000)

    am = 2
    fm = 8
    pm = 0

    # message_signal = am * np.sin(2 * np.pi * fm * time + pm)
    message_signal = analog_signal(am, fm, time, pm)
    plt.title("Carry Signal", color='red')
    plt.plot(time, message_signal)
    plt.show()

    am = .1
    fm = .2
    pm = 0

    # message_signal = am * np.sin(2 * np.pi * fm * time + pm)
    carrier_signal = analog_signal(am, fm, time, pm)
    plt.title("Message Signal", color='red')
    plt.plot(time, carrier_signal)
    plt.show()

    modulated_signal = carrier_signal * message_signal

    plt.figure(figsize=(10, 6))
    plt.title("Amplitude modulation", color='red')
    plt.xlabel('Time in second')
    plt.ylabel('Amplitude')

    plt.plot(time, modulated_signal)
    plt.show()


def frequency_modulation():
    modulator_frequency = 4.0
    carrier_frequency = 40.0
    modulation_index = 1.0

    time = np.arange(44100.0) / 44100.0
    # modulator = np.sin(2.0 * np.pi * modulator_frequency * time) * modulation_index
    # carrier = np.sin(2.0 * np.pi * carrier_frequency * time)
    modulator = analog_signal(modulation_index, modulator_frequency, time, 0)
    carrier = analog_signal(1, carrier_frequency, time, 0)

    product = np.zeros_like(modulator)

    for i, t in enumerate(time):
        product[i] = np.sin(2. * np.pi * (carrier_frequency * t + modulator[i]))

    plt.subplot(3, 1, 1)
    plt.title('Frequency Modulation')
    plt.plot(modulator)
    plt.ylabel('Amplitude')
    plt.xlabel('Modulator signal')
    plt.subplot(3, 1, 2)
    plt.plot(carrier)
    plt.ylabel('Amplitude')
    plt.xlabel('Carrier signal')
    plt.subplot(3, 1, 3)
    plt.plot(product)
    plt.ylabel('Amplitude')
    plt.xlabel('Output signal')
    plt.show()


def phase_modulation():
    fs = 8000
    fc = 100
    ac = 1
    fm = 5
    am = 1
    kp = 20

    t = np.arange(0, 1, 1 / fs)
    # message_signal = am * cos(2 * pi * fm * t)  # Message Signal
    # carrier_signal = ac * cos(2 * pi * fc * t)  # Carrier Signal
    message_signal = analog_signal(am, fm, t, 0)
    carrier_signal = analog_signal(ac, fc, t, 0)

    s_PM = []
    for (ti, m) in zip(t, message_signal):
        # s_PM.append(ac * cos(2 * pi * fc * ti + kp * m))
        s_PM.append(analog_signal(ac, fc, ti + kp * m, 0))

    fig, axs = plt.subplots(3, 1)
    axs[0].plot(t, message_signal)
    axs[0].set(ylabel='m(t)')
    axs[0].set_title('Message Signal')
    axs[1].plot(t, carrier_signal)
    axs[1].set(ylabel='c(t)')
    axs[1].set_title('Carrier Signal')
    axs[2].plot(t, s_PM, t, message_signal)
    axs[2].set(ylabel='s_{PM}(t)')
    axs[2].set_title('PM Signal')
    plt.show()


def __get_input_number__(input_stream):
    input_data = input("Enter number : ")
    input_data = bin(int(input_data))
    binary_stream = str(input_data).replace('0b', '')
    for i in range(len(binary_stream)):
        input_stream[8 - len(binary_stream) + i] = int(binary_stream[i])


# --- main code ---
data = [0, 0, 0, 0, 0, 0, 0, 0]
# __get_input_number__(data)
# print("Data in binary format: ", data)

# __nrzl_nrzi__(data)
# phase_shifting(data)
# amplitude_modulation()
frequency_modulation()
phase_modulation()
