operaciones = input() .split()
A = float(operaciones[0])
B = float(operaciones[1])
C = float(operaciones[2])
pi = 3.14159


TRIANGULO = (A*C)/2
CIRCULO = pi*C*C
TRAPEZIO = ((A + B)/(2))*C
QUADRADO = B * B
RETANGULO = A * B

print(f"TRIANGULO: {TRIANGULO:.3f}") 
print(f"CIRCULO: {CIRCULO:.3f}") 
print(f"TRAPEZIO: {TRAPEZIO:.3f}") 
print(f"QUADRADO: {QUADRADO:.3f}") 
print(f"RETANGULO: {RETANGULO:.3f}") 
