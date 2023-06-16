
peso = float(input('Informe seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

abaixo = imc < 18.5
pesoIdeal = imc >= 18.5 and imc < 25
sobrepeso = imc >= 25 and imc < 30
obesidade = imc >= 30 and imc < 40
obesidadeMorb = imc > 45

if abaixo:
    print(f'Seu imc é de {imc:.1f}. Está abaixo do Peso.')
elif pesoIdeal:
    print(f'Seu imc é de {imc:.1f}. Está no seu peso ideal.')
elif sobrepeso:
    print(f'Seu imc é de {imc:.1f}. Está em sobrepeso')
elif obesidade:
    print(f'Seu imc é de {imc:.1f}. Está na Obesidade')
elif obesidadeMorb:
    print(f'Seu imc é de {imc:.1f}. Está na obesidade mórbida')
else:
    print('Erro. Revise seus dados e tente novamente..')