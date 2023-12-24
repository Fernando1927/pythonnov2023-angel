A,B,C,D = input().split()
A = float(A)
B = float(B)
C = float(C)
D = float(D)

promedio = ((A*2) + (B*3) + (C*4) + (D*1))/(10)

print("Media: %.1f"%promedio)

if promedio >= 7.0:
    print("Aluno aprovado.")
elif promedio <5:
    print("Aluno reprovado.")
elif promedio >= 5 and promedio <7:
    print("Aluno em exame.")
    E = float(input())
    print("Nota do exame: %.1f" %E)
    nuevo_promedio = (promedio+E)/2
    if nuevo_promedio >=5.0:
        print("Aluno aprovado.")
    else: 
        print("Aluno reprovado.")
    
    print("Media final: %.1f"%nuevo_promedio)