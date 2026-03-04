import random

def jotenpo(escolha):
    '''Jogo de pedra, papel e tesoura'''
    
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_usuario = escolha.lower()
    escolha_computador = random.choice(opcoes)
    
    if escolha_usuario not in opcoes:
        return print('Digite uma opção entre PEDRA, PAPEL OU TESOURA')
    
    if escolha_usuario == escolha_computador:
        print('O jogo ficou empatado')
        print(f'Sua escolha foi: {escolha_usuario}')
        print(f'A escolha do computador foi: {escolha_computador}')

    elif escolha_computador == 'pedra' and escolha_usuario == 'papel' or escolha_computador == 'papel' and escolha_usuario == 'tesoura' or escolha_computador == 'tesoura' and escolha_usuario == 'pedra':
        print('Você ganhou!!')
        print(f'Sua escolha foi: {escolha_usuario}')
        print(f'A escolha do computador foi: {escolha_computador}')

    else:
        print('Você perdeu!!')
        print(f'Sua escolha foi: {escolha_usuario}')
        print(f'A escolha do computador foi: {escolha_computador}')

def main():
    escolha = input('Escolha: pedra, papel ou tesoura? ')
    jotenpo(escolha)

if __name__ == '__main__':
    main()