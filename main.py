from random import choice

#opcion seleccionada por el Usuario
user_option = input('Realice su elección: piedra, papel o tijera ->')
#print(type(user_option))
user_option_lower = user_option.lower()

#opcion seleccionada por el compurador 
options = ['piedra','papel','tijera']
computer_option = choice(options)
print('El computador eligió ', computer_option)

if user_option_lower == computer_option:
    print('Empate!')
elif user_option_lower == 'piedra':
    if computer_option == 'tijera':
        print('piedra gana a tijera')
        print('Usuario ganó!')
    else:
        print('papel gana a piedra')
        print('Computador ganó!')
elif user_option_lower == 'papel':
    if computer_option == 'tijera':
        print('tijera gana a papel')
        print('Computador ganó!')
    else:
        print('papel gana a piedra')
        print('Usuario ganó!')
elif user_option_lower == 'tijera':
    if computer_option == 'papel':
        print('tijera gana a papel')
        print('Usuario ganó!')
    else:
        print('piedra gana a tijera')
        print('Computador ganó!')