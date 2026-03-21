# Maiúsculas e minúsculas
# Dada uma string s, retorne quantas letras são maiúsculas e quantas são minúsculas.
# Entrada: s = "AbCde"
# Saída: Maiusculas: 2 | Minusculas: 3

def contar_maiusculas_minusculas(s):
    maiusculas = 0
    minusculas = 0
    for char in s:
        if char.isupper():
            maiusculas += 1
        elif char.islower():
            minusculas += 1
    return maiusculas, minusculas

s = "AbCde"
maiusculas, minusculas = contar_maiusculas_minusculas(s)
print(f"Maiúsculas: {maiusculas}")
print(f"Minúsculas: {minusculas}")
