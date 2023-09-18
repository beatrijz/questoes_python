"""Faça um programa que leia 2 strings e informe o conteúdo delas seguido do
seu comprimento. Informe também se as duas strings possuem o mesmo
comprimento e são iguais ou diferentes no conteúdo."""
string1 = input ('Digite a primeira string: ')
string2 = input ('Digite a segunda string: ')
print (f'O conteúdo da primeira string é: {string1} e o comprimento: {len(string1)}')
print (f'O conteúdo da segunda string é: {string2} e o comprimento: {len(string2)}')

if (len(string1) == len(string2)):
    print (f'A primeira e a segunda String tem tamanhos iguais.')
    if (string1 == string2):
        print ('E, também, o conteúdo é igual.')
    else:
        print (f'As strings são diferentes no conteúdo e no tamanho. ')