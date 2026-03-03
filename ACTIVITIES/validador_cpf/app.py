def validar_cpf(cpf):
    try:
        
        if len(cpf) != 11:
            print('O cpf precisa ter 11 digitos')
        else: 
            for i, numero in enumerate(cpf): 
                numero_int = int(numero) 
    except ValueError:
        print('Erro: O CPF deve conter apenas números')

def main():
    cpf = input('Digite seu cpf: ')
    validar_cpf(cpf)

if __name__ == '__main__':
    main()