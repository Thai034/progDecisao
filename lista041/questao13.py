'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c)
 e ao final apresente-os dispostos em ordem crescente.
'''

print("Me informe três valores")

a = int(input("Informe o primeiro numero: "))
b = int(input("Informe o segundo numero: "))
c = int(input("Informe o terceiro numero: "))

# 1- a tem que ser menor que b

if (a > b):
    aux = a
    a = b
    b = aux
#garantido até aqui que entre a e b o menor está em a

 # 2- a precisa ser menor que c

if (a > c):
    aux = a
    a = c
    c = aux
#garantido até aqui que a é o menor dos 3
# agora é necessário garantir que b seja menor que c

if (b > c):
    aux = b
    b = c
    c = aux
#garantido até aqui que entre b e c, o b é menor, ou seja, o c é o maior de todos

print(f"Ordem crescente: {a}, {b} e {c}")

'''
if (a < b < c):
    print(f"a ordem crescente é {a, b, c}")
    
if (a < c < b):
    print(f"a ordem crescente é {a, c, b}")
    
if (b < a < c):
    print(f"a ordem crescente é {b, a, c}")
    
if (b < c < a):
    print(f"a ordem crescente é {a, b, c}")
    
if (c < b < a):
    print(f"a ordem crescente é {c, b, a}")
    
if (c < a < b):
    print(f"a ordem crescente é {c, a, b}")
'''


