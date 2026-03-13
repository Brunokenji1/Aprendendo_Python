lista_convidados = ['bruno', 'pedro', 'daniel']
print('Lista atual de convidados: ', lista_convidados )
convidado = input('Digite o nome do novo convidado: ')
posicao = int(input('Digite a posição na qual deseja inserir o convidado: '))
lista_convidados.insert(posicao, convidado)
print('Lista atualizada de convidados: ', lista_convidados)