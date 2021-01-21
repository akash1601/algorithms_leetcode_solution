def zeroMatrix(matrix):
    a = set()
    b = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                a.add(i)
                b.add(j)
    for i in a:
        matrix[i] = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in b:
            matrix[i][j] = 0
    return matrix
            
zeroMatrix([[1,1,1,0],[5,0,1,1],[6,1,1,1],[7,0,1,0],[1,1,1,1]])