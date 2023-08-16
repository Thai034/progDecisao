'''
Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.
'''

num1 = int(input("Insira um número: "))
num2 = int(input("Insira um outro número: "))

if (num1 < num2):
    print(f"O maior número será {num2}")
    print(f"E o menor número será {num1}")

if (num1 > num2):
    print(f"O maior número será {num1}")
    print(f"E o menor número será {num2}")

if (num1 == num2):
  print("Os dois números são iguais")