class Restaurante:
    
    restaurantes = []
    
    def __init__(self, nome='', categoria=''):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self.nome} {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo}')
    
restaurante_1 = Restaurante(nome='Soares Lanches', categoria='Hamburgueria')
restaurante_2 = Restaurante(nome='WR', categoria='Pizzaria')

Restaurante.listar_restaurantes()