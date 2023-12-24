valor_1 = int(input())
valor_2 = int(input())

sum_valores = 0

for i in range(valor_2+1, valor_1):
    if i%2 !=0:
        sum_valores +=i

print(sum_valores)