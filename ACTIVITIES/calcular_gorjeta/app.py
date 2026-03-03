def calcular_gorjeta():
    try:
        valor_conta = float(input('Digite o valor da conta: '))
        porcentagem_gorjeta = float(input('Digite a porcentagem de gorjeta: '))
        valor_gorjeta = valor_conta * (porcentagem_gorjeta/100)
        valor_novo = valor_conta + valor_gorjeta
        print(f'Valor da gorjeta: ${valor_gorjeta:.2f}')
        print(f'Total a pagar: ${valor_novo:.2f}')
        
    except ValueError:
        print('Digite numeros')

def main():
    calcular_gorjeta()

if __name__ == '__main__':
    main()