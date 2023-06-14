import random

escolha = input('Escolha pedra, papel ou tesoura: ').lower()


ppt = ['pedra', 'papel', 'tesoura']
botChoose = random.choice(ppt)

perdeu = escolha == 'papel' and botChoose == 'tesoura' \
        or escolha == 'pedra' and botChoose == 'papel' \
        or escolha == 'tesoura' and botChoose == 'pedra'

ganhou = escolha == 'pedra' and botChoose == 'tesoura' \
        or escolha == 'papel' and botChoose == 'pedra' \
        or escolha == 'tesoura' and botChoose == 'papel'

erro = escolha != 'pedra' and escolha != 'papel' and escolha != 'tesoura'
        
if erro:
    print(f'OPA. A palavra "{escolha}" não está escrita corretamente.\nTente novamente')
else:
    if perdeu:
        print(f'Você escolheu {escolha}\nO bot escolheu {botChoose}\nVocê perdeu..')
    elif ganhou: 
        print(f'Você escolheu {escolha}\nO bot escolheu {botChoose}\nVocê ganhouu!')
    elif escolha.isdigit():
        print('OPA. Não digite numeros.\nTente novamente esolhendo pedra, papel ou tesoura\nEscreva apenas letras')
    else:
        print(f'Você escolheu {escolha}\nO bot escolheu {botChoose}\nParece que temos um empate')



