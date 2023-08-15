'''
Desenvolver um programa que pergunte dois valores numéricos inteiros
e apresente o valor da diferença entre o maior valor e o menor valor lido.
'''

print("Me informe dois valores inteiros")

valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))

if (valor1 > valor2):
        div = valor1 - valor2
        print(f"{div} é a diferença entre {valor1} e {valor2}")

else:
    resul = valor2 - valor1
    print(f"{resul} é a diferença entre {valor1} e {valor2}")