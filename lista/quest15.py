"""Faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são: 
- "Telefonou para a vítima?"
- "Esteve no local do crime?"
"Mora perto da vítima?"
- "Devia para a vítima?"
- "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente".


"""
nome = input ('Digite o seu nome: ')
perguntas = [
    "Telefonou para a vítima? (S (sim)/N (não)): ",
    "Esteve no local do crime? (S (sim)/N (não)): ",
    "Mora perto da vítima? (S (sim)/N (não)): ",
    "Devia para a vítima? (S (sim)/N (não)): ",
    "Já trabalhou com a vítima? (S (sim)/N (não)): "
]
respostas = []

for pergunta in perguntas:
    resposta = input(pergunta).strip().upper()
    while resposta not in ['S', 'N']:
        print("Resposta inválida. Por favor, responda com 'S' (sim) ou 'N' (não).")
        resposta = input(pergunta).strip().upper()
    respostas.append(resposta)

aux = respostas.count('S')
if aux == 2:
    print (f"{nome} é suspeito!")
if aux >= 3 and aux <= 4:
    print (f"{nome} é cúmplice!")
if aux == 5:
    print (f'{nome} é o assassino!')
if aux == 0:
    print (f'{nome} é inocente!')