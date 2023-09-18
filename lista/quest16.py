"""" Leia a idade e o tempo de serviço de um trabalhador e escreva se ele
pode ou não se aposentar. As condições para aposentadoria são:
 As condições para aposentadoria são: - Ter pelo menos 65 anos, - Ou ter trabalhado pelo menos 30 anos, 
- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos. 17
"""
idade = int (input ('Digite a sua idade: '))
tempo_servico = float (input ('Digite o seu tempo de serviço: '))

if idade >= 65:
    print ('Já é possível se aposentar.')
elif tempo_servico >= 30:
    print ('Já é possível se aposentar.')
elif idade >= 60 and tempo_servico >= 25:
    print ('Já é possível se aposentar.')
else:
    print ("Não é possível se aposentar.")
