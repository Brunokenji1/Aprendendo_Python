def titulo(texto):
    '''Função que formata o titulo de Titulo'''
    qtd_letras = len(texto)
    print()
    print('*'*qtd_letras)
    print(texto)
    print('*'*qtd_letras)

def adicionar_tarefa(lista_de_tarefas):
    texto = 'Adicionar uma tarefa'
    titulo(texto)
    tarefa_nova = input('Digite a nova tarefa: ')
    lista_de_tarefas.append(tarefa_nova)

def visualizar_tarefas(lista_de_tarefas):
    texto = 'Visualizar todas as tarefas cadastradas'
    titulo(texto)
    for i, tarefa in enumerate(lista_de_tarefas):
        print(f'{i} - {tarefa}')

def remover_tarefa(lista_de_tarefas):
    try:
        texto = 'Remover tarefa da lista'
        titulo(texto)
        index = int(input('Digite o número da tarefa a ser removido: '))
        tarefa_excluida = lista_de_tarefas[index]
        lista_de_tarefas.pop(index)
        print(f'A tarefa "{tarefa_excluida}" foi removida')

    except ValueError:
        print('Digite um numero correspondente ao indice da tarefa a ser excluida')
    except IndexError:
        print('Digite um indice que exista')

def gerencia_menu(opcao, lista_de_tarefas):
    match opcao:
        case '1':
            adicionar_tarefa(lista_de_tarefas)
            menu(lista_de_tarefas)
        case '2':
            visualizar_tarefas(lista_de_tarefas)
            menu(lista_de_tarefas)
        case '3':
            remover_tarefa(lista_de_tarefas)
            menu(lista_de_tarefas)
        case '4':
            print("Fim")
        case _:
            print('Erro: Entrada inválida! Digite um número.')

def menu(lista_de_tarefas):
    titulo('Menu')
    print('1. Adicionar tarefa')
    print('2. Visualizar tarefas ') 
    print('3. Remover tarefa ')
    print('4. Sair')
    opcao = input('Escolha uma opção: ')

    gerencia_menu(opcao, lista_de_tarefas)


def main():
    lista_de_tarefas = []
    menu(lista_de_tarefas)

if __name__ == '__main__':
    main()