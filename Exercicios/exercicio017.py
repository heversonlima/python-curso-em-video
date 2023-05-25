# Cateto e hipotenusa
import math, os

catOp = float(input('Informe o comprimento do cateto oposto: '))
catAd = float(input('Informe o comprimento do cateto adjacente: '))

# Resolvendo  probelma com modulo math   
hi = math.hypot(catOp, catAd)
print(f'O comrprimento da hipotenusa é: {hi}')