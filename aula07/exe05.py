"""Uma empresa concederá um aumento de salário aos seus funcionários,
variável de acordo com o cargo, conforme a tabela abaixo. Faça um
programa que leia o salário e o código do cargo de um funcionário e calcule
o seu novo salário. Se o cargo do funcionário não estiver na tabela, ele
deverá, então, receber 15% de aumento. Mostre o salário antigo, o novo
salário e a diferença entre ambos."""

salario_antes = float (input('Digite o seu salário atual: '))
codigo = int (input('Digite o código do seu respectivo cargo: '))
salario_depois = 0
if codigo == 310:
  salario_depois =  salario_antes + (5/100) * salario_antes
  print (f'O seu salário após o aumento é de R${salario_depois:.2f}')
if codigo == 456:
    salario_depois = salario_antes + (7.5/100) * salario_antes
    print (f'O seu salário após o aumento é de R${salario_depois:.2f}')
if codigo == 885:
    salario_depois = salario_antes + (10/100) * salario_antes
    print (f'O seu salário após o aumento é de R${salario_depois:.2f}')
if codigo != 310 and codigo != 456 and codigo != 885:
    salario_depois = salario_antes + (15/100) * salario_antes
    print (f'O seu salário após o aumento é de R${salario_depois:.2f}')
   
