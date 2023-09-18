"""Faça um programa que imprima a tabuada de multiplicação de 1 a 9;"""
numero = int(input('Digite o número para o qual deseja imprimir a tabuada de multiplicação: '))

print(f'Tabuada de multiplicação para o número {numero}:')
for i in range (1, 10):
    multiplicacao = numero * i
    print (f'{numero} X {i} = {multiplicacao}')