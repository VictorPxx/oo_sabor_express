from modelos.restaurante import Restaurante

restaurante_1 = Restaurante(nome='Soares Lanches', categoria='Hamburgueria')

restaurante_1.receber_avaliacao('Victor', 8)
restaurante_1.receber_avaliacao('Flávia', 6)
restaurante_1.receber_avaliacao('Lavínia', 10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()