"""Faça um programa que receba dois números. Calcule e mostre: 
- a soma dos números pares desse intervalo de números, incluindo os
números digitados; 
- a multiplicação dos números ímpares desse intervalo, incluindo os
digitados;"""

numero1 = int (input ('Digite o primeiro número: '))
numero2 = int (input ('Digite o segundo número: '))
multiplicacao_impares = 1

i = 0
numeros_pares = []
numeros_impares = []
if numero1 < numero2:
    i = numero1
    while i <= numero2:
        if i % 2 == 0:
            numeros_pares.append (i)
        else:
            numeros_impares.append (i)
        i +=1
else:
    i = numero2
    while i <= numero1:
        if i % 2 == 0:
            numeros_pares.append (i)
        else:
            numeros_impares.append (i)
        i +=1

soma_pares = sum (numeros_pares)
print (f'A soma dos números pares desse intervalo é {soma_pares}')

for x in numeros_impares:
    multiplicacao_impares *= x  
print (f'A multiplicação dos números ímpares desse intervalo é: {multiplicacao_impares}')
