from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    
    restaurantes = []
    
    def __init__(self, nome='', categoria=''):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)
        return media
    
    def adicionar_item_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property        
    def exibir_cardapio(self):
        print(f'Cardápio do Restaurante {self._nome}')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome.ljust(20)} |  Preço: {str(item._preco).ljust(5)} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome.ljust(20)} |  Preço: {str(item._preco).ljust(5)} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
            