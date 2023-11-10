#Vetor e matrizes

# > Vetor
notas = [7.9, 9.7, 8.2]
notas = [3]
lista = [26, "Guilherme", 3.14159, False]
lista_de_listas = [10, [1,2,3]]

#Indexação e Slices (fatiamento)
# > Indexação
lista = [10, "Guilhernme", 3.14159, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# > Slice

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3])

print("\n")

#Interação com for
# > Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

print("\n")

# > utilizando o tamanho da lista

print("Comrpimento da lista: ",len(lista)) #Len verifica o tam do array

for i in range(len(lista)): #Imprime os índices da funcao Len
    print(i)

print("\n")

for i in range(len(lista)):
    print(lista[i])
