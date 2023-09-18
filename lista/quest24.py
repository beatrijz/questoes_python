"""Faça um programa que leia um numero inteiro positivo “N” e imprima
todos os números naturais de 0 até N em ordem decrescente."""
n = int(input("Digite um número inteiro: "))
i = n
for i in range ( i, -1, -1):
    print (i, end= " ")
    i -=1