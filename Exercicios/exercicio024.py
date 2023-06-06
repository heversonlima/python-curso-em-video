city = input('Em que cidade voce nasceu? ').strip(); # strip() para eliminar os espaços

print('Tem santo? ', city[:5].upper() == 'SANTO')