"""13. Faça um programa que receba a altura e o sexo de uma pessoa e calcule
e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h
corresponde à altura): 
- Homens: (72.7 * h) − 58
- Mulheres: (62, 1 * h) − 44, 7"""
nome = input ('Digite o seu nome: ')
sexo = input ('Digite o seu sexo (F/M): ').upper()
altura = float (input('Digite a sua altura: '))
peso_ideal = 0 

if sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = (72.7 * altura) - 58

pessoa = {
    nome : peso_ideal
}
for pessoa_nome, pessoa_peso in pessoa.items():
    print (f'{pessoa_nome} o seu peso ideal é {pessoa_peso:.2f}kg.')
