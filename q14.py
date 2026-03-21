# Contar ocorrências de um caractere
# Dada uma string s e um caractere c, conte e retorne quantas vezes c aparece em s.
# Entrada: s = "banana", c = 'a'
# Saída: 3

def contar_caractere(s, c):
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count

s = "banana"
c = 'a'
saida = contar_caractere(s, c)
print(saida)
