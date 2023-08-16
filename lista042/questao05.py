'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

#logica do op ternario1: var = (se for falso, se for verdadeiro)[teste condicional]

sigla = input("Insira uma sigla de uma estado Brasileiro: ")

if ((sigla == "RJ") or (sigla == "SP") or (sigla == "MG") or (sigla == "ES")):
    print(f"O estado da sigla {sigla} pertence a região Sudeste")

else:
    print(f"O estado da sigla {sigla} não pertence a região Sudeste")
