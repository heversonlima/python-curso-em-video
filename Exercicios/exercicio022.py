nome = input('Informe seu nome: ')

primeiroNome = nome.split()[0] #linha pra pegar o primeiro nome

print(f'\nNome maiusculo: {nome.upper()}') 
print(f'Nome minusculo: {nome.lower()}')

print(f'Primeira letra do seu nome: {len(primeiroNome)}') # len para contar quantas letras tem

 # contando quantas letras tem, desconsiderando espaços
print(f'Seu nome possui ', len(nome.replace(' ', '')), ' letras') 
