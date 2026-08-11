preco_unitario = input('Valor do ingresso: ') # '20'
preco_unitario = float(preco_unitario) # 20.0 

valor_disponível = float(input('Informe o valor disponível: ')) 

quantidade = int(valor_disponível // preco_unitario)
troco = valor_disponível % preco_unitario
print(f'quantidade de ingressos: {quantidade}')
print(f'troco de R$ {troco}')

