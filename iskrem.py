w, h= 4 , 4;
matrix = [[0 for x in range (w)] for y in range (h)]
matrix = [[4,2,8,9],[317,828,332,461],[274,932,154,354],[232,644,656,998]]

for k in range(w):
    for n in range(h):
        if (matrix[k][n] % 2) ==0:
            print(matrix[k][n])
            print(' er et partition\n')


print('\n'.join ([''.join(['{:4}'.format(item) for item in row])
    for row in matrix]))