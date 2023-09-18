"""Faça um programa que solicite uma string ao usuário e em
seguida a imprima em formato de escada."""
frase = input ('Digite uma string: ')
i = 0
for i in range (len (frase)):
    i += 1
    print (frase [:i])
    