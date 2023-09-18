""" Faça um programa que peça ao usuário para digitar 10 valores e some-os
e imprima o resultado. """
i = 1
valores = []
while i <= 10:
    valor = int (input (f'Digite o {i}° valor: '))
    i+=1
    valores.append (valor)
soma = sum (valores)
print (f"O total da soma dos valores é: {soma}")
