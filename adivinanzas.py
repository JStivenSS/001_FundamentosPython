import random
opcion = 'si'

while opcion == 'si':
    # limpiar la consola de comandos
    print('\n' * 100)
    adivinanzas = {
        'una estrella': 'Aunque soy pequeño y en la noche brillante, soy una luz en el cielo, ¿qué soy?',
        'una papa': 'Soy un tubérculo que se come frito, ¿qué soy?',
        'un reloj': 'Tengo manecillas y no soy una persona, ¿qué soy?',
        'un huevo': 'Soy blanco por dentro, amarillo por fuera, ¿qué soy?',
        'batman': 'Soy un superhéroe que no tiene superpoderes, ¿quién soy?',
        'un perro': 'Soy el mejor amigo del hombre, ¿qué soy?',
        'un gato': 'Soy un animal que tiene 7 vidas, ¿qué soy?',
        'hachiko': 'Soy un perro que esperó a su dueño por 10 años, ¿quién soy?'
    }

    respuestas = ('una estrella', 'una papa', 'un reloj', 'un huevo',
                  'batman', 'un perro', 'un gato', 'hachiko')
    respuesta = random.choice(respuestas)
    adivinanza = adivinanzas[respuesta]

    usuario = input(f'{adivinanza}: ')
    usuario = usuario.lower()

    if usuario == respuesta:
        print('¡Felicidades, has ganado!')
        opcion = input('Quieres volver a intentarlo? ')
    else:
        print('¡Lo siento, has perdido!')
        opcion = input('Quieres volver a intentarlo? ')
