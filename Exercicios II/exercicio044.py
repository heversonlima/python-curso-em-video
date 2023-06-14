
precoProd = float(input('Informe o preço do produto: R$'))
formaPAy = int(input('Informe a condição de pagamento\n1-Pagamento em cheque a vista \
                       \n2-A vista no cartão\n3-Ate 2x no cartão\n4-Ate 3x ou mais no cartão  '))

desconto1 = precoProd * 0.1
desconto2 = precoProd * 0.05
taxa = precoProd * 0.20

if formaPAy == 1:
    print(f'\nO subtotal com 10% de desconto é: R${precoProd - desconto1}')
elif formaPAy == 2:
    print(f'\nO subtotal com 5% de desconto é: R${precoProd - desconto2}')
elif formaPAy == 3:
    print(f'\nEm até 2x vezes no cartão não há desconto. Seu subtotal é: R${precoProd}')
elif formaPAy == 4:
    print(f'\nEm tres vezes ou mais no cartão será cobrado uma taxa de 20% do valor.\
          \nSeu subtotal é de: R${precoProd + taxa}')
else:
    print('Opa, algo deu errado. Revise os dados e tente novamete..')


 