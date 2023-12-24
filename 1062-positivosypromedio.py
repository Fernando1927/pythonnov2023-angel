x = 0
s = 0


print("Ingrese 6 números entre positivos y negativos")

for valores in range (1,7):
    y = float(input())
    if y>0:
        s = s+y
        x = x+1

print("Aqui estan tus resultados")
print(f"{x} valores positivos")
print(f"{s/x:.1f}")