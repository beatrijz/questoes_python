"""Faça um programa que leia um numero inteiro “N” e depois imprima os N
primeiros números naturais ímpares. """
n = int(input("Digite um número inteiro: "))
i = 0
numero_impar = 1

while i < n:
    print (numero_impar, end=" ")
    numero_impar += 2
    i += 1
