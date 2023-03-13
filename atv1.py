num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Digite sua escolha (1,2,3,4): "))

if op == 1:
    print("Resultado da soma:", num1 + num2)
elif op == 2:
    print("Resultado da subtração:", num1 - num2)
elif op == 3:
    print("Resultado da multiplicação:", num1 * num2)
elif op == 4:
    if num2 == 0:
        print("Erro: não é possível dividir por zero")
    else:
        print("Resultado da divisão:", num1 / num2)
else:
    print("Erro: escolha uma operação válida (1,2,3,4)")