TEMPO = float(input("Digite o tempo da viagem: "))
VELOCIDADE = float(input("Digite a velocidade media: "))

DISTANCIA = TEMPO * VELOCIDADE
LITROS_USADOS = DISTANCIA / 12

print("Velocidade media:", VELOCIDADE)
print("Tempo gasto:", TEMPO)
print("Distancia percorrida:", DISTANCIA)
print("Litros usados:", LITROS_USADOS)
