pares =0



for valor_par in range(1,6):
    ing = float(input())
    if ing%2==0:
        pares = pares+1
print(f"{pares} valores pares")