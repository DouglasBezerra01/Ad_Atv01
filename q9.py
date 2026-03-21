# Soma dos valores positivos
# Dada uma lista de números inteiros (que pode conter valores negativos), calcule e retorne a soma apenas dos valores positivos.
# Entrada: [-1, 2, -3, 4, 5]
# Saída: 11

def soma_positivos(entrada):
    total = 0
    for num in entrada:
        if num > 0:
            total += num
    return total

entrada = [-1, 2, -3, 4, 5]
saida = soma_positivos(entrada)
print(saida)
