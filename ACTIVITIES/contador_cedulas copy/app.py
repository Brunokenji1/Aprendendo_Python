def contador_cedulas(valor):
    try:
        lista_notas = [0, 0, 0, 0, 0, 0, 0]
        lista_cedul = [200, 100, 50, 20, 10, 5, 2]
        valor = int(valor)
        if valor % 2 == 1:
            print('Digite um numero par')
        if valor >= 200:
            valor-=200
            lista_notas[0] += 1
            contador_cedulas(valor)
        if valor >= 100:
            valor -= 100
            lista_notas[1] += 1
            contador_cedulas(valor)
        if valor >= 50:
            valor -= 50
            lista_notas[2] += 1
            contador_cedulas(valor)
        if valor >= 20:
            valor -= 20
            lista_notas[3] += 1
            contador_cedulas(valor)
        if valor >= 10:
            valor -= 10
            lista_notas[4] += 1
            contador_cedulas(valor)
        if valor >= 5:
            valor -= 5
            lista_notas[5] += 1
            contador_cedulas(valor)
        if valor >= 2:
            valor -= 2
            lista_notas[6] += 1
            contador_cedulas(valor)
 
        cont = 0
        for cedula in lista_cedul:

            print(f'{lista_notas[cont]} de R$ {cedula}')
            cont += 1
    except ValueError:
        print('Digite um numero')
def main():
    try:

        valor = int(input('Digite o valor do saque: '))

        contador_cedulas(valor)
    except ValueError:
        print('Digite um numero')
if __name__ == '__main__':
    main()