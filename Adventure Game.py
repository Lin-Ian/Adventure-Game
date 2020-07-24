"""
Name: Adventure Game.py
Purpose: Adventure Game structure in preparation for graphics
         using Processing

Author: Lin.I

Created: 09/01/2019
"""
import time


# Create variable for list of rooms
room_list = []

# Create new rooms and append to list of rooms
room = ["Entrance lobby", 7, None, 1, 8]
room_list.append(room)
room = ["Check-in Room for the Lab", 0, None, None, 2]
room_list.append(room)
room = ["Cleaning room", None, 1, None, 3]
room_list.append(room)
room = ["Laboratory", 4, 2, None, None]
room_list.append(room)
room = ["Laboratory Storage", None, None, 3, None]
room_list.append(room)
room = ["Storage/Maintenance Room", None, 6, None, None]
room_list.append(room)
room = ["Boiler Room", None, 7, None, 5]
room_list.append(room)
room = ["Front Desk", None, None, 0, 6]
room_list.append(room)
room = ["Elevator (1st floor)", None, 0, None, None]
room_list.append(room)
room = ["Elevator (2nd floor)", None, 10, None, None]
room_list.append(room)
room = ["Hallway", 11, None, 15, 9]
room_list.append(room)
room = ["Washroom", None, None, 10, 12]
room_list.append(room)
room = ["Break Room", None, 11, 13, None]
room_list.append(room)
room = ["Printing Room", 12, None, 14, None]
room_list.append(room)
room = ["Offices", 13, 15, None, None]
room_list.append(room)
room = ["Locker Room", 10, None, None, 14]
room_list.append(room)

# Variable for room player is in
current_room = 0

# Create a variable for a list of items in the game
item_list = []

# Create items and append to list of items
item = [0, None]
item_list.append(item)
item = [1, None]
item_list.append(item)
item = [2, "Hazmat Suits"]
item_list.append(item)
item = [3, None]
item_list.append(item)
item = [4, "Needles"]
item_list.append(item)
item = [5, "Cleaning Products"]
item_list.append(item)
item = [6, None]
item_list.append(item)
item = [7, "Plants"]
item_list.append(item)
item = [8, None]
item_list.append(item)
item = [9, None]
item_list.append(item)
item = [10, "Water"]
item_list.append(item)
item = [11, "Soap"]
item_list.append(item)
item = [12, "Food"]
item_list.append(item)
item = [13, "Toner"]
item_list.append(item)
item = [14, "Money"]
item_list.append(item)
item = [15, "Credentials"]
item_list.append(item)

# Create a variable for a list of items player has
user_items = []

# Create a variable for a list of people in each room
people_list = []

# Create people and append to list of people
people = [0, 2]
people_list.append(people)
people = [1, 1]
people_list.append(people)
people = [2, 0]
people_list.append(people)
people = [3, 0]
people_list.append(people)
people = [4, 0]
people_list.append(people)
people = [5, 0]
people_list.append(people)
people = [6, 0]
people_list.append(people)
people = [7, 2]
people_list.append(people)
people = [8, 0]
people_list.append(people)
people = [9, 0]
people_list.append(people)
people = [10, 0]
people_list.append(people)
people = [11, 0]
people_list.append(people)
people = [12, 3]
people_list.append(people)
people = [13, 0]
people_list.append(people)
people = [14, 3]
people_list.append(people)
people = [15, 0]
people_list.append(people)

# Game ends if done is True
done = False

# Search item variables
found_all_items = False
item_count = 0

# Synthesizer variables
your_name = cure_name = None

# Curing people variables
cure_successful = False
everyone_cured = False
cure_count = 0

# Create a table of valid commands
valid_commands = ("""\n{0:<15}{1}{2}
{3}
{4:<15}{1}{5}
{6:<15}{1}{7}
{8:<15}{1}{9}
{10:<15}{1}{11}
{12:<15}{1}{13}
{14:<15}{1}{15}
{16:<15}{1}{17}
{18:<15}{1}{19}
{20:<15}{1}{21}
{22:<15}{1}{23}
""".format("Commands", "|", "Description",
           "-"*50,
           "North (or n)", "Player goes North",
           "East (or e)", "Player goes East",
           "South (or s)", "Player goes South",
           "West (or w)", "Player goes West",
           "Search (or f)", "Player searches room for items and people",
           "Up (or u)", "Go up in the elevator",
           "Down (or d)", "Go down in the elevator",
           "Cure (or c)", "Cure people when cure is made",
           "Help (or h)", "Display valid commands",
           "Quit (or q)", "Quit Game"))


def yes_or_no(prompt: str) -> bool:
    """Keep asking the user for a valid answer until they provide one

    :param prompt: yes or no question asked to the user
    :return: True or False, or prompt for user to enter valid answer
    """
    valid_answer = False
    while not valid_answer:
        answer = input(prompt + " (y/n) ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please enter \"y\" or \"n\"")


