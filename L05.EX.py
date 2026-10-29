VALOR = float(input("Digite o valor da prestacao: "))
TAXA = float(input("Digite a taxa de juros: "))
TEMPO = float(input("Digite o tempo de atraso: "))

PRESTACAO = VALOR + (VALOR * TAXA / 100) * TEMPO

print("Valor da prestacao:", PRESTACAO)
