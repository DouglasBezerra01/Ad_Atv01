# Contar elementos maiores que um valor
# Dada uma lista de inteiros e um número X, retorne quantos elementos da lista são estritamente maiores que X.
# Entrada: lista = [1, 5, 8, 2, 10], X = 5
# Saída: 2

def contar_maiores(lista, x):
    count = 0
    for num in lista:
        if num > x:
            count += 1
    return count

entrada = [1, 5, 8, 2, 10]
x = 5
saida = contar_maiores(entrada, x)
print(saida)
