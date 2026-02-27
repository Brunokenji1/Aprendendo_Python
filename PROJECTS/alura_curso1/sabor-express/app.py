import os
restaurantes = [{'nome': 'Izo', 'categoria':'Gastrobar', 'ativo': True}, 
                {'nome': 'Champignon', 'categoria':'Pizza', 'ativo': True},
                {'nome': 'MC', 'categoria': 'Fastfood', 'ativo': False}]


def exibir_nome_do_programa():
    '''Exibi o nome estilizado do aplicativo na tela'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗███╗░░██╗███████╗██████╗░░██████╗░███████╗████████╗██╗░█████╗░░█████╗░
██╔════╝████╗░██║██╔════╝██╔══██╗██╔════╝░██╔════╝╚══██╔══╝██║██╔══██╗██╔══██╗
█████╗░░██╔██╗██║█████╗░░██████╔╝██║░░██╗░█████╗░░░░░██║░░░██║██║░░╚═╝██║░░██║
██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██║░░╚██╗██╔══╝░░░░░██║░░░██║██║░░██╗██║░░██║
███████╗██║░╚███║███████╗██║░░██║╚██████╔╝███████╗░░░██║░░░██║╚█████╔╝╚█████╔╝
╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░╚════╝░░╚════╝░
      """)
    
def exibir_opcoes():
    '''Exibi as opções disponíveis do menu principal'''
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Alternar estado restaurante")
    print("4 - Sair \n")

def voltar_menu_principal():
    '''Solicita uma tecla para voltar ao menu principal
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    '''Exibe um subtítulo estilizado na tela
    
    Inputs:
    - texto: str - o texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f'{texto}')
    print(linha)
    print()

def finalizar_app():
    '''Exibe mensagem de finalização do aplicativo'''
    exibir_subtitulo('Finalizando o app')

def opcao_invalida():
    '''Exibe mensagem de opção inválida e retorna ao menu principal
    Outputs:
    - Retorna ao menu principal
    '''
    print('opção inválida')
    opcao = input('Digite 1 - para voltar  ou  2 - para terminar')
    if(opcao == 1 or opcao == '1'):
        voltar_menu_principal()

    else:
        print('fim')

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''

    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_menu_principal()

def listar_restaurantes():
    '''Lista os restaurantes presentes na lista
    
    Outputs:
    -Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
    voltar_menu_principal()

def alternar_estado_restaurante():
    '''Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    
    nome_restaurante = input('Digite o nome do restaureante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_menu_principal()


def escolher_opcao():
    '''Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        print('Digite uma opção valida')

def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao ()

if __name__== '__main__':
    main()
