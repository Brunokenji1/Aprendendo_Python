from modelos.avaliacao import Avaliacao

class Restaurante:
    '''Representa um restaurante e suas características.'''
    restaurantes = []
    def __init__(self, nome, categoria):
        '''
        Inicializa uma instância de Restaurante.
        
        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        '''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False  # com o _ antes transforma em private
        self._avaliacoes = []

        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Retorna uma representação em string do restaurante.'''
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        '''Exibe uma lista formatada de todos os restaurantes.'''
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)} | {'Avaliação'}')
        for restaurante in cls.restaurantes:  #before: for restaurante in Restaurante.restaurantes
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)}| {str(restaurante.media_avaliacoes).ljust(25)}')
    
    @property
    def ativo(self):
        '''Retorna um símbolo indicando o estado de atividade do restaurante'''
        return '✅' if self._ativo else '❎'
    
    def alternar_estado(self): 
        '''Alterna o estado de atividade do restaurante.'''
        self._ativo = not self._ativo
    
    def registrar_avaliacao(self, nome, nota):
        '''
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação
        - nota (float)> A nota atribuída ao restaurante (entre 1 e 5)
        '''
        if 0 < nota < 5:
            avalicao = Avaliacao(nome, nota)
            self._avaliacoes.append(avalicao)
    
    @property
    def media_avaliacoes(self):
        '''Calcula e retorna a média das avaliações do restaurante.'''
        if not self._avaliacoes:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_de_notas = len(self._avaliacoes)
        media = round(soma_das_notas/quantidade_de_notas, 1)
        return media
    
    
# restaurante_izo = Restaurante('izo', 'GastroBar')
# restaurante_izo.alternar_estado()
# restaurante_champignon = Restaurante('Champignon', 'Pizzaria')

# restaurantes = [restaurante_izo, restaurante_champignon]


# print(dir(restaurantes))            #exibe todos os atributos, metodos, etc.
# print(vars(restaurantes))           #exibe os atributos em um dicionario]

# print(vars(restaurante_izo))            #{'nome': 'Izo', 'categoria': 'GastroBar', 'ativo': False}
# print(vars(restaurante_champignon))     #{'nome': 'Champignon', 'categoria': 'Pizzaria', 'ativo': False}

# Após cria o metodo __str__
# print(restaurante_izo)                    #Izo | GastroBar
# print(restaurante_champignon)             #Champignon | Pizzaria

# Restaurante.listar_restaurantes()           #Izo | GastroBar | False
                                            #Champignon | Pizzaria | False
