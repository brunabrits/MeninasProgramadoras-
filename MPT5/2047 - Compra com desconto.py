valor_produto = float (input())
desconto = float(input())

desconto = desconto /100
valor_produto_economizado = valor_produto * desconto 
valor_produtoT = valor_produto - valor_produto_economizado

print('{:.2f}'.format (valor_produto))
print('{:.2f}'.format (valor_produtoT))
print('{:.2f}'.format (valor_produto_economizado))
