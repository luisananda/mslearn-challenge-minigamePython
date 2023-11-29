#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

def obtener_opcion_jugador():
    opcion = input("Elige piedra, papel o tijera: ").lower()
    while opcion not in ['piedra', 'papel', 'tijera']:
        print("Opción inválida. Intenta de nuevo.")
        opcion = input("Elige piedra, papel o tijera: ").lower()
    return opcion

def determinar_ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (
        (jugador1 == 'piedra' and jugador2 == 'tijera') or
        (jugador1 == 'tijera' and jugador2 == 'papel') or
        (jugador1 == 'papel' and jugador2 == 'piedra')
    ):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"

def jugar_piedra_papel_tijera():
    puntuacion_jugador1 = 0
    puntuacion_jugador2 = 0

    while True:
        print(f"\nPuntuación actual - Jugador 1: {puntuacion_jugador1}, Jugador 2: {puntuacion_jugador2}")
        print("¡Bienvenido al juego de piedra, papel y tijera!")
        jugador1 = obtener_opcion_jugador()
        jugador2 = obtener_opcion_jugador()

        print(f"Jugador 1 elige {jugador1}")
        print(f"Jugador 2 elige {jugador2}")

        resultado = determinar_ganador(jugador1, jugador2)
        print(resultado)

        if resultado == "Jugador 1 gana":
            puntuacion_jugador1 += 1
        elif resultado == "Jugador 2 gana":
            puntuacion_jugador2 += 1

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_nuevamente != 's':
            break

    print(f"\nJuego terminado. Puntuación final - Jugador 1: {puntuacion_jugador1}, Jugador 2: {puntuacion_jugador2}")
    if puntuacion_jugador1 > puntuacion_jugador2:
        print("¡Jugador 1 es el ganador!")
    elif puntuacion_jugador2 > puntuacion_jugador1:
        print("¡Jugador 2 es el ganador!")
    else:
        print("¡El juego terminó en empate!")

# Llamamos a la función principal para iniciar el juego
jugar_piedra_papel_tijera()