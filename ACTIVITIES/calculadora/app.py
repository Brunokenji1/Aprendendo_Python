
def calcular():
    try: 
        operacoes = '+-/*'
        n1 = int(input('Digite o primeiro número: '))
        opcao = input('Escolha a operação (+, -, *, /): ')

        if opcao not in operacoes:
            print('Erro: Digite uma operação matematica valida')  
        else:
            n2 = int(input('Digite o segundo número: '))
            if n1 == 0 or n2 == 0:
                print('Divisão por zero não é permitida')
            else:
                res = 0
                if opcao in operacoes:
                    match opcao:
                        case '+':
                            res = n1+n2
                        case '-':
                            res = n1-n2
                        case '*':
                            res = n1*n2
                        case '/':
                            res = n1/n2
                print(f'Resultado = {res}')      
                
    except ValueError:
        print('Erro: Entrada inválida. Digite apenas números.')

def main():
    calcular()
    
if __name__ == '__main__':
    main()