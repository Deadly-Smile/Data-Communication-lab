def __get_input_stream__(input_stream):
    number = int(input('Enter a number: '))
    number = bin(number)
    binary_number = str(number).replace('0b', '')
    for i in range(len(binary_number)):
        input_stream[8 - len(binary_number) + i] = int(binary_number[i])
    return input_stream
