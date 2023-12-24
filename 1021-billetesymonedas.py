
billetes, monedas = map(int, input().split('.'))
monedas = (monedas + (billetes*100))

valores = [100, 50, 20, 10, 5, 2]

print("NOTAS:")

for valor in valores:
    print(f"{monedas//(valor*100)} nota(s) de R$ {valor}.00")
    monedas = monedas%(valor*100)
    
moedas = [100, 50, 25, 10, 5, 1]

print("MOEDAS:")

for moeda in moedas:
    print(f"{monedas//moeda} moeda (s) de R$ {moeda//100}.{moeda%100:02}")
    monedas = monedas%moeda


