frase = input ('Digite uma frase: ')
for i in range (len (frase)):
    i += 1
    print (frase [:i])

for x in range (len (frase)):
    print (frase [x:])
    x += 1