import random

def gerar_numero_aleatorio():
    '''Metodo que gera um numero aleatorio entre 1-100'''
    numero_aleatorio = random.randint(1,100)
    return numero_aleatorio

def adivinhar_numero(numero_aleatorio, chute, qtd_chutes):
    '''Metodo que vai verificar se o chute que o usuário informou é maior, menor ou igual ao numero gerado aleatoriamente'''
    try:
        if numero_aleatorio > chute:
            print('Muito baixo! ')
            print()
            chute = int(input('Tente novamente:'))
            qtd_chutes += 1
            adivinhar_numero(numero_aleatorio, chute, qtd_chutes)

        elif numero_aleatorio < chute:
            print('Muito alto!')
            print()
            chute = int(input('Tente novamente:'))
            qtd_chutes += 1
            adivinhar_numero(numero_aleatorio, chute, qtd_chutes)
            
        else:
            print(f'\nParabéns! Você acertou o número {numero_aleatorio}')
            print(f'A quantidades de chutes foi {qtd_chutes}')
        
    except ValueError as e:
        print(f'Entrada inválida: {e}')

def main():
    try:
        numero_aleatorio = gerar_numero_aleatorio()
        chute = int(input('Tente adivinhar o número (1-100): '))
        adivinhar_numero(numero_aleatorio, chute, 1)
    except ValueError as e:
        print(f'Entrada inválida: {e}')

if __name__ == '__main__':
    main()