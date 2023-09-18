"""Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média."""
i = 1
j = 1
valores = []
valores_positivos = []
while i <= 10:
    valor = int (input (f'Digite o {i}° valor: '))
    i+=1
    valores.append (valor)
while j <= len (valores):
    for num in valores:
        if num > 0:
            valores_positivos.append (num)
    j += 1
soma = sum (valores_positivos)
media = soma / len (valores_positivos)
print (f"A média dos valores positivos digitados é: {media:.2f}")