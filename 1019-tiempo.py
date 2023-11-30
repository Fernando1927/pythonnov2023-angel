


tiempo = int(input())


#Definir las horas
horas = tiempo//(60*60)
tiempo = tiempo%(60*60)

#definición de los minutos
minutos = tiempo//(60)
tiempo = tiempo%(60)

print(f"{horas}:{minutos}:{tiempo}")

