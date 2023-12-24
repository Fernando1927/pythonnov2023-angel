a,b,c=list(map(float,input().split()))
a = float(a)
b = float(b)
c = float(c)


if (a>=b and a>=c):
    a_1 = a
    b_1 = b
    c_1 = c

if (b>=a and b>=c):
    a_1 = b
    b_1 = a
    c_1 = c
    
if (c>=a and c>=b):
    a_1 = c
    b_1 = a
    c_1 = b
    

if(a_1>=(b_1+c_1)):
    print("NAO FORMA TRIANGULO")
    
elif(a_1*a_1 == (b_1*b_1+c_1*c_1)):
    print("TRIANGULO RETANGULO")
    
elif(a_1*a_1>(b_1*b_1+c_1*c_1)):
    print("TRIANGULO OBTUSANGULO")

elif(a_1*a_1<(b_1*b_1+c_1*c_1)):
    print("TRIANGULO ACUTANGULO")
    
if (a_1==b_1 and b_1==c_1):
    print("TRIANGULO EQUILATERO")
elif(a_1==b_1 or b_1==c_1):
    print("TRIANGULO ISOSCELES")
    