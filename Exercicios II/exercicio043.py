
peso = float(input('Informe seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (peso * peso)

abaixo = imc < 18.5
pesoIdeal = imc >= 18.5 and imc <= 25
sobrepeso = imc > 25 and imc <= 30
obesidade = imc > 30 and imc <= 40
obesidadeMorb = imc > 45

if abaixo:
    print(f'Seu imc é de {imc}. Está abaixo do Peso.')
elif pesoIdeal:
    print(f'Seu imc é de {imc}. Está no seu peso ideal.')
elif sobrepeso:
    print(f'Seu imc é de {imc}. Está em sobrepeso')
elif obesidade:
    print(f'Seu imc é de {imc}. Está na Obesidade')
elif obesidadeMorb:
    print(f'Seu imc é de {imc}. Está na obesidade mórbida')
else:
    print('Erro. Revise seus dados e tente novamente..')