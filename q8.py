# Contar ocorrências
# Dada uma lista de inteiros e um número X, conte e retorne quantas vezes X aparece na lista.
# Entrada: lista = [1, 2, 2, 3, 2, 4], X = 2
# Saída: 3

def contar_ocorrencias(entrada, x):
    count = 0
    for num in entrada:
        if num == x:
            count += 1
    return count

entrada = [1, 2, 2, 3, 2, 4]
x = 2
saida = contar_ocorrencias(entrada, x)
print(saida)
