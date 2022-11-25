user_option = input("Por favor ingrese: piedra, papel o tijera ->")
computer_option = "piedra"

if user_option == computer_option:
    print("Empate!")
elif user_option == "piedra":
    if computer_option == "tijera":
        print("Piedra gana a tijera")
        print("Usuario ganó!")
    else:
        print("Papel gana a piedra")
        print("Computador ganó!")
elif user_option == "papel":
    if computer_option == "tijera":
        print("Tijera gana a papel")
        print("Computador ganó!")
    else:
        print("Papel gana a piedra")
        print("Usuario ganó!")
elif user_option == "tijera":
    if computer_option == "papel":
        print("Tijera gana a papel")
        print("Usuario ganó!")
    else:
        print("Piedra gana a tijera")
        print("Computador ganó!")