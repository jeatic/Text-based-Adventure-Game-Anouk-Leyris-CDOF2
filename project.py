import time

def introduction():
    print("Bienvenue dans l'aventure textuelle !")
    time.sleep(1)
    print("Vous vous trouvez au début de votre aventure.")
    time.sleep(1)
    print("Faites des choix pour définir l'issue de votre histoire.")

def make_choice(choices):
    print("Choix disponibles:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice_num = int(input("Choisissez un numéro : "))
            if 1 <= choice_num <= len(choices):
                return choice_num
            else:
                print("Veuillez choisir un numéro valide.")
        except ValueError:
            print("Veuillez entrer un numéro.")

def forest_adventure():
    print("Vous vous trouvez dans une forêt sombre.")
    time.sleep(1)
    print("Vous entendez des bruits étranges autour de vous.")

    choices = ["Explorer la forêt plus en profondeur.", "Allumer une torche.", "Appeler à l'aide."]
    choice = make_choice(choices)

    if choice == 1:
        print("Vous rencontrez une créature mystérieuse dans la forêt.")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("Fin de l'aventure.")
    elif choice == 2:
        print("La torche éclaire votre chemin, révélant des indices cachés.")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("Fin de l'aventure.")
    elif choice == 3:
        print("Vous appelez à l'aide, mais personne ne répond.")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("Fin de l'aventure.")
    else:
        print("Quelque chose a mal tourné.")

def main():
    introduction()
    forest_adventure()

if __name__ == "__main__":
    main()
