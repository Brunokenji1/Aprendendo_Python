import random

def gerar_senha():
    '''Metodo que cria senhas aleatorias'''
    maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '1234567890'
    especiais = '!@#$%&*ç'
    senha = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiais),
    ]
    todos_caracteres = maiusculas + minusculas + numeros + especiais
    senha.extend(random.choices(todos_caracteres, k=8))
    random.shuffle(senha)
    return ''.join(senha)

def main():
    senha_gerada = gerar_senha()
    print(f' Senha gerada: {senha_gerada}')

if __name__ == '__main__':
    main()