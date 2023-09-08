num1 = int (input('Digite o primeiro número: '))
num2 = int (input ('Digite o segundo número: '))
num3 = int (input ('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print ('O primeiro número é o maior.')
if num2 > num1 and num2 > num3:
    print ('O segundo número é o maior.')
if num3 > num1 and num3 > num2:
    print ('O terceiro número é o maior.')
if num1 < num2 and num1 < num3:
    print ('O primeiro número é o menor.')
if num2 < num1 and num2 < num3:
    print ('O segundo número é o menor.')
if num3 < num1 and num3 < num2:
    print ('O terceiro número é o menor.')
