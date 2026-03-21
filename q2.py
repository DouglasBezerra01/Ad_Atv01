# Contar números pares
# Dada uma lista de inteiros, retorne a quantidade de números pares presentes na lista.
# Entrada: [1, 2, 3, 4, 5, 6]
# Saída: 3

def contar_pares(entrada):
    count = 0
    for num in entrada:
        if num % 2 == 0:
            count += 1
    return count

entrada = [1, 2, 3, 4, 5, 6]
saida = contar_pares(entrada)
print(saida)
