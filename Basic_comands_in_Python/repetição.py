numero_sorteado = 15

numero_escolhido = int(input("Informe um numero entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
    print("Você errou. Tente novamente ... ")
    numero_escolhido = int(input("Informe um numero entre 1 e 20: "))

print("Parabéns! Você acertou.")

# Estrutura com contador

cont = 0

while cont <5:
    print(cont)

    cont = cont + 1
