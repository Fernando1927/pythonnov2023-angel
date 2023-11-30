

edad = int(input())

#Definir los años
años = edad//365
edad = edad%365

#definición de los meses
mes = edad//30
edad = edad%30

print(f"{años} ano(s)")
print(f"{mes} mes(es)")
print(f"{edad} dia(s)")


