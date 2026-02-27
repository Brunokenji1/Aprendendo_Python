from modelos.restaurante import Restaurante

restaurante_catelinho = Restaurante('catelinho', 'comida caseira')
restaurante_pizza = Restaurante('pizza', 'pizzaria')

restaurante_catelinho.registrar_avaliacao('bruno', 10)
restaurante_catelinho.registrar_avaliacao('lucas', 8)
restaurante_catelinho.registrar_avaliacao('pedro', 6)
restaurante_pizza.registrar_avaliacao('bruno', 8)
restaurante_catelinho.alternar_estado()


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()