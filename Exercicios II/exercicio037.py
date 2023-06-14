
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



