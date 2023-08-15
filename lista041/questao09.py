'''
Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

num = int(input("Informe um número aqui: "))

if (num < 0):
    print("Este número é negativo")

if (num == 0):
    print("Este número é nulo")

if (num > 0):
    print("Este número é positivo")