import time

def introduction():
    print("Welcome to the text adventure!")
    time.sleep(1)
    print("You find yourself at the beginning of your journey.")
    time.sleep(1)
    print("Make choices to determine the outcome of your story.")

def create_question(question, choices):
    print(question)
    time.sleep(1)
    print("Available choices:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    try:
    choice_num = int(input("Choose a number: "))
    if 1 <= choice_num <= len(choices):
        return choice_num
    else:
        print("Please choose a valid number.")
    except ValueError:
    print("Please enter a number.")

def encounter_creature():
    print("You encounter a mysterious creature in the forest.")
    time.sleep(1)
    print("...")
    time.sleep(2)

def use_torch():
    print("The torch illuminates your path.")
    time.sleep(1)
    print("...")
    time.sleep(2)

def eaten():
    print("The creature is actually a werewolf. Tonight being a full moon, it attacks and eats you.")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("End of the adventure.")
    exit_game()

def run():
    print("You flee, but the absence of light makes you miss the root on the ground. You stumble. Slowly, the creature approaches you and eventually devours you.")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("End of the adventure.")
    exit_game()

def run2():
    print("You run away, but in haste, you miss the root on the ground. You stumble. Slowly, the creature approaches you and eventually devours you.")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("End of the adventure.")
    exit_game()

def left():
    print("You arrive on a road. You come across a well-maintained house, but it seems uninhabited.")
    time.sleep(1)
    print("...")
    time.sleep(2)

def right():
    print("You venture deeper into the forest following the noises. Suddenly, the monster appears in front of you. You wield your torch to scare it, you're ready.")
    time.sleep(1)
    print("...")
    time.sleep(2)

def turn_back():
    print("You turn back and return to the forest. What the story hides from us is that by making these kinds of decisions, you will never get out of here.")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("End of the adventure.")
    exit_game()

def surprise():
    print("You enter the house. Suddenly the lights come on, and you see about ten people shouting 'Happy Birthday!!!'. Was all of this just a setup? And what about the noises from the right path? You will find out, one day...")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("End of the adventure.")
    exit_game()

def win():
    print("You throw the torch at the werewolf. It catches fire and flees into the forest. You've won!")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Victory, for now...")
    exit_game()

def exit_game():
    print("Thanks for playing!")
    exit()

def forest_adventure():
    question_text = "You find yourself in a dark forest. You hear strange noises around you."
    choices = ["Explore the forest further.", "Light a torch."]
    
    choice = create_question(question_text, choices)

    if choice == 1:
        encounter_creature()
        question_text = "You can barely make out the creature, but it seems to be your size. What do you do?"
        choices = ["Approach.", "Light a torch.", "Run away."]
        choice = create_question(question_text, choices)
        if choice == 1:
            eaten()
        if choice == 2:
            use_torch()
            question_text = "You realize the creature is actually a werewolf. What do you do?"
            choices = ["Attack it", "Run away"]
            choice = create_question(question_text, choices)
            if choice == 1:
                win()
            if choice == 2:
                run2()
        if choice == 3:
            run()
    elif choice == 2:
        use_torch()
        question_text = "The edge of the forest is far now. You are on a path, and it eventually splits. Noises seem to come from the right one, but it's impossible to know if they are friendly or hostile. What do you do?"
        choices = ["Go left.", "Go right.", "Turn back."]
        choice = create_question(question_text, choices)
        if choice == 1:
            left()
            question_text = "Your fate (your life?) is in your hands. What do you do?"
            choices = ["Enter the house.", "Turn back."]
            choice = create_question(question_text, choices)
            if choice == 1:
                surprise()
            if choice == 2:
                turn_back()
        if choice == 2:
            right()
            question_text = "It's time to make the most important choice of your life!"
            choices = ["Confront the beast.", "Turn back."]
            choice = create_question(question_text, choices)
            if choice == 1:
                win()
            if choice == 2:
                run2()
        if choice == 3:
            turn_back()
    else:
        print("Something went wrong.")

def main():
    introduction()
    forest_adventure()

if __name__ == "__main__":
    main()
