'''
Crie um rpograma que pergunte a idade do usuário
e em seguida informe se este usuário é menor de idade ou maior de idade.
'''

idade = int(input("Informe a sua idade: "))

#logica do op ternario1: var = (se for falso, se for verdadeiro)[teste condicional]
resposta = ("Você é menor de idade", "Você é maior de idade")[idade>=18]

print(resposta)