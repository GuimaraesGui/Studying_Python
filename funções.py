# Principais funções:
"""
print() # - Imrime uma mensagem (int, float, str) no console.
input() # - Retorna um dado informado pelo usuário e pode receber uma string.
len()  # - Recebe uma lista e retorna o tamanho dessa lista.
max() # - Retorna o maior valor de uma lista
"""
# Criação de funções
# Função inicial

def saudacao(nome, curso="Python"):
    print("\n")
    print(f"Seja bem-vindo(a), {nome}!")
    print("\n")
    print(f"Olá, é um prazer ter você fazendo parte do curso de {curso}!")
    print("\n")

saudacao("Guilherme")

# Funções com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print("O resultado da soma é",resultado)

def calculadora(num1, num2, operacao="+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    
resultado = calculadora(10, 20, "-")

print(resultado)