# Produto dos elementos
# Dada uma lista de números inteiros, calcule e retorne o produto de todos os elementos.
# Entrada: [1, 2, 3, 4]
# Saída: 24

def produto_elementos(entrada):
    resultado = 1
    for num in entrada:
        resultado *= num
    return resultado

entrada = [1, 2, 3, 4]
saida = produto_elementos(entrada)
print(saida)
