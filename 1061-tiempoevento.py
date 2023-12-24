dia, fecha1 = input().split()
fecha1 = int(fecha1)
a,b,c = map(int, input().split(':'))

dia, fecha2 = input().split()
fecha2 = int(fecha2)
x,y,z = map(int, input().split(':'))

j = z-c
k = y-b
l = x-a
m = fecha2-fecha1

if(j<0):
    j+=60
    k-=1

if(k<0):
    k+=60
    l-=1

if(l<0):
    l+=24
    m-=1
    
print(f"{m} dia(s)")
print(f"{l} hora(s)")
print(f"{k} minuto(s)")
print(f"{j} segundo(s)")