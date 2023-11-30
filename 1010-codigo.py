valor_1 = input() .split()
a = int(valor_1[0])
b = int(valor_1[1])
d = float(valor_1[2])
suma_1 = (b*d)

valor_2 = input() .split()
e = int(valor_2[0])
f = int(valor_2[1])
h = float(valor_2[2])
suma_2 = (f*h)

suma_3 = suma_1 + suma_2

print(f"VALOR A PAGAR: R$ {suma_3:.2f}")
