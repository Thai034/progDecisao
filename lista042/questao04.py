'''
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
'''
num = int(input("Por favor, insira um número de 1 a 7: "))

if (num == 1):
    print(f"O número {num} corresponde a Domingo")

if (num == 2):
    print(f"O número {num} corresponde a Segunda-feira")

if (num == 3):
    print(f"O número {num} corresponde a Terça-feira")

if (num == 4):
    print(f"O número {num} corresponde a Quarta-feira")

if (num == 5):
    print(f"O número {num} corresponde a Quinta-feira")

if (num == 6):
    print(f"O número {num} corresponde a Sexta-feira")

if (num == 7):
    print(f"O número {num} corresponde a Sábado")

