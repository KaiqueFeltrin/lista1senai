numero = int(input("Digite um número inteiro: "))

numero_str = str(numero)

soma = 0

for digito in numero_str:
    soma += int(digito) ** 3
a
if soma == numero:
    print(numero, "é um número de Armstrong!")
else:
    print(numero, "não é um número de Armstrong.")