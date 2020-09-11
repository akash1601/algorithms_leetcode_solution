M = 3
N = 3
matrix = [[12, 23, 34], 
          [45, 56, 67],  
          [78, 89, 91]] 
  
# function to rotate 
# matrix by k times 
def rotateMatrix(k) : 
  
    global M, N, matrix 
      
    # temporary array  
    # of size M 
    temp = [0] * M 
      
    # within the size 
    # of matrix 
    k = k % M 
      
    for i in range(0, N) :  
      
        # copy first M-k elements 
        # to temporary array 
        for t in range(0, M - k) : 
            temp[t] = matrix[i][t] 
      
        # copy the elements from  
        # k to end to starting 
        for j in range(M - k, M) : 
            matrix[i][j - M + k] = matrix[i][j] 
      
        # copy elements from  
        # temporary array to end 
        for j in range(k, M) : 
            matrix[i][j] = temp[j - k] 
      
# function to display 
# the matrix 
def displayMatrix() : 
  
    global M, N, matrix 
    for i in range(0, N) : 
      
        for j in range(0, M) : 
            print ("{} " .  
                   format(matrix[i][j]), end = "") 
        print () 
  
# Driver code 
k = 2
  
# rotate matrix by k 
rotateMatrix(k) 
  
# display rotated matrix 
displayMatrix() 
  