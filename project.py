import time

def introduction():
    print("Bienvenue dans l'aventure textuelle !")
    time.sleep(1)
    print("Vous vous trouvez au début de votre aventure.")
    time.sleep(1)
    print("Faites des choix pour définir l'issue de votre histoire.")

def create_question(question, choices):
    print(question)
    time.sleep(1)
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

def encounter_creature():
    print("Vous rencontrez une créature mystérieuse dans la forêt.")
    time.sleep(1)
    print("...")
    time.sleep(2)

def use_torch():
    print("La torche éclaire votre chemin.")
    time.sleep(1)
    print("...")
    time.sleep(2)

def eaten():
    print("La créature est en fait un loup-garou. Ce soir étant un soir de pleine lune, elle vous attaque et vous mange.")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Fin de l'aventure.")
    exit_game()

def run():
    print("Vous vous enfuyez, mais l'abscence de lumière vous fait manquer la racine au sol. Vous trébuchez. Lentement, la créature s'approche de vous, et finit par vous dévorer.")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Fin de l'aventure.")
    exit_game()

def run2():
    print("Vous vous enfuyez, mais dans la précipitation vous manquez la racine au sol. Vous trébuchez. Lentement, la créature s'approche de vous, et finit par vous dévorer.")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Fin de l'aventure.")
    exit_game()

def left():
    print("Vous arrivez sur une route. Vous tombez sur une maison en bon état, mais qui semble inhabitée.")
    time.sleep(1)
    print("...")
    time.sleep(2)

def right():
    print("Vous vous enfoncez dans la forêt en suivant les bruits. Soudain, le monstre surgit devant vous. Vous brandissez votre torche pour lui faire peur, vous êtes prêt.")
    time.sleep(1)
    print("...")
    time.sleep(2)

def turn_back():
    print("Vous faites demi-tour et retournez dans la forêt. Ce que l'histoire nous cache, c'est qu'en prenant ce genre de décisions, vous ne sortirez jamais d'ici.")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Fin de l'aventure.")
    exit_game()

def surprise():
    print("Vous entrez dans la maison. Soudain les lumières s'allument et vous voyez une dizaine de personnes vous crier 'Bon anniversaire !!!'. Tout cela n'était donc qu'une mise en scène ? Et qu'en est-il des bruits du chemin de droite ? Vous le saurez, un jour...")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Fin de l'aventure.")
    exit_game()

def win():
    print("Vous lancez la torche sur le loup-garou. Il prend feu et s'enfuit dans la forêt. Vous avez gagné !")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Gagné, pour l'instant...")
    exit_game()

def exit_game():
    print("Merci d'avoir joué !")
    exit()

def forest_adventure():
    question_text = "Vous vous trouvez dans une forêt sombre. Vous entendez des bruits étranges autour de vous."
    choices = ["Explorer la forêt plus en profondeur.", "Allumer une torche."]
    
    choice = create_question(question_text, choices)

    if choice == 1:
        encounter_creature()
        question_text = "Vous distinguez à peine la créature, mais elle semble faire votre taille. Que faites-vous ?"
        choices = ["S'approcher.", "Allumer une torche.", "S'enfuir."]
        choice = create_question(question_text, choices)
        if choice == 1:
            eaten()
        if choice == 2:
            use_torch()
            question_text = "Vous constatez que la créature est en fait un loup-garou. Que faites-vous ?"
            choices = ["L'attaquer", "S'enfuir"]
            choice = create_question(question_text, choices)
            if choice == 1:
                win()
            if choice == 2:
                run2()
        if choice == 3:
            run()
    elif choice == 2:
        use_torch()
        question_text = "La lisière de la forêt est loin maintenant. Vous êtes sur un chemin et ce dernier finit par se séparer. Des bruits semblent provenir de celui de droite, mais impossible de savoir s'ils sont amis ou ennemis. Que faites-vous ?"
        choices = ["Aller à gauche.", "Aller à droite.", "Faire demi-tour."]
        choice = create_question(question_text, choices)
        if choice == 1:
            left()
            question_text = "Votre destin (votre vie ?) est entre vos mains. Que faites-vous ?"
            choices = ["Entrer dans la maison.", "Faire demi-tour."]
            choice = create_question(question_text, choices)
            if choice == 1:
                surprise()
            if choice == 2:
                turn_back()
        if choice == 2:
            right()
            question_text = "Il est temps de faire le choix le plus important de votre vie !"
            choices = ["Confronter la bête.", "Faire demi-tour."]
            choice = create_question(question_text, choices)
            if choice == 1:
                win()
            if choice == 2:
                run2()
        if choice == 3:
            turn_back()
    else:
        print("Quelque chose a mal tourné.")

def main():
    introduction()
    forest_adventure()

if __name__ == "__main__":
    main()
