import time
import random


def print_and_pause(statement):
    print(statement)
    time.sleep(2)


def is_valid(message, a, b):
    while True:
        s = input(message)
        if s == a or s == b:
            return s


def intro():
    print_and_pause("You find yourself standing in an open field, "
                    "filled with grass and yellow wildflowers.")
    enemy = random.choice(["dragon", "pirate", "troll",
                          "tiger", "lion", "gorgon", "wicked fairie"])
    print_and_pause(f"Rumor has it that a {enemy} is somewhere "
                    "around here, and has been terrifying the nearby village.")
    print_and_pause("In front of you is a house.")
    print_and_pause("To your right is a dark cave.")
    print_and_pause("In your hand you hold your trusty"
                    " (but not very effective) dagger.")
    print()
    hasWeapon = []
    start(hasWeapon)


def start(hasWeapon):
    print_and_pause("Enter 1 to knock on the door of the house.")
    print_and_pause("Enter 2 to peer into the cave.")
    print_and_pause("What would you like to do?")
    choice = is_valid("(Please enter 1 or 2.)\n", '1', '2')
    enemy = random.choice(["dragon", "pirate", "troll",
                          "tiger", "lion", "gorgon", "fairie"])
    weapon = random.choice(['Sword', 'Hammer', 'Axe', 'Gun'])
    if choice == '1':
        enter_house(enemy, weapon, hasWeapon)
    else:
        enter_cave(weapon, hasWeapon)


def enter_house(enemy, weapon, hasWeapon):
    print_and_pause("You approach the door of the house.")
    print_and_pause(f"Your are about to knock when the door"
                    f" opens and out steps a {enemy}.")
    print_and_pause(f"Eep! This is the {enemy}'s house!")
    print_and_pause(f"The {enemy} attacks you!")
    if 1 not in hasWeapon:
        print_and_pause("You feel a bit under-prepared for this,"
                        " what with only having a tiny dagger.")
    fight = is_valid("Would you like to (1) fight"
                     " or (2) run away?\n", '1', '2')
    if fight == '1':
        if 1 not in hasWeapon:
            print_and_pause("You do your best...")
            print_and_pause(f"but the dagger is no match for the {enemy}.")
            print_and_pause("You have been defeated!")
        else:
            print_and_pause(f"As the {enemy} moves to attack"
                            f",you unsheath your new {weapon}.")
            print_and_pause(f"The {weapon} of Ogoroth shines brightly in your"
                            " hand as you brace yourself for the attack.")
            print_and_pause(f"but the {enemy} takes look at"
                            " your shiny new toy and runs away!")
            print_and_pause("You have rid the town of the"
                            " pirate. You are victorious!")
        play_again = is_valid("Would you like to play"
                              " again? (y/n)\n", 'y', 'n')
        if play_again == 'y':
            print_and_pause("Excellent! Restarting the game ...")
            print()
            intro()
        else:
            print_and_pause("Thanks for playing! see you next time.")
    else:
        print_and_pause('Running Back to field!')
        start(hasWeapon)


def enter_cave(weapon, hasWeapon):
    print_and_pause("You peer cautiously into the cave.")
    if 1 in hasWeapon:
        print_and_pause("You've been here before, and gotten all"
                        " the good stuff. It's just an empty cave now.")
    else:
        print_and_pause("It turns out to be only a very small cave.")
        print_and_pause("Your eye catches a glint of metal behind a rock.")
        print_and_pause(f"You have found the magical {weapon} of Ogoroth!")
        print_and_pause(f"You discard your silly old dagger and"
                        f" take the {weapon} with you.")
        hasWeapon.append(1)
    print_and_pause("You walk back out to the field.")
    print()
    start(hasWeapon)


intro()
