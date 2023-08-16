'''
Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:
Média Situação
Abaixo de 3,0 Reprovado
Entre 3,0 e 6,9 Prova Final
A partir de 7,0 Aprovado
'''

nome = input("Me informe seu nome: ")
nota1 = float(input("Me informe sua primeira nota: "))
nota2 = float(input("Me informe sua segunda nota: "))

media = (nota1 + nota2)/2

if (media < 3.0):
    print("Você está reprovado")

if (media >= 3.0 and media <= 6.9):
    print("Você depende da Prova final!")

if (media >= 7.0):
    print(f"Parabéns {nome} você está aprovado!")