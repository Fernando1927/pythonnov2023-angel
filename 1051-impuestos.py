ingreso = float(input())

if ingreso >=0 and ingreso <= 2000:
    print("Isento")
elif ingreso>= 2000.01 and ingreso<=3000:
    ingreso = ingreso - 2000
    pago = ingreso*0.08
    print(f"R$ {pago:.2f}")
    
elif ingreso>= 3000.01 and ingreso<=4500.00:
    ingreso = ingreso - 3000
    pago = (ingreso*0.18)+80
    print(f"R$ {pago:.2f}")

elif ingreso > 4500.00:
    ingreso = ingreso - 4500
    pago = (ingreso*0.28)+350
    print(f"R$ {pago:.2f}")
