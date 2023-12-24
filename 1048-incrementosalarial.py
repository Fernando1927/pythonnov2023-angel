salario_actual = float(input())

if salario_actual <=400:
    porcentaje_ganancia = 15

elif salario_actual <=800:
    porcentaje_ganancia = 12
    
elif salario_actual <=1200:
    porcentaje_ganancia = 10
    
elif salario_actual <=2000:
    porcentaje_ganancia = 7
    
else:
    porcentaje_ganancia = 4
    
ganancia = (salario_actual *porcentaje_ganancia)/100
nuevo_salario = (salario_actual + ganancia)


print(f"Novo salario: {nuevo_salario:.2f}")
print(f"Reajuste ganho: {ganancia:.2f}")
print(f"Em percentual: {porcentaje_ganancia}%")