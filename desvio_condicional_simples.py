'''
Crie um programa que pergunte dois numeros do usuário.
Em seguida o programa deverá somar os dois numeros e
apresentar o resultado se o vlaor for maior que 10
'''

num1 = int(input("Informe um número: "))
num2 = int(input("Informe um número: "))

soma = num1 + num2

if (soma > 10):
    print(f"A soma dos valores inseridos é {soma}")

print("FIM DO PROGRAMA")
