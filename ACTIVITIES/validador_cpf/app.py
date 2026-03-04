def validar_cpf(cpf):
    '''
    02/03/2026
    Essa função no momento so verifica quantos caracteres tem o cpf informado 
    e verifica se não possui nenhuma letra

    Inputs:
    - cpf: str - o cpf informado pelo usuario 
    '''
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