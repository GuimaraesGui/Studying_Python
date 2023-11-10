# > Dicionarios

# > Crian dicionários

dicionario = { } #Como criar um dicionário
dicionario = dict() #Como cria um dicionário vazio

dicionario = { "nome": "Guilherme", "idade": 26, "Altura": 1.77} #Exemplo de dicionário

print(dicionario) #imprimindo um dicionário inteiro.
print("\n")
print(dicionario["idade"]) #Imprime o valor(26) da chave(idade) -> Imprime um dicionario em especifico

dicionario["programador"] = True #Cria chave (Programador) e atribui valor (True)

print(dicionario)

dicionario["Altura"] = 2 #Acessa o dicionario(altura) e reescreve o seu valor(passa a ser 2)

# > Iterando sobre um dicionário

for variavel in dicionario: #Imprime a chave do dicionario
    print("\n")
    print(variavel)

for chave in dicionario:
    print("____________")
    print(chave, dicionario[chave])

# > Verificando a existência de uma chave no dicionário
print("\n")
print("Altura" in dicionario)
print("Peso" in dicionario)