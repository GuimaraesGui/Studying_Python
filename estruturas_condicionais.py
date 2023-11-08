# Função if-else
idade = int(input("Qual é a sua idade? "))

if idade < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")

# Função if-elif-else (Se tiver mais de duas condições, abordar elif antes de else)

print("________________________________________________")

if idade < 18:
        print("Você é criança")
elif idade >= 18:
     print("Você é adulto")
elif idade > 60:
    print("Você é idoso")
