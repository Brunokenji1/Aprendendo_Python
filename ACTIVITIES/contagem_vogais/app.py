def contador_vogais(texto):
    '''Verifica quantas vogais tem no texto que o usuário enviou'''
    vogais = 'aeiouáéíóúâêîôûãõàèìòù'
    soma_vogais=0
    for vogal in vogais:
        soma_vogais += texto.count(vogal).lower()
    return soma_vogais


def main():
    texto = input("Digite um texto: ")
    quantidade_vogais = contador_vogais(texto)
    print(f'O texto contém {quantidade_vogais} vogais.')


if __name__ == '__main__':
    main()