import random


def jugar():  #Función Principal
    usuario = input("Escoje una opción: 'pi' para piedra, 'pa' para papel, 'ti', para tijera.\n").lower()
    compu = random.choice(['pi', 'pa', 'ti'])

    if usuario == compu:
        return '¡Emmpate!'
    
    if ganó_el_jugador(usuario, compu):
        return '¡Ganaste!'
    
    return '¡Perdiste!'


def ganó_el_jugador(jugador, oponente):
    #Retornar True si gana el jugador.
    #Piedra gana a Tijera (pi > ti)
    #Tijera gana a Papel (ti > pa)
    #Papel gana a Piedra (pa > pi)
    if  ((jugador == 'pi' and oponente == 'ti' )
         or(jugador == 'ti' and oponente == 'pa')
         or(jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False 


print(jugar())