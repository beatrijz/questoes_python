"""14. A nota final de um estudante é calculada a partir de três notas atribuídas
entre o intervalo de 0 até 10, respectivamente, a um trabalho de
laboratório, a uma avaliação semestral e a um exame final. A média das
três notas mencionadas anteriormente obedece aos pesos: Trabalho de
Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o
resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as
verificações necessárias."""
nome = input ('Digite o nome do aluno: ')
trabalho_lab = float (input ('Digite a nota do trabalho no laboratório: '))
avaliacao_semestral = float (input('Digite a nota da avaliação semestral: '))
exame_final = float (input ('Digite a nota do exame final: '))
media_notas = 0
if (trabalho_lab >= 0 and trabalho_lab <= 10) and (avaliacao_semestral >= 0 and avaliacao_semestral <= 10) and (exame_final >= 0 and exame_final <= 10):
    media_notas = ((trabalho_lab * 2) + (avaliacao_semestral * 3) + (exame_final * 5)) / 10
else:
    print ('Alguma nota digitada é inválida.')

if media_notas >= 0 and media_notas <= 2.9:
    print (f'{nome} está reprovado.\nA nota final foi de {media_notas}.')

if media_notas >= 3 and media_notas <= 4.9:
    print (f'{nome} está em recuperação.\nA nota final foi de {media_notas}.')  

if media_notas >= 5 and media_notas <= 10:
    print (f'{nome} foi aprovado.\nA nota final foi de {media_notas}.')