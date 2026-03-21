# Maior número
# Dada uma lista de números inteiros, retorne o maior valor presente na lista.
# Entrada: [3, 7, 2, 9, 5]
# Saída: 9

def maior_numero(lista):
    if not lista:
        return None
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

entrada = [3, 7, 2, 9, 5]
saida = maior_numero(entrada)
print(saida)
