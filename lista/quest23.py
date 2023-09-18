"""Faça um programa que leia um numero inteiro positivo “N” e imprima
todos os números naturais de 0 até “N” em ordem crescente."""
n = int(input("Digite um número inteiro: "))

for i in range (n + 1):
    print (i, end= " ")
    i +=1