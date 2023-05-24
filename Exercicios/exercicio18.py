# seno e cosseno
 
import math

value = float(input('Informe um valor em graus'))

seno = math.sin(math.radians(value))
cosseno = math.cos(math.radians(value))
tangente = math.tan(math.radians(value))

print(f'Seno: {seno}')
print(f'Cosseno: {cosseno}')
print(f'Tangente: {tangente}')