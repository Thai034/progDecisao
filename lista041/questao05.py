'''
Desenvolver um programa que pergunte 4 notas escolares de um aluno
e exiba mensagem informando que o aluno foi aprovado se a média
escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar
uma mensagem informando essa condição. Apresentar junto com a mensagem
de aprovação ou reprovação o valor da média obtida pelo aluno.
'''

print("Me informe suas 4 notas: ")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

resul = (nota1 + nota2 + nota3 + nota4)/4

if (resul >= 5):
    print("Você está aprovado!")

else:
    print("Você infelizmente está reprovado!")


