# Conversão de metros para centímetros e milímetros 

metros = float(input('Insira um valor em metros: '))

print(f'{metros} metros são {metros/1000:.1f}km')
print(f'{metros} metros são {metros/100:.1f} hectometros')
print(f'{metros} metros são {metros/10:.1f} decâmetros')
print(f'{metros} metros são {metros*10:.1f} decimetros')
print(f'{metros} metros são {metros*100:.0f} centimetros') 
print(f'{metros} metros são {metros*1000:.0f} milimetros')


