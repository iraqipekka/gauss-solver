import numpy as np 

def a_matrix(rows, col):

    matrix = []
    print("Input A matrix row entries: ")

    for _ in range(rows):

        row = []

        for _ in range(col):
            row.append(int(input()))
        matrix.append(row)


    print("Matrix is: ")

    for i in range(rows):
        for j in range(col):
            print(matrix[i][j], end="")
        print()

    return np.array(matrix)

def y_matrix(rows):

    cols = 1

    y_matrix = []
    print("Input Y matrix row entries: ")

    for _ in range(rows):
        y_matrix.append(int(input()))

    print("Y is: ")

    for i in range(rows):
        print(y_matrix[i], end="")
        print()
    
    return np.array(y_matrix)

def solve_sys(A, y):


    try:
        solution = np.linalg.solve(A, y)
    except:
        return "Invalid system"
    else: 
        print("Solution is: ")
        return solution

    



