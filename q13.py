# Verificar palíndromo
# Dada uma string s, verifique se ela é um palíndromo, ou seja, se é igual quando lida de trás para frente.
# Desconsidere diferenças entre maiúsculas e minúsculas.
# Entrada: s = "arara"
# Saída: verdadeiro
# Entrada: s = "casa"
# Saída: falso

def verificar_palindromo(s):
    s = s.lower()
    esquerda = 0
    direita = len(s) - 1
    while esquerda < direita:
        if s[esquerda] != s[direita]:
            return False
        esquerda += 1
        direita -= 1
    return True

s = "arara"
saida = verificar_palindromo(s)
print(saida)
