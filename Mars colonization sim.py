def display_introduction():  # tells the user what to expect from the application
    print("You are put in charge of establishing a colony on Mars.")  # Player's role
    print("Your decision will determine the survival of both you and your comrades.")  # Player's goal


# gets a valid input from the user
def get_input(prompt='', valid_answers=''):
    inp = input(prompt)

    if not (inp in valid_answers):  # If input is not listed within the valid answers
        print()
        inp = get_input(prompt, valid_answers)  # will repeat function

    return inp


if __name__ == '__main__':
    isAlive, Playing = True, True

    display_introduction()  # Announces the introduction
    input("\nPress Enter...\n")
    while Playing:
        Health = 100  # The player's starting health

        print("where should you play set up your base?")  # The first decision
        baseLocation = get_input("1.Underground\n2.On the surface\n3.Don't make a base", "123")

        if baseLocation == '1':  # if the user picks the correct decision
            print("You and our crew find a safe spot on Mars to survive")
        else:  # if the players decision was wrong
            print("Your crew scatter due to the poor conditions of Mars")
            print("Though everyone survives, your left in bad conditions")
            Health -= 50  # Reduces health due to the player's decision

        input("\nPress Enter...\n")
        print("What is your plan for getting your food")  # The second decision
        foodSource = get_input("1.Scavenge for food\n2.Build a green-house\n3.Grow Mars native plants", "123")  # gets the user's input
        if foodSource == '2':  # If the decision was correct
            print("You have established a reliable food source for you and the rest of the colony")

        else:  # If the decision was wrong
            print("Your food supply dwindles in within a month.")
            print("Luckily the colony was sent extra rations, but not before infighting and cannibalism could occur")
            Health -= 50  # Reduces health due to the player's decision

        input("\nPress Enter...\n")
        if Health <= 0:  # checks if the player is dead
            isAlive = False

        else:  # plays the final scenario if the player is alive
            print("Homebase has asked you what vehicles they should send to the colony. What is your answer?")  # Final Decision
            vehicleType = get_input("1.pressurized vehicles\n2.Nissan\n3.We don't need vehicles", "123")  # gets the user's input

            if vehicleType == '1':  # if the decision was correct
                print("the colony is capable of navigating Mars with minimal problems")

            else:  # if the decision was wrong
                print("Your decision causes the death of several colonists.")
                print("The colony is deciding whether they should banish you...")
                if Health <= 0:  # if the player is dead
                    isAlive = False
            input("\nPress Enter...\n")

        if isAlive:  # plays if the player survives
            print("Though there were some bumps in the metaphorical road, you managed to establish a colony on Mars")
        else:  # plays if the player dies
            print("Because of your decisions, your corpse is now in the middle of Mars")

        print("\nThe End\n")

        Replaying = get_input("1.Play Again\n2.End Simulation", "12")  # Gives the player the choice to play again
        if Replaying != '1':  # stops playing if the player does not enter 1
            Playing = False

