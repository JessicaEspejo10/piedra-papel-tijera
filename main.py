from random import choice

#opcion seleccionada por el Usuario
user_option = input("Realice su elección: Piedra, papel o tijera ->")
#print(type(user_option))
user_option_upper = user_option.upper()

#opcion seleccionada por el compurador 
options = ["PIEDRA","PAPEL", "TIJERA"]
computer_option = choice(options)
print("El computador eligió ", computer_option)

if user_option_upper == computer_option:
    print("Empate!")
elif user_option_upper == "PIEDRA":
    if computer_option == "TIJERA":
        print("Piedra gana a tijera")
        print("Usuario ganó!")
    else:
        print("Papel gana a piedra")
        print("Computador ganó!")
elif user_option_upper == "PAPEL":
    if computer_option == "TIJERA":
        print("Tijera gana a papel")
        print("Computador ganó!")
    else:
        print("Papel gana a piedra")
        print("Usuario ganó!")
elif user_option_upper == "TIJERA":
    if computer_option == "PAPEL":
        print("Tijera gana a papel")
        print("Usuario ganó!")
    else:
        print("Piedra gana a tijera")
        print("Computador ganó!")