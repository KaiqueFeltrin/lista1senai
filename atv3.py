num = int(input("Digite um número inteiro: "))

if num <= 1:
    print("O número não é primo")

for i in range(2, num//2+1):
    if num % i == 0:
        print("O número não é primo")
        break

else:
    print("O número é primo")