"""Modifique o programa anterior de forma que este imprima apenas os
números que são pares."""
i = 0
num = 0
list_pares = []
while i <= 50:
    if i % 2 == 0:
        list_pares.append (i)
    i += 1
print (f'Os números pares são: {list_pares}')