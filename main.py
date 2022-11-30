from random import choice

def choose_options():
    options = ('piedra','papel','tijera')
    #opcion seleccionada por el compurador 
    computer_option = choice(options)
    
    #opcion seleccionada por el Usuario
    user_option = input('Por favor ingrese su elección: piedra, papel o tijera ->')
    user_option_lower = user_option.lower()
    print('\n')

    if not user_option_lower in options:
        print('La opción que ingresó no es válida\n\n')
        return None, computer_option
    else:
        #imprimir elecciones de usuarios
        print('Usted eligió -> ', user_option_lower)
        print('El computador eligió ->', computer_option)    
    
    return user_option_lower, computer_option

def check_rules(user_option_lower, computer_option, user_win, pc_win ):
    if user_option_lower == computer_option:
        print('Empate!')
        
    elif user_option_lower == 'piedra':
        if computer_option == 'tijera':
            print('Piedra le gana a tijera')
            print('Punto para el usuario!')
            user_win += 1
        else:
            print('Papel gana a piedra')
            print('Punto para el computador!')
            pc_win += 1
    elif user_option_lower == 'papel':
        if computer_option == 'tijera':
            print('tijera gana a papel')
            print('Punto para el computador!')
            pc_win += 1
        else:
            print('papel gana a piedra')
            print('Punto para el usuario!')
            user_win += 1
    elif user_option_lower == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('Punto para el usuario!')
            user_win += 1
        else:
            print('piedra gana a tijera')
            print('Punto para el computador!')
            pc_win += 1
    return user_win, pc_win

def final_results(rounds, user_win, pc_win, flag):

    if rounds == 3:
        if (user_win!= pc_win) & (user_win >= 2):
            print('\nESTE JUEGO HA TERMINADO!\nHA GANADO EL USUARIO!!\n\n')
            flag = False      
        elif (user_win!= pc_win) & (pc_win >= 2):
            print('\nESTE JUEGO HA TERMINADO!\nHA GANADO EL COMPUTADOR!!\n\n')
            flag = False
    elif rounds > 3:
        if user_win > pc_win:
            print('\nESTE JUEGO HA TERMINADO!\nHA GANADO EL USUARIO!!\n\n')
            flag = False
        elif user_win < pc_win:
            print('\nESTE JUEGO HA TERMINADO!\nHA GANADO EL COMPUTADOR!!\n\n')
            flag = False
    return flag

def run_game():
    rounds = 1
    user_win =0
    pc_win = 0
    flag = True

    while flag == True:
        
        print('-' * 50)
        print('Ronda No. ',rounds)
        print('-' * 50,'\n \n')
        
        user_option_lower, computer_option = choose_options()

        if not user_option_lower == None:

            user_win, pc_win = check_rules(user_option_lower, computer_option, user_win, pc_win )

            print('\n\n   Resultados parciales:')
            print(f'   - El usuario ha ganado {user_win} partidas')
            print(f'   - El computador ha ganado {pc_win} partidas')
                
            flag = final_results(rounds, user_win, pc_win, flag)
                
            rounds +=1

run_game()