"""O IMC (índice de massa corpórea) indica o grau de obesidade de uma pessoa. Este
índice é obtido pelo peso (em kg) dividido pelo quadrado da altura (em metros). A
tabela a seguir apresenta as faixas deste índice:"""
peso = int (input ('Digite o seu em peso kg: '))
altura = input ('Digite a sua altura em metros: ').replace (',', '.')
altura_formatada = float (altura)
imc = peso / (altura_formatada * altura_formatada)
if imc < 20:
    print (f'O seu IMC é: {imc:.2f}\nPeso abaixo do normal.')
elif imc >= 20 and imc < 25:
    print (f'O seu IMC é: {imc:.2f}\nO seu peso está normal.')
elif imc >= 25 and imc < 30:
    print (f'O seu IMC é: {imc:.2f}\nVocê está com sobrepeso.')
elif imc >= 30 and imc < 35:
    print (f'O seu IMC é: {imc:.2f}\nVocê está com obesidade leve.')
elif imc >= 35 and imc < 40:
    print (f'O seu IMC é: {imc:.2f}\nVocê está com obesidade moderada.')
elif imc >= 40:
    print (f'O seu IMC é: {imc:.2f}\nVocê está com obesidade mórbida.')