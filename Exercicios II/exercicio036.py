# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

nome = input('Ola, Digite seu nome: ')
salario = float(input('Informe seu salario: '))
precoCasa = float(input(f'Legal {nome},agora informe o valor da casa que deseja comprar: '))
qtdAnos = int(input('Por quantos anos quer pagar essa casa? '))

maisDeUmAno = qtdAnos >= 1
limiteEmprestimo = qtdAnos > 30

if maisDeUmAno:
    qtdParcelas = qtdAnos * 12
    parcelamentoCasa = precoCasa / qtdParcelas
    if parcelamentoCasa > salario * (30/100):
        print(f'Caro {nome}, infelizmente você não pode financiar esta casa.')
    else:
        print(f'Pra pagar a casa de {precoCasa:.2f} em {qtdAnos} anos, a prestação será de {parcelamentoCasa:.2f}')
        print('Emprestimo concedido')
if limiteEmprestimo:
    print(f'Opa, {nome}, determinamos como em até 30 o numero máximo de financiamento para compra da sua casa..')


