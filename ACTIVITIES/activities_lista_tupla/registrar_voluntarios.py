def registrar_voluntario(lista_voluntarios):
    nome_voluntario = input("Digite o nome do Coluntário (ou 'sair' para encerrar): ")
    if nome_voluntario == 'sair':
        print('\n voluntários registrados: ', lista_voluntarios)
    else:
        lista_voluntarios.append(nome_voluntario)
        registrar_voluntario(lista_voluntarios)

def main():
    lista_voluntarios = []
    registrar_voluntario(lista_voluntarios)

if __name__ == '__main__':
    main()