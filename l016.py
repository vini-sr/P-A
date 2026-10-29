SM = float(input("Digite o salario atual: "))
PR = float(input("Digite o percentual de reajuste: "))

NS = SM + (SM * PR / 100)

print("Novo salario:", NS)
