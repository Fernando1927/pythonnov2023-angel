
x = 0

print("Ingrese 6 números entre positivos y negativos")

for valores in range (1,7):
    y = float(input())
    if y>0:
        x = x+1


print(f"{x} valores positivos")