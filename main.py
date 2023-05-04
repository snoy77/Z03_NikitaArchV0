# constant -------------
VERSION = '0.001 AT 03.05.2023'

print('/////// NekitArch V' + VERSION + "/////////\n")

Methods = ['Кодирование длин серий (без модификации)']


def count_bytes(INPUT_BYTES, OUTPUT_BYTES):
    print("Входное сообщение в виде байтов:")
    print(INPUT_BYTES)
    print("Размер: " + str(len(INPUT_BYTES)) + " byte")
    print("\n")

    print("Выходное сообщение в виде байтов:")
    print(OUTPUT_BYTES)
    print("Размер: " + str(len(OUTPUT_BYTES)) + " byte")
    print("\n")
def Methods_1():
    print("\n========== Кодирование длин серий (без модификации) ==========\n")
    while True:
        INPUT_DATA = input("Введите строку для сжатия: ")
        if INPUT_DATA == '-0-':
            break

        #INPUT_DATA_len = len(INPUT_DATA)
        INPUT_BYTES = INPUT_DATA.encode('utf-8')
        INPUT_BYTES_LEN = len(INPUT_BYTES)

        OUTPUT_BYTES = bytearray(0)

        fc = INPUT_BYTES[0] #forst byte
        nc = ''             #next byte
        countC = 1          #count bytes

        #for i in range(1, INPUT_DATA_len):
        for i in range(1, INPUT_BYTES_LEN):
            nc = INPUT_BYTES[i]

            if fc == nc:
                countC = countC + 1
            else:
                #OUTPUT_DATA = OUTPUT_DATA + str(countC) + fc
                OUTPUT_BYTES.append(countC)
                OUTPUT_BYTES.append(fc)
                fc = nc
                countC = 1
        #печатаем последний символ
        #OUTPUT_DATA = OUTPUT_DATA + str(countC) + fc
        OUTPUT_BYTES.append(countC)
        OUTPUT_BYTES.append(fc)
        count_bytes(INPUT_BYTES, OUTPUT_BYTES)
        #count_bytes(INPUT_DATA, OUTPUT_DATA)
    print("\n===============================================================\n")

while True:
    print("Выберите метод сжатия:")
    i = 1
    for methods in Methods:
        print(str(i) + '. ' + methods)

    _I = input("\nВаш выбор: ")

    if _I == '1':
        Methods_1()
    input('Конец главной иттерации')
