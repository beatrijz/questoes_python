"""27. Escreva um programa que leia um numero inteiro positivo “N” e em
seguida imprima “N” linhas do chamado Triângulo de Floyd. Para n = 6,
temos:"""
numero = int(input('Digite o número para o tamanho do Triângulo de Floyd: '))

count = 1
for i in range(1, numero + 1):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()