import random
import os
import getpass
import numpy as np

# fungsi untuk penjumlahan matriks
def add(x, y):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] + y[i][j]

    for r in result:
        print(r)

# fungsi untuk pengurangan matriks
def sub(x, y):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] - y[i][j]

    for r in result:
        print(r)

# fungsi untuk perkalian matriks
def mul(x, y, row_1, col_1, row_2, col_2):
    if (col_1 != row_2):
        print('Tidak bisa dikali')
        return

    result = [[0 for x in range(col_2)] for y in range(row_1)]

    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]
              
    for r in result:
        print(r)

# fungsi untuk pembagian matriks
def divided(x, y):
    A = np.array(y)
    y = np.linalg.inv(A)

    mul(x, y, len(x), len(x[0]), len(y), len(y[0]))

row_matrix_1 = int(input('Input row for matrix 1: '))
column_matrix_1 = int(input('Input column for matrix 1: '))
row_matrix_2 = int(input('Input row for matrix 2: '))
column_matrix_2 = int(input('Input column for matrix 2: '))

# inisialisasi matrix 1
matrix_1 = [[random.randint(-10, 10) for x in range(
    column_matrix_1)] for y in range(row_matrix_1)]

# inisialisasi matrix 2
matrix_2 = [[random.randint(-10, 10) for x in range(
    column_matrix_2)] for y in range(row_matrix_2)]

while True:
    os.system('cls')
    print('Matrix 1:')
    for r in matrix_1:
        print(r)

    print('\n')

    print('Matrix 2:')
    for r in matrix_2:
        print(r)

    print('\n\n')
    print('Apa operasi yang ingin dilakukan?')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    print('9. exit')

    opsi = int(input('input: '))
    if opsi == 1:
        print('\nM1 + M2\n')
        add(matrix_1, matrix_2)
    elif opsi == 2:
        print('\nM1 - M2\n')
        sub(matrix_1, matrix_2)
    elif opsi == 3:
        print('\nM1 * M2\n')
        mul(matrix_1, matrix_2, row_matrix_1, column_matrix_1, row_matrix_2, column_matrix_2)
    elif opsi == 4:
        print('\nM1 * (M2)\'\n')
        divided(matrix_1, matrix_2)
    elif opsi == 9:
        exit()
    else:
        print('minimal baca opsi')
    getpass.getpass(prompt='Press any key to continue...')
