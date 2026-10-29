A = int(input("Votos do candidato A: "))
B = int(input("Votos do candidato B: "))
C = int(input("Votos do candidato C: "))
NULOS = int(input("Votos nulos: "))
BRANCOS = int(input("Votos em branco: "))

TOTAL = A + B + C + NULOS + BRANCOS

VALIDOS = A + B + C

print("Total de eleitores:", TOTAL)
print("Votos validos:", VALIDOS / TOTAL * 100, "%")
print("Candidato A:", A / TOTAL * 100, "%")
print("Candidato B:", B / TOTAL * 100, "%")
print("Candidato C:", C / TOTAL * 100, "%")
print("Votos nulos:", NULOS / TOTAL * 100, "%")
print("Votos em branco:", BRANCOS / TOTAL * 100, "%")
