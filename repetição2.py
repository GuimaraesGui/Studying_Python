for i in range(10):
    print(i)

print("\n")

for i in range(1, 10):
    print(i)

print("\n")

for i in range(1, 12, 1):
    print(i)

print("\n")
#Automatizando escritas. Exemplo em notas
soma = 0
for i in range(1, 4, 1):
    nota = float(input(f"Informe sua nota {i}: ")) 
    soma = soma + nota
    
    cont = 0
    cont = cont + i

media = soma/cont

print("A media das notas é: ", media)