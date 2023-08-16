'''
Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”.
'''

#logica do op ternario1: var = (se for falso, se for verdadeiro)[teste condicional]
ano = int(input("Insira seu ano de nascimento: "))
atual = int(input("Insira o ano atual: "))

idade = atual - ano

if (atual == 2023):
    print(f"Sua idade é {idade}")

else:
    print("Dados inseridos estão incorretos")