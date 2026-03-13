lista_estoque = []

estoque1 = input('Produtos do estoque 1 (separados por vírgula): ').split(',')
estoque2 = input('Produtos do estoque 2 (separados por vírgula): ')
lista_estoque += estoque1
lista_estoque += estoque2.split(',')
print(lista_estoque)