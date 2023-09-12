"""Escreva um programa para contar a quantidade de números pares entre dois
números quaisquer fornecidos pelo usuário"""
numero1 = int (input('Digite o primeiro número: '))
numero2 = int (input('Digite o segundo número: '))
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

list_pares = []
while numero1 <= numero2:
    if numero1 % 2 == 0:
        list_pares.append (numero1)
    numero1 += 1
print (f'Os números pares são: {list_pares}')