entra = 0
sale = 0

for i in range(int(input())):
    x = int(input())
    if x>=10 and x<=20:
        entra += 1
    else:
        sale += 1
print(f"{entra} in") 
print(f"{sale} out")

