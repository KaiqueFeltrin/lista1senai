nome_funcionario = input("Digite o nome do funcionário: ")
salario_antigo = float(input("Digite o salário antigo do funcionário: "))

if salario_antigo <= 1500:
    aumento = salario_antigo * 0.1
else:
    aumento = salario_antigo * 0.05

salario_novo = salario_antigo + aumento

print("Novo salário de", nome_funcionario, "é R$", salario_novo)
print("A diferença entre o salário antigo e o novo é de R$", salario_novo - salario_antigo)