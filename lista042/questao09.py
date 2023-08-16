'''
Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos.
'''

#logica do op ternario1: var = (se for falso, se for verdadeiro)[teste condicional]
idade = int(input("Insira sua idade: "))

if (idade >= 18 and idade <= 65):
    print("Você é maior de idade!")

if (idade >= 65):
    print("Você é maior de 65 anos!")

else:
    print("Você é menor de idade!")