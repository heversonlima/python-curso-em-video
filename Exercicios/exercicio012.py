# ler o valor do produto e descontar 5%

nome_prod = input('Insira o nome do produto: ')
valor_prod = float(input('Insira o valor do produto: '))

descoonto = valor_prod * (5/100)

print(f'Nome do produto: {nome_prod}')
print(f'Preço cheio: {valor_prod}')
print(f'Preço com desconto: {valor_prod - descoonto}')