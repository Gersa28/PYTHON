import random

def choose_options():
    """
    Solicita al usuario que elija entre piedra, papel o tijera.
    Devuelve la opción del usuario y la opción generada aleatoriamente por la computadora.
    """
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if user_option not in options:
        print('Opción no válida.')
        return None, None

    computer_option = random.choice(options)

    print('Opción del usuario =>', user_option)
    print('Opción de la computadora =>', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    """
    Verifica las reglas del juego y determina el ganador de la ronda.
    Actualiza los conteos de victorias del usuario y de la computadora.
    """
    if user_option == computer_option:
        print('¡Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('¡El usuario gana!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('¡La computadora gana!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('¡El usuario gana!')
            user_wins += 1
        else:
            print('Tijera gana a papel')
            print('¡La computadora gana!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('¡El usuario gana!')
            user_wins += 1
        else:
            print('Piedra gana a tijera')
            print('¡La computadora gana!')
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    """
    Ejecuta el juego de piedra, papel o tijera.
    El juego continúa hasta que uno de los jugadores alcanza 2 victorias.
    """
    computer_wins = 0
    user_wins = 0  
    rounds = 1
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('Victorias de la computadora:', computer_wins)
        print('Victorias del usuario:', user_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        if user_option is None:  # Si el usuario ingresó una opción no válida
            continue

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print('El ganador es la computadora')
            break

        if user_wins == 2:
            print('El ganador es el usuario')
            break

run_game()
