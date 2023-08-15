'''
Desenvolver um programa que pergunte um número inteiro qualquer e verifique
se ele está na faixa de 1 a 10.
'''

num = int(input("Informe um número: "))

if (num < 10 and num > 1):
    print("Este número esta na faixa de 1 a 10")

else:
    print("Este número não esta na faixa de 1 a 10")