def step_successful():
    """If step is successfully completed advance user to next step

    :return: None
    """
    global step
    input("Step " + str(step) + " Successful\nNext -->")
    timer(start_time)


def step_unsuccessful(message: str) -> None:
    """Restart synthesis if user answers questions incorrectly

    :param message: Advice or comment on the incorrect answer given
    :return: None
    """
    global step, restart_machine
    step = 0
    restart_machine = True
    input("ERROR\nSynthesis Failed\n" +
          "You will need to restart synthesis\n" +
          message + "\nRestart -->")
    timer(start_time)


def timer(time_at_start):
    """Check and display time left

    :param time_at_start: the time in seconds at the start of the game
    :return: None
    """
    global done
    time_remaining = 600 - (time.time() - time_at_start)
    print()
    if time_remaining <= 0:
        print("You took to long to save everyone\n" +
              "You Lose")
        done = True
    else:
        print(int(time_remaining // 60), "minute(s),",
              int(time_remaining % 60), "second(s) remain")


# Welcome user
print("***** Welcome to Virus Treatment *****")

# Backstory of game
print("\nYou arrive at work like how you always have everyday.")
input("Continue -->")

print("\nHowever, today is different...")
input("Continue -->")

print("\nAt work you find out that a virus has broken out within the",
      "building and it has been quarantined by the CDC",
      "in order to prevent further outbreak.")
input("Continue -->")

print("\nYou think all hope is lost until you remember you are a scientist." +
      "\nOnly you can synthesize a cure for the virus")
input("Continue -->")

print("\nAfter minutes of hard work you determine the components",
      "needed for the cure.\nHowever you realize you only have 10 minutes",
      "before the virus kills you and everyone in the building.")
input("Continue -->")

print("\nEverything you need is in this building...")
input("Start -->")

# Find the time the game starts for the player
start_time = time.time()

# Display table of valid commands
print(valid_commands)

# Game continues prompting until game over
while not done:
    # Display the room player is in
    print("\nYou are in the", room_list[current_room][0])

    # When the cure is made, display the number of uncured people in the room
    if cure_successful and not everyone_cured:
        print(people_list[current_room][1],
              "person/people in the", room_list[current_room][0],
              "need(s) to be cured")

    # Get command from user
    command = input("What do you want to do? ").lower()

    # Travelling north
    if command == "north" or command == "n":
        next_room = room_list[current_room][1]
        # Check if player can travel to next room
        if next_room is None:
            print("You can't go that way")
        else:
            current_room = next_room

    # Travelling east
    elif command == "east" or command == "e":
        next_room = room_list[current_room][2]
        # Check if player can travel to next room
        if next_room is None:
            print("You can't go that way")
        else:
            current_room = next_room

    # Travelling south
    elif command == "south" or command == "s":
        next_room = room_list[current_room][3]
        # Check if player can travel to next room
        if next_room is None:
            print("You can't go that way")
        else:
            current_room = next_room

    # Travelling west
    elif command == "west" or command == "w":
        next_room = room_list[current_room][4]
        # Check if player can travel to next room
        if next_room is None:
            print("You can't go that way")
        # Check if player has credentials to travel to cleaning room
        elif next_room == 2 and item_list[15] not in user_items:
            print("You need credentials to go into the cleaning room")
        # Check if player has hazmat suit to travel to laboratory
        elif next_room == 3 and item_list[2] not in user_items:
            print("You died from an exposure of a cocktail of viruses,",
                  "you needed a hazmat suit. You'll get'em next time.")
            done = True
        else:
            current_room = next_room

    # Going up in elevator
    elif command == "up" or command == "u":
        # Check if player is in elevator to go up
        if room_list[current_room][0] == room_list[8][0]:
            current_room = 9
        else:
            print("You can't go up from here")

    # Going down in elevator
    elif command == "down" or command == "d":
        # Check if player is in elevator to go down
        if room_list[current_room][0] == room_list[9][0]:
            current_room = 8
        else:
            print("You can't go down from here")

    # Search room for item
    elif ((not found_all_items or not cure_successful) and
          (command == "search" or command == "f")):
        # Check if user already has item from room
        if (item_list[current_room][1] is not None and
           item_list[current_room] not in user_items):
            # Check if player has money for water
            if current_room == 10 and item_list[14] not in user_items:
                print("You need money for this item")
            # If user finds new item, and item to inventory
            else:
                user_items.append(item_list[current_room])
                item_count += 1
                print("You found", item_list[current_room][1])
                print(10-item_count, "item(s) left to find")
        # If item is already in inventory show no items in room
        else:
            print("No items in this room")
            print(10-item_count, "item(s) left to find")

        print(people_list[current_room][1], "person/people in this room")

        # Tell user to go to lab if all items have been collected
        if item_count == 10:
            found_all_items = True
            print("You have everything you need to synthesize the cure.\n" +
                  "Now head back to the lab to synthesize it")

    # Display all valid commands
    elif command == "help" or command == "h":
        print(valid_commands)

    # Leave the game
    elif command == "quit" or command == "q":
        print("You left the game")
        break

    # Synthesizing the cure
    step = 1
    leave_synth_mach = False
    if (found_all_items and current_room == 3 and not cure_successful and
        input("\nYou are in the " + room_list[current_room][0] + "\n" +
              "Welcome to Synthesizing Machine\n" +
              "Enter \"b\" to begin synthesizing cure ")) == "b":
        print()

        # Cycle through steps until cure is complete or if step is inccorect
        while not leave_synth_mach:
            restart_machine = False
            print("Step", str(step))

            if step == 1:
                if yes_or_no("Do you wish to leave the synthesis machine?"):
                    break
                your_name = input("Enter your name: ")
                print("Hello, " + your_name + ".")
                step_successful()

            elif step == 2:
                serum = input("Hello, " + your_name + ".\n" +
                              "What do you want to make?\n" +
                              "[1] Virus, [2] Cure, [3] Vaccine\n" +
                              "Enter your choice: ")
                if serum == "1":
                    step_unsuccessful("You seriously want to make a virus?!" +
                                      "\nThis one is about to kill you")
                elif serum == "2":
                    print("That's a smart choice")
                    step_successful()
                elif serum == "3":
                    step_unsuccessful("A bit late to make a vaccine" +
                                      "for a virus that is currently" +
                                      "killing you at the moment")
                else:
                    step_unsuccessful("No valid answer given")

            elif step == 3:
                if input("How many cures do you need to make?\n" +
                         "(Hint: It's the number of people in the " +
                         "building including you)\n-->") == "12":
                    step_successful()
                else:
                    step_unsuccessful("Go back and recount the number " +
                                      "of people in the building")

            elif step == 4:
                if input("What is x in this equation? (x is positive)\n7x^2 = 28 --> ") == "2":
                    step_successful()
                else:
                    step_unsuccessful("Think back to algebra")

            elif step == 5:
                print("Balance the chemical equation below:\n" +
                      "_H2 + _O2 -> _H2O)")
                H2 = input("How many H2 molecules? ")
                O2 = input("How many O2 molecules? ")
                H2O = input("How many H2O molecules? ")
                if H2 == "2" and O2 == "1" and H2O == "2":
                    step_successful()
                else:
                    step_unsuccessful("Both sides must have the " +
                                      "same number of atoms")

            elif step == 6:
                print("Balance the chemical equation below:\n" +
                      "_CH4 + _O2 -> _CO2 + _H2O)")
                CH4 = input("How many CH4 molecules? ")
                O2 = input("How many O2 molecules? ")
                CO2 = input("How many CO2 molecules? ")
                H2O = input("How many H2O molecules? ")
                if CH4 == "1" and O2 == "2" and CO2 == "1" and H2O == "2":
                    step_successful()
                else:
                    step_unsuccessful("Both sides must have the " +
                                      "same number of atoms")

            elif step == 7:
                print("Based on what you have found, what should the " +
                      "resultant or resultants of the following " +
                      "word equation be?")
                if input("Plants + Water -> ").lower() == "food":
                    step_successful()
                else:
                    step_unsuccessful("Check what you collected")

            elif step == 8:
                if yes_or_no("Cure is ready\nInject cure into needles?"):
                    input("Needles Filled\nNext -->")
                    step_successful()
                else:
                    step_unsuccessful("Cure has gone bad")

            elif step == 9:
                print("Cure Synthesized\nThis is a new cure")
                cure_name = input("What would you like to name this cure? ")
                print("Cure has now been named " + cure_name)
                step_successful()

            elif step == 10:
                print(cure_name, "is ready now\nYou have cured yourself with",
                      cure_name + "\n11 people left to cure with", cure_name)
                cure_successful = True
                leave_synth_mach = True

            print()
            step += 1

    # Curing people
    if (cure_successful and not everyone_cured and
       (command == "cure" or command == "c")):
        # Use cure if there is anyone in the room to cure
        if people_list[current_room][1] != 0:
            people_list[current_room][1] -= 1
            cure_count += 1
            print(people_list[current_room][1],
                  "person/people left to cure in the",
                  room_list[current_room][0])
            print(11-cure_count, "person/people in total left to cure with",
                  cure_name)
        # Game ends when everyone is cured
        if cure_count == 11:
            everyone_cured = True

    # Check if cure has been made before curing
    if not cure_successful and (command == "cure" or command == "c"):
        print("You need to have made the cure to cure people")

    # Check and display time left
    timer(start_time)

    # Win game message
    if everyone_cured:
        done = True
        print("\nEveryone has been cured\n" +
              "Congratulations!\nYou saved everyone")

    print()
