numero = int (input ('Digite um número: '))
if numero %2 != 0:
    print ('O número digitado é um ímpar', end = " ")
else:
    print ('O número digitado é um par', end=" ")
if numero >= 0:
    print ('positivo.')
else:
    print ('negativo.')