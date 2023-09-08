"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total."""
import math

tamanho_parede = float (input ('Digite o tamanho da parede que vai ser pintada: '))
quant_tinta = tamanho_parede / 3
quant_latas = math.ceil(quant_tinta / 18)
valor_latas = quant_latas * 80

print (f'Para pintar a parede, é necessário {quant_latas:.2f} latas de tinta.\nO preço total das tintas é R${valor_latas:.2f}')