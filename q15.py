# Substituir caractere
# Dada uma string s e dois caracteres c1 e c2, retorne uma nova string com todas as ocorrências de c1 substituídas por c2.
# Entrada: s = "banana", c1 = 'a', c2 = 'o'
# Saída: "bonono"

def substituir_caractere(s, c1, c2):
    resultado = ""
    for char in s:
        if char == c1:
            resultado += c2
        else:
            resultado += char
    return resultado

s = "banana"
c1 = 'a'
c2 = 'o'
saida = substituir_caractere(s, c1, c2)
print(saida)
