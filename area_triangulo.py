def run():
    altura = float(input('Escribe la altura del trándulo: '))
    base = float(input('Escribe la base del triángulo: '))
    area = str((base * altura)/2)
    print('El área del triángulo es: ' + area + ' unidades cuadradas')


if __name__ == '__main__':
    run()