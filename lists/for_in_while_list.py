carrinho = []
produto =''

while produto != 'sair':
  print("Adicione um produto na lista ou digite 'sair' para encerrar:")
  produto = input()
  if produto != 'sair':
    carrinho.append(produto)

for produto in carrinho:
  print(produto)
