""" Leia a distância em Km e a quantidade de litros de gasolina consumidos
por um carro em um percurso, calcule o consumo em Km/l e escreva uma
mensagem de acordo com a tabela abaixo:"""
distancia_km = float(input('Digite a distância percorrida (em Km): '))
litros_gasolina = float(input('Digite a quantidade de litros de gasolina consumidos: '))

consumo_por_litro = distancia_km / litros_gasolina
print (consumo_por_litro)
if consumo_por_litro < 8:
    print ('Venda o carro!')
if consumo_por_litro >= 8 and consumo_por_litro <= 12:
    print ('Econômico!')
if consumo_por_litro > 12:
    print ('Super econômico!')