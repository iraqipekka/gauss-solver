import numpy as np
import function as fn

print("A matrix: ")
rows = int(input("Amount of rows: "))
cols = int(input("Amount of columns: "))
print(f"A matrix will be a {cols}x{rows}")

print("Y matrix: ")
y_rows = int(input("Amount of rows: "))
print(f"Y matrix will be a 1x{y_rows}")

print(fn.solve_sys(fn.a_matrix(rows, cols), fn.y_matrix(y_rows)))


