from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida


restaurante_comida = Restaurante('catelinho', 'comida caseira')
restaurante_pizza = Restaurante('pizza', 'pizzaria')

bebida_suco = Bebida('Suco de limão', 5.00, 'grande')
bebida_suco.aplicar_desconto()
prato_lasanha = Prato('lasanha', 34.00, 'A melhor lasanha')
prato_lasanha.aplicar_desconto()

restaurante_comida.adicionar_no_cardapio(bebida_suco)
restaurante_comida.adicionar_no_cardapio(prato_lasanha)

def main():
    restaurante_comida.exibir_cardapio

if __name__ == '__main__':
    main()