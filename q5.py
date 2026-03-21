# Soma dos pares
# Dada uma lista de inteiros, calcule e retorne a soma apenas dos números pares.
# Entrada: [1, 2, 3, 4, 5, 6]
# Saída: 12

def soma_pares(entrada):
    total = 0
    for num in entrada:
        if num % 2 == 0:
            total += num
    return total

entrada = [1, 2, 3, 4, 5, 6]
saida = soma_pares(entrada)
print(saida)
