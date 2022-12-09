import utils

if __name__ == '__main__':
    rounds = 1
    user_win =0
    pc_win = 0
    flag = True

    while flag == True:
            
        print('-' * 50)
        print('Ronda No. ',rounds)
        print('-' * 50,'\n \n')
            
        user_option_lower, computer_option = utils.choose_options()

        if not user_option_lower == None:

            user_win, pc_win = utils.check_rules(user_option_lower, computer_option, user_win, pc_win )

            print('\n\n   Resultados parciales:')
            print(f'   - El usuario ha ganado {user_win} partidas')
            print(f'   - El computador ha ganado {pc_win} partidas')
                    
            flag = utils.final_results(rounds, user_win, pc_win, flag)
                    
            rounds +=1
