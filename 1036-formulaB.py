#Resolucion de la formula Bhaskara

V1,V2, V3 = list(map(float,input().split()))
Resultado = V2 * V2 - 4 * V1 * V3
Raiz = pow(Resultado, .5)

if ( Resultado < 0 or V1 == 0):
    print("Impossivel calcular")
    
else:
    Resultado2 = (-V2 + Raiz) / (2 * V1)
    Resultado3 = (-V2 - Raiz) / (2 * V1)
    print("R1 = %.5lf"%Resultado2)
    print("R2 = %.5lf"%Resultado3)
