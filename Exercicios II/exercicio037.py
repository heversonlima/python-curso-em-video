# Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.
# conteudo para ajuda https://www.delftstack.com/pt/howto/python/python-int-to-binary/

try:
    number = int(input('Digite um valor: '))

    choice = int(input(f'Deseja converter o numero {number} para:\n1-Binario\n2-Octal\n3-hexadecimal:\n\n'))

    binario = format(number, "b") # ultilzamos a conversão diretamente pelo format
    octal = format(number, "o")   # onde os paramentros "b", "o", "x" correspodem
    hexadecimal = format(number, "x") # a cada tipo de conversão

    if choice == 1:
        print(f'{number} em binário é igual a: {binario}')
    elif choice == 2:
        print(f'Convertendo o numero {number} para octal o resultado será: {octal}')
    elif choice == 3:
        print(f'Convertendo o numero {number} para hexadecimal o resultado sera: {hexadecimal}')
    else:
            print('Digite o valor de acordo com o menu de conversão, de 1 ate 3')
except:
    print('Recomendo que digite apenas numeros inteiros e tente novamente')

# CODIGO DO PROFESSOR
# if choice == 1:
#         print(f'{number} em binário é igual a: {number(bin(number)[2:])}')
#     elif choice == 2:
#         print(f'Convertendo o numero {number} para octal o resultado será: {number(oct(number)[2:])}')
#     elif choice == 3:
#         print(f'Convertendo o numero {number} para hexadecimal o resultado sera: {number(hex(number)[2:])}')
#     else:
#         print('Digite o valor de acordo com o menu de conversão, de 1 ate 3')
# except:
#     print('Recomendo que digite apenas numeros inteiros e tente novamente')

