#Insertar el valor del billete

billetes = int(input())
print(billetes)

#Contador


valor_1 = billetes//100
billetes = billetes%100

valor_2 = billetes//50
billetes = billetes%50

valor_3 = billetes//20
billetes = billetes%20

valor_4 = billetes//10
billetes = billetes%10

valor_5 = billetes//5
billetes = billetes%5

valor_6 = billetes//2
billetes = billetes%2

valor_7 = billetes//1
billetes = billetes%1

print(f"{valor_1} nota(s) de R$ 100,00")
print(f"{valor_2} nota(s) de R$ 50,00")
print(f"{valor_3} nota(s) de R$ 20,00")
print(f"{valor_4} nota(s) de R$ 10,00")
print(f"{valor_5} nota(s) de R$ 5,00")
print(f"{valor_6} nota(s) de R$ 2,00")
print(f"{valor_7} nota(s) de R$ 1,00")
