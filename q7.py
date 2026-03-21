# Inverter lista
# Dada uma lista de inteiros, crie e retorne uma nova lista com os elementos em ordem inversa.
# Não utilize funções prontas de inversão da linguagem.
# Entrada: [1, 2, 3, 4]
# Saída: [4, 3, 2, 1]

def inverter_lista(entrada):
    resultado = []
    for i in range(len(entrada) - 1, -1, -1):
        resultado.append(entrada[i])
    return resultado

entrada = [1, 2, 3, 4]
saida = inverter_lista(entrada)
print(saida)
