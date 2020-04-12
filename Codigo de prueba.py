while True:
    try:
        Dimension = int(input('Por favor ingresa la dimension de tu tablero: '))
        break
    except(TypeError, ValueError):
        print('Hey! Eso no es un numero.\nIntentalo otra vez.')
