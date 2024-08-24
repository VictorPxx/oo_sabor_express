from modelos.restaurante import Restaurante

restaurante_1 = Restaurante(nome='Soares Lanches', categoria='Hamburgueria')
restaurante_2 = Restaurante(nome='WR', categoria='Pizzaria')

restaurante_1.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
