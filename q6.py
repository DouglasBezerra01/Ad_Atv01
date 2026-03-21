# Verificar existência de elemento
# Dada uma lista de inteiros e um número X, verifique se X está presente na lista.
# Entrada: lista = [4, 7, 1, 9], X = 7
# Saída: verdadeiro

def verificar_existencia(entrada, x):
    for num in entrada:
        if num == x:
            return True
    return False

entrada = [4, 7, 1, 9]
x = 7
saida = verificar_existencia(entrada, x)
print(saida)
