# Contar vogais
# Dada uma string s, conte e retorne quantas vogais ela contém.
# Considere as vogais: a, e, i, o, u (maiúsculas e minúsculas).
# Entrada: s = "Programacao"
# Saída: 5

def contar_vogais(s):
    vogais = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vogais:
            count += 1
    return count

s = "Programacao"
saida = contar_vogais(s)
print(saida)
