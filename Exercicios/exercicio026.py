frase = str(input('Digite uma frase: ')).upper()

print(f'Quantas vezes a letra A aparece: {frase.count("A")}')
print(f'A posicao da primeira letra "A" esta: {frase.find("A")}')
print(f'A posicao da ultima letra "A" esta: {frase.rfind("A")+1}')