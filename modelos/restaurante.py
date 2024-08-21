class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Soares Lanches'
restaurante_praca.categoria = 'Lanchonete'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Tarantella'
restaurante_pizza.categoria = 'Pizzaria'

restaurantes = [restaurante_praca, restaurante_pizza]