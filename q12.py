# Contar caracteres
# Dada uma string s, retorne o número de caracteres que ela possui.
# Se possível, implemente sem usar funções prontas de comprimento da linguagem.
# Entrada: s = "teste"
# Saída: 5

def contar_caracteres(s):
    count = 0
    for char in s:
        count += 1
    return count

s = "teste"
saida = contar_caracteres(s)
print(saida)
