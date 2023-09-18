""" Faça um programa que permita ao usuário digitar o seu nome e em seguida
mostre o nome do usuário de trás para frente utilizando somente letras
maiúsculas. Dica: lembre−se que ao informar o nome, o usuário pode digitar
letras maiúsculas ou minúsculas."""
nome = input ('Digite o seu nome: ').upper()
nome_list = []
i = len (nome)
x = -1
while i >= x:
    x += 1
    i -= 1
    print (nome [i], end ="")
