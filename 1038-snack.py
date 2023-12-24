codigo, cantidad = input().split()

codigo = int (codigo)
cantidad = int (cantidad)

if (codigo ==1):
    final = (cantidad *4)
    
elif (codigo ==2):
    final = (cantidad *4.5)

elif (codigo ==3):
    final = (cantidad *5)

elif (codigo ==4):
    final = (cantidad *2)
    
elif (codigo ==5):
    final = (cantidad *1.5)
    
print("Total: R$ %.2f" %final)
