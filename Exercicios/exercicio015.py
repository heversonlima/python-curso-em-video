# aluguel de carros

qtdDias = float(input('O carro ficou quantos dias alugado? '))
qtdKm = float(input('Quantos quilometros percorridos? '))

custo = 60 * qtdDias
custoKm = 0.15 * qtdKm

soma = custo + custoKm
print(f'O total a pagar é de: R${soma}')