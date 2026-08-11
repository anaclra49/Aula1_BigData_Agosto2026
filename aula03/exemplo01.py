# GITHUB
print('Github - Aula 03')
 
#Exemplo01 - Veículo 10 km/1 
CONSUMO = 10     #Constantes
distancia1 = float(input('Informe a distancia: '))
distancia2 = float(input('Informe a outra distancia: '))

# Processamento 
distancia_total = distancia1 + distancia2 
combustível = distancia_total / CONSUMO

# Saída: 
print(f'Distancia percorrida{distancia_total}')
print(f'Consumo de {combustível} litros')
