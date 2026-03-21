# Remover espaços
# Dada uma string s, retorne uma nova string com todos os espaços removidos.
# Entrada: s = "ola mundo"
# Saída: "olamundo"

def remover_espacos(s):
    resultado = ""
    for char in s:
        if char != ' ':
            resultado += char
    return resultado

s = "ola mundo"
saida = remover_espacos(s)
print(saida)
