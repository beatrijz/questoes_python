"""12. Faça um programa que leia 2 notas de um aluno, verifique se as notas são
válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua
um valor válido, este fato deve ser informado ao usuário e o programa
termina. """
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = 0

if (nota1 < 0.0 or nota1 > 10.0) and (nota2 < 0.0 or nota2 > 10.0):
    print('A primeira e a segunda nota são inválidas.')
elif nota1 < 0.0 or nota1 > 10.0:
    print('A primeira nota informada é inválida')
elif nota2 < 0.0 or nota2 > 10.0:
    print('A segunda nota informada é inválida')
else:
    media = (nota1 + nota2) / 2

    aluno = {
        nome: media
    }
    
    for nome_aluno, media_aluno in aluno.items():
        print(f'A média das notas do aluno {nome_aluno} é {media_aluno:.2f}')
