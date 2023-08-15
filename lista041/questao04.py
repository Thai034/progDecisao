'''
Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

num = int(input("Me informe um número: "))
resul = num % 4
resul2 = num % 5

if (resul == 0 and resul2 == 0):
    print(f"{num} é divisivel por 4 e 5!")

else:
    print("Valor não é divisível por 4 e 5")