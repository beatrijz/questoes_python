"""11. Faça um programa que receba um número inteiro e verifique se este
número é par ou ímpar, positivo ou negativo. """
numero = int (input('Digite um número: '))
if numero > 0:
    if numero % 2 == 0:
        print (f'O número {numero} é um par positivo.')
    else:
        print(f'O número {numero} é um ímpar positivo.')
else:
    if numero % 2 == 0:
        print (f'O número {numero} é um par negativo.')
    else:
        print(f'O número {numero} é um ímpar negativo.')
