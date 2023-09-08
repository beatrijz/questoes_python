num1 = int (input('Digite o primeiro número: '))
num2 = int (input ('Digite o segundo número: '))
num3 = int (input ('Digite o terceiro número: '))
maior = 0
meio = 0
menor = 0
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
if num1 != maior and  num1 != menor:
    meio = num1
if num2 != maior and  num2 != menor:
    meio = num2
if num3 != maior and  num3 != menor:
    meio = num3
print (maior, meio, menor)