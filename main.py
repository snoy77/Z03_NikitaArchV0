# constant -------------
VERSION = '0.001 AT 03.05.2023'

print('/////// NekitArch V' + VERSION + "/////////\n")

Methods = ['Кодирование длин серий (без модификации)']


def count_bytes(INPUT_DATA, OUTPUT_DATA):
    print("Выходное сообщение \"" + OUTPUT_DATA + "\"")
    print("Размер входного сообщения (количество = виртуальные байты): " + str(len(INPUT_DATA)))
    print("Размер выходного сообщения (количество = виртуальные байты): " + str(len(OUTPUT_DATA)))
def Methods_1():
    print("\n========== Кодирование длин серий (без модификации) ==========\n")
    while True:

        INPUT_DATA = input("Введите строку для сжатия: ")
        INPUT_DATA_len = len(INPUT_DATA)

        input_bytes = INPUT_DATA.encode('utf-8')

        if INPUT_DATA == '-0-':
            break

        OUTPUT_DATA = ''
        fc = INPUT_DATA[0] #forst char
        nc = '' #next char
        countC = 1 #count char
        for i in range(1, INPUT_DATA_len):
            nc = INPUT_DATA[i]

            if fc == nc:
                countC = countC + 1
            else:
                OUTPUT_DATA = OUTPUT_DATA + str(countC) + fc
                fc = nc
                countC = 1
        #печатаем последний символ
        OUTPUT_DATA = OUTPUT_DATA + str(countC) + fc
        print()
        count_bytes(INPUT_DATA, OUTPUT_DATA)
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
