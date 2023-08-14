'''
crie um programa que pergunte um numero ao usuario.
Em seguida o programa deve informar se o número inserido
está abaixo de 100, entre 100 e 200 ou acima de 200.
'''

num = int(input("Informe um número: "))

if (num < 100):
    print(f"{num} esta abaixo de 100")
elif (num <= 200):
    print(f"{num} está entre 100 e 2000")
else:
    print(f"{num} está acima de 200")