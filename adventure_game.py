import time
import random

def print_pause(msg):
    """Print a message and pause for 1 second."""
    print(msg)
    time.sleep(1)

def get_choice():
    """Prompt the user for a choice and ensure it's valid."""
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice in ["1", "2"]:
            return choice
        else:
            print_pause("Invalid input. Please enter 1 or 2.")

def status_line(health, supplies, steps):
    """Display the player's current status in one line."""
    print_pause(f"Health: {health} | Supplies: {supplies} | Steps: {steps}")

def explore_jungle_or_beach(supplies, health, steps):
    print_pause("\nYou see a trail leading into the jungle and a path along the beach.")
    print_pause("1. Follow the jungle trail.")
    print_pause("2. Walk along the beach.")
    choice = get_choice()
    if choice == "1":
        print_pause("You walk into the jungle. The trees close in around you.")
    else:
        print_pause("You check the beach and find a flask of clean water. But don't find people there. Supplies +1.")
        supplies += 1
    steps += 1
    status_line(health, supplies, steps)
    return supplies, health, steps

def explore_cave_or_continue(supplies, health, steps):
    print_pause("\nYou find a dark cave hidden behind some vines.")
    print_pause("1. Enter the cave.")
    print_pause("2. Avoid it and move on.")
    choice = get_choice()
    if choice == "1":
        print_pause("Inside, you find old survival gear. You grab them and come out. Supplies +2.")
        supplies += 2
    else:
        print_pause("You decide it's too risky and keep walking.")
    steps += 1
    status_line(health, supplies, steps)
    return supplies, health, steps

def deal_with_threats_and_obstacles(health, supplies, steps):
    print_pause("\nYou hear growling in the bushes.")
    print_pause("1. Climb a tree to hide.")
    print_pause("2. Try to scare the animal away.")
    choice = get_choice()
    if choice == "1":
        print_pause("You climb quickly. The animal loses interest and walks away.")
    else:
        print_pause("It's a wild bear! It attacked and you get injured. Health -30.")
        health -= 30
        if health <= 0:
            print_pause("You were too injured to survive.")
            status_line(health, supplies, steps + 1)
            return health, supplies, steps + 1, True

    steps += 1
    status_line(health, supplies, steps)

    print_pause("\nYou reach a wide river.")
    print_pause("1. Try to cross it.")
    print_pause("2. Follow it downstream.")
    choice = get_choice()
    if choice == "1":
        if random.choice([True, False]):
            print_pause("You cross safely but it takes effort. Supplies -1.")
            supplies -= 1
        else:
            print_pause("You slip on rocks and get badly hurt. Health -50.")
            health -= 50
            if health <= 0:
                print_pause("You lost too much blood and didn’t survive.")
                status_line(health, supplies, steps + 1)
                return health, supplies, steps + 1, True
    else:
        print_pause("You follow the river and find animal tracks that lead to shelter.")

    steps += 1
    status_line(health, supplies, steps)

    print_pause("\nYou spot a rescue helicopter in the distance.")
    print_pause("1. Light a signal fire.")
    print_pause("2. Wave and shout.")
    choice = get_choice()
    if choice == "1":
        if supplies >= 1:
            print_pause("You use supplies to build a fire. The helicopter sees you!")
            print_pause("You're rescued! You survived the jungle!!!.")
            status_line(health, supplies, steps + 1)
            return health, supplies, steps + 1, True  # End game on rescue
        else:
            print_pause("You don't have enough supplies to make a fire. The helicopter flies away.")
            print_pause("You're alone again in the jungle.")
    else:
        print_pause("You wave and shout, but you're not seen. The helicopter disappears.")
        print_pause("You're still stuck. You lose hope. You need to try harder. Health -30.")
        health -= 30
        if health <= 0:
            print_pause("You collapse from exhaustion and injuries.")
            status_line(health, supplies, steps + 1)
            return health, supplies, steps + 1, True

    steps += 1
    status_line(health, supplies, steps)
    return health, supplies, steps, False

def jungle_game():
    health = 100
    supplies = 3
    steps = 0
    print_pause("You wake up on a beach after a plane crash.")
    print_pause("The broken pieces of your plane are still smoking nearby.")
    print_pause("You must survive and find a way to safety.")
    print_pause(f"Health: {health} | Supplies: {supplies} | Steps: {steps}")


    while True:
        if steps == 0:
            supplies, health, steps = explore_jungle_or_beach(supplies, health, steps)
        elif steps == 1:
            supplies, health, steps = explore_cave_or_continue(supplies, health, steps)
        else:
            health, supplies, steps, end_game = deal_with_threats_and_obstacles(health, supplies, steps)
            if end_game:
                print_pause("GAME OVER")
                break

        if supplies <= 0:
            print_pause("You've run out of supplies and can't go on.")
            status_line(health, supplies, steps)
            print_pause("GAME OVER")
            break
        if health <= 0:
            print_pause("Your injuries are too severe. You can't continue.")
            status_line(health, supplies, steps)
            print_pause("GAME OVER")
            break

    while True:
        replay = input("\nDo you want to play again? Type 'yes' or 'no': ").strip().lower()
        if replay == "yes":
            jungle_game()
            break
        elif replay == "no":
            print_pause("Thanks for playing Jungle Survival! Stay safe out there.")
            break
        else:
            print_pause("Please type 'yes' or 'no'.")

# Start the game
jungle_game()
