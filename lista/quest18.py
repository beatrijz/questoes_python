"""Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 2
vezes. A primeira vez deve usar a estrutura de repetição “for”, a segunda
vez a estrutura “while”."""
j = 1
for i in range (1, 101):
    print (i, end=" ")
print ("\n")
while j <= 100:
    print (j, end=" ")
    j +=1
