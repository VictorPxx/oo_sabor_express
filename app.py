from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_soares = Restaurante(nome='Soares Lanches', categoria='Hamburgueria')
cachorro_quente = Prato('Cachorro Quente', 6.0, 'O mais tradicional')
suco_graviola = Bebida('Suco de Graviola', 4.0, 'grande')

restaurante_soares.adicionar_item_no_cardapio(cachorro_quente)
restaurante_soares.adicionar_item_no_cardapio(suco_graviola)

def main():
    restaurante_soares.exibir_cardapio

if __name__ == '__main__':
    main()