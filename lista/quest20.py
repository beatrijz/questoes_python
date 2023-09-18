"""Faça um programa que leia 10 inteiros e imprima sua media. """
i = 1
valores = []
while i <= 10:
    valor = int (input (f'Digite o {i}° valor: '))
    i+=1
    valores.append (valor)
soma = sum (valores)
media = soma / 2 
print (f"A média dos valores digitados é: {media:.2f}")