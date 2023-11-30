

from math import sqrt


operaciones = input() .split()
Y1 = float(operaciones[0])
X1 = float(operaciones[1])
operaciones2 = input() .split()
Y2 = float(operaciones2[0])
X2 = float(operaciones2[1])

x = sqrt(((X2 - X1)*(X2 - X1))+((Y2 - Y1)*(Y2 - Y1)))
u = x
print(f"{u:.4f}")
