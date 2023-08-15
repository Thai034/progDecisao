'''
Desenvolver um programa que pergunte um valor inteiro positivo ou negativo,
e exiba como resposta o módulo deste valor, ou seja, o número lido como sendo
positivo.
'''

num = int(input("Informe um número: "))

if (num < 0):
    resultado = num * -1
    print(f"O módulo do seu numero é {resultado}!")

else:
    print(f"O módulo do seu número é {num}!")