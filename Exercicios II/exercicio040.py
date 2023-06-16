# Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
reprovado = media < 5
recuperacao = media >= 5 and media < 7
aprovado = media >= 7
erro = nota1 < 0 and nota1 > 10 or nota2 < 0 and nota2 > 10

if reprovado:
    print(f'Meida: {media}\nConceito: Reprovado.')
elif recuperacao:
    print(f'Media: {media}\nConceito: Recuperação')
elif aprovado:
    print(f'Media: {media}\nConceito: Aprovado.')
if erro:
    print(f'A sua nota não pode ser menor que 0 nem maior que 10')
else:
    print('Algo deu errado. Tente novamente..')