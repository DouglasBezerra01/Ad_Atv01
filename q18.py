# Primeiro caractere
# Dada uma string s, retorne o primeiro caractere. Se a string estiver vazia, retorne um valor nulo.
# Entrada: s = "python"
# Saída: 'p'

def primeiro_caractere(s):
    if len(s) == 0:
        return None
    return s[0]

s = "python"
saida = primeiro_caractere(s)
print(saida)
