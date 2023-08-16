'''
Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000.
'''

num = int(input("Informe um número: "))

if (num < 1000):
    print(f"O número {num} é menor que 1000")

else:
    print(f"O número {num} é maior que 1000")