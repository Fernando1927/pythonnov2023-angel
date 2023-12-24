
impares=0
pares =0
positivo=0
negativo=0


for valor_par in range(1,6):
    ing = float(input())
    if ing%2==0:
        pares = pares+1
    else:
        impares = impares+1
    if ing>0:
        positivo = positivo + 1
    elif ing<0:
        negativo=negativo + 1
    
    
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")