"""Faça um programa que leia um número e, caso ele seja positivo, calcule e
mostre: - O número digitado ao quadrado
- A raiz quadrada do número digitado"""
numero = int (input('Digite um número: '))

if numero > 0:
    print (f'O número ao quadrado: {numero ** 2}')
    print (f'A raíz do número: {numero ** 0.5:.2f}')