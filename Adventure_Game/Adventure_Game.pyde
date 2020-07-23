"""
Name:          Adventure_Game.pyde
Purpose:       Graphical implementation of <Adventure Game.py>

Author:        Lin.I

Created:       25/01/2019
"""
from time import *
from rooms import *
from items import *
from VFX import *
add_library('sound')


# Home screen variable
home = True

# Instructions page variable
instructions = False

# Play intro screen variables
intro_to_play = False
slide_number = 0

# Play adventure game variable
play_advntr_game = False

# Timer variables
start_timer = False
start_pause_timer = False
time_before_paused = 0
time_paused = 0
subtract_10 = False

# Pop-up message variables
display_message = False
pop_up_message = ""

# Paused screen variable
paused = False

# Building map variable
show_map = False

# Inventory variable
show_inventory = False

# Game over variable
game_done = False
r_val = 0
g_val = 0
b_val = 0

# Synthesizer variables
using_synthesizer = False
step = 1
player_name = ""
number_of_people = ""
x_value = ""
num_reactant_a = num_reactant_b = num_product_a = num_product_b = "_"
reactant_a = reactant_b = product_a = product_b = False
resultant = ""
cure_name = ""
cure_finished = False
restart_error_msg = ""
restart_synthesizer = False
str_nums_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
cure_count = 0

# Play error sound
play_sound = False


def home_screen():
    '''Display home screen

    :return: None
    '''
    background(255)

    # Title
    fill(0)
    textSize(75)
    textAlign(CENTER)
    text("Virus Treatment", 480, 200)

    noStroke()
    # Play button
    button(480, 295, 140, 60, 50, "Play")

    # Instructions button
    button(480, 380, 310, 60, 50, "Instructions")

    stroke(0)


def instructions_page():
    '''Display instructions page

    :return: None
    '''
    background(255)

    # Title
    fill(0)
    textSize(75)
    textAlign(CENTER)
    text("Instructions", 480, 100)

    # Instructions
    textAlign(LEFT, TOP)
    textSize(20)
    text("Use the WASD keys or on-screen buttons to navigate the building\n" +
         "Press SPACE or click on-screen button to up and " +
         "down in the elevator\n" +
         "Collect items by clicking on them\n" +
         "Synthesize a cure once you have collected all your items\n" +
         "Press Enter to enter your answer if there is no next button\n" +
         "Your time is reduced by 10 seconds for each wrong answer\n" +
         "Click on people to cure them\n" +
         "Red is sick and Green is cured\n" +
         "Remember you only have 10 minutes\n" +
         "Quick Tip: Make sure to count the number of " +
         "people in the building\n" +
         "Press \"m\" or click on icon to open map\n" +
         "Press \"i\" or click on icon to open inventory", 120, 160)

    # Back button
    button(50, 490, 100, 100, 20, "BACK\n<--")


def play_intro_slides(slide_num):
    '''Give user an introduction/backstory to the game

    :param slide_num: the slide number of introduction
    :return: None
    '''
    slide_text_list = []

    # Append text to a list for slides
    slide_text = "You arrive at work just like\nhow you always have everyday."
    slide_text_list.append(slide_text)
    slide_text = "However, today is different..."
    slide_text_list.append(slide_text)
    slide_text = ("At work you find out that a virus\nhas broken out " +
                  "within the building\nand it has been quarantined by " +
                  "the CDC\nin order to prevent further outbreak.")
    slide_text_list.append(slide_text)
    slide_text = ("You think all hope is lost until you remember\nyou are " +
                  "a scientist.\nOnly you can synthesize a cure for the virus")
    slide_text_list.append(slide_text)
    slide_text = ("After minutes of hard work\nyou determine the components" +
                  "\nneeded for the cure.\nHowever you realize you only " +
                  "have 10 minutes\nbefore the virus kills you and\n" +
                  "everyone in the building.")
    slide_text_list.append(slide_text)
    slide_text = "Everything you need is in this building..."
    slide_text_list.append(slide_text)

    background(255)

    # Display information on slide
    fill(0)
    textSize(40)
    textAlign(CENTER, CENTER)
    text(slide_text_list[slide_num], 480, 270)

    # Continue button
    fill(255)
    if slide_num == 5:
        button(860, 490, 200, 100, 20, "Start\n ----->")
    else:
        button(860, 490, 200, 100, 20, "Continue\n ----->")


def timer():
    '''Timer of 10 minutes for the game

    :return: None
    '''
    global start_time, start_timer, start_pause_timer
    global time_before_paused, time_paused, subtract_10
    global game_done, pop_up_message
    # Get the time at which the game starts
    if not start_timer:
        start_time = time()
        start_timer = True

    # Get the time at which the game is paused
    if paused:
        if not start_pause_timer:
            time_before_paused = time()
            start_pause_timer = True
    # Find the amount of time spent when game was paused
    else:
        if start_pause_timer:
            start_pause_timer = False
            time_paused += time() - time_before_paused

    # Determine the time left in the game
    time_remaining = 600 - (time() - start_time) + time_paused

    # Take 10 seconds from the clock if synthesizer answer is incorrect
    if subtract_10:
        time_remaining -= 10
        subtract_10 = False

    # Find the number of minutes left in game
    minutes = time_remaining // 60
    # Find the number of seconds left in game
    seconds = time_remaining % 60
    # Time left in digital clock format
    dig_clock = '%02d:%02d' % (minutes, seconds)

    fill(0)
    textSize(30)
    textAlign(CENTER, TOP)
    # Display time left
    text("Time left " + dig_clock, 770, 10)

    # Check if time has not gone past 10 minutes
    if time_remaining <= 0:
        game_done = True
        pop_up_message = "You took too long to save everyone\nYou Lose"


def synthesizer():
    '''Display synthesizer screen

    :return: None
    '''
    global step, player_name, number_of_people, x_value
    global num_reactant_a, num_reactant_b, num_product_a, num_product_b
    global reactant_a, reactant_b, product_a, product_b, resultant
    global cure_name, cure_finished, restart_error_msg, restart_synthesizer
    background(57, 255, 20)
    fill(0)
    textAlign(CENTER, CENTER)
    textSize(40)
    # Title
    text("Step " + str(step), 240, 54)

    # Display step 1
    if step == 1:
        text("Enter your name: " + player_name, 480, 270)
        textSize(30)
        text("*** Backspace clears text ***", 480, 405)

    # Display step 2
    elif step == 2:
        text("Hello " + player_name + ",\nWhat do you what to make?", 480, 135)
        command_button(240, 370, 150, 100, 255, 40, "Virus")
        command_button(480, 370, 150, 100, 255, 40, "Cure")
        command_button(720, 370, 150, 100, 255, 40, "Vaccine")

    # Display step 3
    elif step == 3:
        text("How many cures do you need to make?\n" +
             "(Hint: It's the number of people\n in the building " +
             "including you)\n--> " + str(number_of_people), 480, 270)
        text("*** Backspace clears text ***", 480, 405)

    # Display step 4
    elif step == 4:
        text("What is x in this equation?\n7x^2 = 28\nx = " +
             x_value, 480, 270)
        text("*** Backspace clears text ***\n" +
             "*** x is positive ***", 480, 425)

    # Display step 5
    elif step == 5:
        fill(255)
        rectMode(CENTER)
        if reactant_a:
            rect(320, 270, 100, 50)
        elif reactant_b:
            rect(480, 270, 100, 50)
        elif product_a:
            rect(640, 270, 100, 50)

        fill(0)
        textAlign(CENTER, CENTER)
        text("Balance the chemical equation below:", 480, 170)
        text(num_reactant_a + "H2 + ", 320, 270)
        text(num_reactant_b + "O2 -> ", 480, 270)
        text(num_product_a + "H2O", 640, 270)

        text("*** Click on each symbol to answer ***\n" +
             "*** Answer all of the above ***", 480, 390)

        # Check answers
        button(860, 490, 200, 100, 30, "Next")

    # Display step 6
    elif step == 6:
        fill(255)
        rectMode(CENTER)
        if reactant_a:
            rect(160, 270, 100, 50)
        elif reactant_b:
            rect(320, 270, 100, 50)
        elif product_a:
            rect(640, 270, 100, 50)
        elif product_b:
            rect(800, 270, 100, 50)

        fill(0)
        textAlign(CENTER, CENTER)
        text("Balance the chemical equation below:", 480, 170)
        text(num_reactant_a + "CH4 + ", 160, 270)
        text(num_reactant_b + "O2", 320, 270)
        text("->", 480, 270)
        text(num_product_a + "CO2 + ", 640, 270)
        text(num_product_b + "H2O", 800, 270)

        text("*** Click on each symbol to answer ***\n" +
             "*** Answer all of the above ***", 480, 390)

        # Check answer
        button(860, 490, 200, 100, 30, "Next")

    # Display step 7
    elif step == 7:
        text("Based on what you have found,\n" +
             "what should the resultant or\nresultants of the " +
             "following word equation be?\n" +
             "plants + water -> " + resultant, 480, 270)
        text("*** Backspace clears text ***\n" +
             "*** Enter answer in lower case ***", 480, 450)

    # Display step 8
    elif step == 8:
        text("Cure is ready\nInject cure into needles?", 480, 180)
        command_button(320, 360, 150, 150, 255, 40, "YES")
        command_button(640, 360, 150, 150, 255, 40, "NO")

    # Display step 9
    elif step == 9:
        text("Cure Synthesized\nThis is a new cure\n" +
             "What would you like to name this cure?\n--> " + cure_name,
             480, 270)
        text("*** Backspace clears text ***", 480, 405)

    # Display step 10
    elif step == 10:
        text(cure_name + " is ready now\nYou have cured yourself\n" +
             "11 people left to cure with " + cure_name +
             "\nClick anywhere to leave", 480, 270)

    # Button to leave synthesizer
    if step != 10:
        button(50, 490, 100, 100, 20, "LEAVE\n<--")


def word_input(player_input):
    '''Ensure player is inputting an answer when asked for name

    :param player_input: player input
    :return: player input
    '''
    global display_message, pop_up_message, step
    if key == BACKSPACE:
        player_input = ""
    elif key == ENTER:
        if player_input == "":
            pop_up_message = "Enter a name"
            display_message = True
        else:
            step += 1
    else:
        player_input += key
    return player_input


def number_input(player_input):
    '''Ensure player is inputting a number

    :param equation_component: player input
    :return: player input
    '''
    global display_message, pop_up_message
    if key == BACKSPACE:
        player_input = ""
    elif key not in str_nums_list:
        pop_up_message = "Enter valid number"
        display_message = True
    else:
        player_input += key
    return player_input


def check_room(direction):
    '''Check if player can travel in the direction they wish

    :param direction: index 1-4 of room for cardinal directions
    :return: if player can go in the direction they wish
    '''
    global display_message, pop_up_message
    global game_done, r_val, g_val, b_val
    next_room = room_list[current_room][direction]
    # Check if there is a room in said direction
    if next_room is None:
        display_message = True
        pop_up_message = "You can't go that way"
        # print("You can't go that way")
        return current_room

    # Player needs to have credentials before entering the cleaning room
    elif next_room == 2 and item_list[15] not in user_items:
        display_message = True
        pop_up_message = "You need credentials to go into the cleaning room"
        return current_room

    # If player does not have hazmat suit before entering lab they lose
    elif next_room == 3 and item_list[2] not in user_items:
        game_done = True
        r_val = 255
        g_val = 8
        b_val = 0
        pop_up_message = "You died from an exposure of many viruses"
        return current_room

    # If room next room is not None player can go to next room
    else:
        display_message = False
        return next_room


def display_pop_up_msg(display, message):
    '''Display a pop up message to player

    :param display: if message needs to be shown
    :param message: message to be displayed
    :return: None
    '''
    fill(100, 100, 255)
    textAlign(CENTER, CENTER)
    textSize(30)
    if using_synthesizer:
        text(message, 480, 480)
    elif display:
        text(message, 480, 270)


# Function to draw a paused screen menu
def pause_game():
    '''Display pause screen

    :return: None
    '''
    background(255)
    textSize(40)
    textAlign(CENTER)
    fill(0)
    text("Game Paused", 480, 100)

    # Resume
    button(480, 405, 200, 100, 20, "RESUME")
    # Quit
    button(480, 270, 200, 100, 20, "QUIT")


def game_done_screen(message, r_value, g_value, b_value):
    '''Display game done screen

    :param message: message for player to read
    :return: None
    '''
    background(r_value, g_value, b_value)
    textSize(40)
    textAlign(CENTER, CENTER)
    text(message, 480, 270)
    button(860, 490, 200, 100, 20, "--->")


def reset_pages():
    '''Reset pages when changing between pages

    :return: None
    '''
    global home, instructions, intro_to_play, play_advntr_game
    global show_map, paused, game_done
    home = instructions = intro_to_play = play_advntr_game = False
    show_map = paused = game_done = False


def reset_synthesizer():
    '''Reset synthesizer if player answers incorrectly

    :return: None
    '''
    global step
    global player_name, number_of_people, x_value
    global reactant_a, reactant_b, product_a, product_b
    global num_reactant_a, num_reactant_b, num_product_a, num_product_b
    global resultant, cure_name
    step = 1
    player_name = number_of_people = x_value = ""
    reactant_a = reactant_b = product_a = product_b = False
    num_reactant_a = num_reactant_b = num_product_a = num_product_b = "_"
    resultant = cure_name = ""


def restart_screen(message):
    '''Display restart screen for synthesizer if player answers incorrectly

    :param message: display message for player to read
    :return: None
    '''
    global display_message, subtract_10, play_sound
    display_message = False
    background(255, 0, 0)
    textSize(40)
    textAlign(CENTER, CENTER)
    text(message, 480, 270)
    button(860, 490, 200, 100, 30, "RESTART")
    reset_synthesizer()
    subtract_10 = True
    if play_sound:
        synthesizer_error_sound.play()
        play_sound = False


def reset_game():
    '''Reset game data if player quits, loses or wins

    :return: None
    '''
    global slide_number, current_room, user_items
    global display_message
    global start_timer, start_pause_timer, time_before_paused, time_paused
    global cure_name
    global using_synthesizer, restart_synthesizer
    global cure_count, people_list, org_people_list
    global home
    slide_number = current_room = 0
    user_items = []
    display_message = False
    start_timer = start_pause_timer = False
    timer_before_paused = time_paused = 0
    cure_name = ""
    using_synthesizer = restart_synthesizer = False
    cure_count = 0
    reset_synthesizer()
    reset_pages()
    home = True


def setup():
    global synthesizer_error_sound
    size(960, 540)
    synthesizer_error_sound = SoundFile(this, "Error Sound.wav")


def draw():
    if home:
        home_screen()

    elif instructions:
        instructions_page()

    elif intro_to_play:
        play_intro_slides(slide_number)

    elif play_advntr_game:
        adventure_game(current_room)
        if show_map:
            building_map(level)
        elif show_inventory:
            inventory()
        elif using_synthesizer:
            synthesizer()
            if restart_synthesizer:
                restart_screen(restart_error_msg)

        if display_message:
            display_pop_up_msg(display_message, pop_up_message)

        timer()
        command_buttons(using_synthesizer, show_map, show_inventory)

        if game_done:
            game_done_screen(pop_up_message, r_val, g_val, b_val)
        elif paused:
            pause_game()


def mouseClicked():
    global home, instructions, intro_to_play, slide_number, show_map
    global play_advntr_game, current_room, display_message, pop_up_message
    global paused, level
    global user_items, show_inventory
    global using_synthesizer, step, restart_synthesizer
    global game_done, r_val, g_val, b_val
    global reactant_a, reactant_b, product_a, product_b
    global num_reactant_a, num_reactant_b, num_product_a, num_product_b
    global restart_error_msg
    global cure_finished, people_list, cure_count
    global play_sound

    # Home to instructions
    if home and mouse_in_button(325, 635, 350, 410):
        reset_pages()
        instructions = True
    # Instructions to home
    elif instructions and mouse_in_button(0, 100, 440, 540):
        reset_pages()
        home = True

    # Home to play intro
    if home and mouse_in_button(410, 550, 265, 325):
        reset_pages()
        intro_to_play = True

    # Advance slides in play intro
    if slide_number == 5:
        reset_pages()
        play_advntr_game = True
        slide_number = 6
    elif (intro_to_play and slide_number < 5 and
          mouse_in_button(760, 960, 440, 540)):
        slide_number += 1

    # Play the adventure game
    elif play_advntr_game:

        if (not paused and not show_map and not using_synthesizer and
           not game_done):
            # North navigation
            if mouse_in_button(835, 885, 365, 415):
                current_room = check_room(1)
            # East navigation
            elif mouse_in_button(885, 935, 415, 465):
                current_room = check_room(2)
            # South navigation
            elif mouse_in_button(835, 885, 465, 515):
                current_room = check_room(3)
            # West navigation
            elif mouse_in_button(785, 835, 415, 465):
                current_room = check_room(4)

            # Go up and down in elevator
            elif mouse_in_button(835, 885, 415, 465):
                if current_room == 8:
                    current_room = 9
                    display_message = False
                elif current_room == 9:
                    current_room = 8
                    display_message = False
                elif current_room < 8:
                    display_message = True
                    pop_up_message = "You need to be in the elevator to go up"
                elif current_room > 9:
                    display_message = True
                    pop_up_message = ("You need to be in the elevator " +
                                      "to go down")

            # If player finds/clicks on any items in the rooms
            if (item_list[current_room] not in user_items and
               item_list[current_room][1] is not None):

                # Cleaning Room (hazmat suit)
                if (mouse_in_button(450, 550, 250, 350) and
                   current_room == 2):
                    user_items.append(item_list[current_room])

                # Lab storage (needles)
                elif (mouse_in_button(450, 550, 250, 350) and
                      current_room == 4):
                    user_items.append(item_list[current_room])

                # Storage room (cleaning products)
                elif (mouse_in_button(450, 550, 250, 350) and
                      current_room == 5):
                    user_items.append(item_list[current_room])

                # Front desk (plant)
                elif (mouse_in_button(450, 550, 250, 350) and
                      current_room == 7):
                    user_items.append(item_list[current_room])

                # Hallway (water)
                elif (mouse_in_button(390, 490, 230, 330) and
                      current_room == 10):
                    # Player needs to have money in the inventory
                    if item_list[14] in user_items:
                        user_items.append(item_list[current_room])
                    else:
                        display_message = True
                        pop_up_message = "You need money for this item"
                        # print("You need money for this item")

                # Washroom (soap)
                elif (mouse_in_button(450, 550, 250, 350) and
                      current_room == 11):
                    user_items.append(item_list[current_room])

                # Break room (food)
                elif (mouse_in_button(450, 550, 250, 350) and
                      current_room == 12):
                    user_items.append(item_list[current_room])

                # Printing room (toner)
                elif (mouse_in_button(450, 550, 250, 350) and
                      current_room == 13):
                    user_items.append(item_list[current_room])

                # Offices (money)
                elif (mouse_in_button(450, 550, 250, 350) and
                      current_room == 14):
                    user_items.append(item_list[current_room])

                # Locker room (credentials)
                elif (mouse_in_button(450, 550, 250, 350) and
                      current_room == 15):
                    user_items.append(item_list[current_room])

            # Check if everyone has been cured
            if len(user_items) == 10 and not cure_finished:
                display_message = True
                pop_up_message = ("You have everything you need to " +
                                  "synthesize the cure.\nNow head back " +
                                  "to the lab to synthesize it")

        # Open game map
        if (not show_map and not using_synthesizer and not show_inventory and
           mouse_in_button(25, 75, 465, 515)):
            show_map = True
            display_message = False
        # Close game map
        elif (not using_synthesizer and show_map and
              mouse_in_button(0, 50, 490, 540)):
            show_map = False
        # Flip map
        elif show_map and mouse_in_button(860, 960, 440, 540):
            level = (level+1) % 2

        # Open player inventory
        if (not show_inventory and not using_synthesizer and
           mouse_in_button(100, 150, 465, 515)):
            show_inventory = True
            display_message = False
        # Close player inventory
        elif (show_inventory and not using_synthesizer and
              mouse_in_button(0, 100, 440, 540)):
            show_inventory = False

        # Use synthesizer in lab
        if (not using_synthesizer and len(user_items) == 10 and
           current_room == 3 and mouse_in_button(200, 350, 350, 425)):
            display_message = False
            using_synthesizer = True

        # Leave synthesizer screen
        elif (step != 10 and using_synthesizer and
              mouse_in_button(0, 100, 440, 540)):
            using_synthesizer = False
            reset_synthesizer()

        # Sythesizer at step 2
        elif using_synthesizer and step == 2:
            display_message = False
            if mouse_in_button(165, 315, 320, 420):
                restart_synthesizer = True
                restart_error_msg = ("You seriously want to make a virus?!\n" +
                                     "This one is about to kill you")
            elif mouse_in_button(645, 795, 320, 420):
                restart_synthesizer = True
                restart_error_msg = ("A bit late to make a vaccine\n" +
                                     "for a virus that is currently " +
                                     "killing you")
            elif mouse_in_button(405, 555, 320, 420):
                step += 1

        # Synthesizer at step 5
        elif using_synthesizer and step == 5:
            display_message = False
            if mouse_in_button(240, 340, 220, 320):
                reactant_b = product_a = product_b = False
                reactant_a = True
                num_reactant_a = ""
            elif mouse_in_button(430, 530, 220, 320):
                reactant_a = product_a = product_b = False
                reactant_b = True
                num_reactant_b = ""
            elif mouse_in_button(610, 770, 220, 320):
                reactant_a = reactant_b = product_b = False
                product_a = True
                num_product_a = ""

            # Check answer
            elif mouse_in_button(760, 960, 440, 540):
                if (num_reactant_a == "2" and num_reactant_b == "1" and
                   num_product_a == "2"):
                    step += 1
                    reactant_a = reactant_b = product_a = product_b = False
                    num_reactant_a = num_reactant_b = "_"
                    num_product_a = num_product_b = "_"
                else:
                    restart_synthesizer = True
                    restart_error_msg = ("Both sides must have the same " +
                                         "number of atoms")

        # Synthesizer at step 6
        elif using_synthesizer and step == 6:
            display_message = False
            if mouse_in_button(110, 210, 245, 295):
                reactant_b = product_a = product_b = False
                reactant_a = True
                num_reactant_a = ""
            elif mouse_in_button(270, 370, 245, 295):
                reactant_a = product_a = product_b = False
                reactant_b = True
                num_reactant_b = ""
            elif mouse_in_button(590, 690, 245, 295):
                reactant_a = reactant_b = product_b = False
                product_a = True
                num_product_a = ""
            elif mouse_in_button(710, 850, 245, 295):
                reactant_a = reactant_b = product_a = False
                product_b = True
                num_product_b = ""
            # Check answer
            elif mouse_in_button(760, 960, 440, 540):
                if (num_reactant_a == "1" and num_reactant_b == "2" and
                   num_product_a == "1" and num_product_b == "2"):
                    step += 1
                    num_reactant_a = num_reactant_b = "_"
                    num_product_a = num_product_b = "_"
                else:
                    restart_synthesizer = True
                    restart_error_msg = ("Both sides must have the same " +
                                         "number of atoms")

        # Synthesizer at step 8
        elif using_synthesizer and step == 8:
            if mouse_in_button(245, 395, 285, 435):
                step += 1
            elif mouse_in_button(565, 715, 285, 435):
                restart_synthesizer = True
                restart_error_msg = "Cure has gone bad"

        # Synthesizer at step 10
        elif using_synthesizer and step == 10:
            cure_finished = True
            using_synthesizer = False

        # Dismiss restart screen
        elif restart_synthesizer:
            if mouse_in_button(760, 960, 440, 540):
                restart_synthesizer = False
                play_sound = True

        # Cure people when cure is finished
        if cure_finished:
            # Cure people in Entrance Lobby
            if current_room == 0:
                if (mouse_in_button(75, 125, 375, 525) and
                   not people_list[0][1]):
                    people_list[0][1] = True
                    cure_count += 1
                elif (mouse_in_button(575, 625, 275, 425) and
                      not people_list[0][2]):
                    people_list[0][2] = True
                    cure_count += 1
            # Cure person in Check-in Room
            elif current_room == 1:
                if (mouse_in_button(675, 725, 325, 475) and
                   not people_list[1][1]):
                    people_list[1][1] = True
                    cure_count += 1
            # Cure people at Front Desk
            elif current_room == 7:
                if (mouse_in_button(275, 325, 175, 325) and
                   not people_list[7][1]):
                    people_list[7][1] = True
                    cure_count += 1
                elif (mouse_in_button(675, 725, 175, 325) and
                      not people_list[7][2]):
                    people_list[7][2] = True
                    cure_count += 1
            # # Cure people in Break Room
            elif current_room == 12:
                if (mouse_in_button(175, 225, 325, 475) and
                   not people_list[12][1]):
                    people_list[12][1] = True
                    cure_count += 1
                elif (mouse_in_button(475, 525, 325, 475) and
                      not people_list[12][2]):
                    people_list[12][2] = True
                    cure_count += 1
                elif (mouse_in_button(675, 725, 325, 475) and
                      not people_list[12][3]):
                    people_list[12][3] = True
                    cure_count += 1
            # Cure people in Offices
            elif current_room == 14:
                if (mouse_in_button(75, 125, 325, 475) and
                   not people_list[14][1]):
                    people_list[14][1] = True
                    cure_count += 1
                elif (mouse_in_button(375, 425, 325, 475) and
                      not people_list[14][2]):
                    people_list[14][2] = True
                    cure_count += 1
                elif (mouse_in_button(675, 725, 325, 475) and
                      not people_list[14][3]):
                    people_list[14][3] = True
                    cure_count += 1

        # Player wins if they cure everyone in 10 minutes
        if cure_count == 11:
            game_done = True
            r_val = 57
            g_val = 255
            b_val = 20
            pop_up_message = ("YAY!\nEveryone has been cured\n" +
                              "Congratulations!\nYou saved everyone")

        # Pause game
        if (play_advntr_game and not paused and
           mouse_in_button(910, 960, 0, 50)):
            paused = True
        # Resume game
        elif paused and mouse_in_button(440, 640, 355, 455):
            paused = False
        # Quit game
        elif paused and mouse_in_button(440, 640, 220, 320):
            reset_game()

        # Game done
        if game_done:
            if mouse_in_button(760, 960, 440, 540):
                reset_game()


def keyTyped():
    global current_room, show_map, show_inventory, paused
    global step
    global player_name, number_of_people, x_value
    global reactant_a, reactant_b, product_a, product_b
    global num_reactant_a, num_reactant_b, num_product_a, num_product_b
    global resultant, cure_name
    global display_message, pop_up_message
    global restart_synthesizer, restart_error_msg

    if play_advntr_game:
        if (not paused and not show_map and not using_synthesizer and
           not game_done):
            # North navigation
            if key == "w":
                current_room = check_room(1)
            # East navigation
            elif key == "d":
                current_room = check_room(2)
            # South navigation
            elif key == "s":
                current_room = check_room(3)
            # West navigation
            elif key == "a":
                current_room = check_room(4)

            # Go up and down in elevator
            elif key == " ":
                if current_room == 8:
                    current_room = 9
                    display_message = False
                elif current_room == 9:
                    current_room = 8
                    display_message = False
                elif current_room < 8:
                    display_message = True
                    pop_up_message = "You need to be in the elevator to go up"
                elif current_room > 9:
                    display_message = True
                    pop_up_message = ("You need to be in the elevator" +
                                      "to go down")

        # Display game map
        if (not show_map and not using_synthesizer and
           not show_inventory and key == "m"):
            show_map = True
            display_message = False
        elif (show_map and not using_synthesizer and
              not show_inventory and key == "m"):
            show_map = False

        # Display player inventory
        if (not show_inventory and not using_synthesizer and
           not show_map and key == "i"):
            show_inventory = True
        elif (show_inventory and not using_synthesizer and
              not show_map and key == "i"):
            show_inventory = False

        # Pause and unpause game
        if not paused and not using_synthesizer and key == "p":
            paused = True
        else:
            paused = False

    # Synthesizer input
    if using_synthesizer:
        display_message = False
        # Key input for step 1
        if step == 1:
            player_name = word_input(player_name)

        # Key input for step 3
        elif step == 3:
            number_of_people = number_input(number_of_people)
            if key == ENTER:
                if number_of_people == "12":
                    step += 1
                    display_message = False
                else:
                    restart_synthesizer = True
                    restart_error_msg = ("Go back and recount the number\n" +
                                         "of people in the building")

        # Key input for step 4
        elif step == 4:
            x_value = number_input(x_value)
            if key == ENTER:
                if x_value == "2":
                    step += 1
                    display_message = False
                else:
                    restart_synthesizer = True
                    restart_error_msg = "Think back to algebra"

        # Key input for step 5
        elif step == 5:
            if reactant_a:
                num_reactant_a = number_input(num_reactant_a)
            elif reactant_b:
                num_reactant_b = number_input(num_reactant_b)
            elif product_a:
                num_product_a = number_input(num_product_a)

        # Key input for step 6
        elif step == 6:
            if reactant_a:
                num_reactant_a = number_input(num_reactant_a)
            elif reactant_b:
                num_reactant_b = number_input(num_reactant_b)
            elif product_a:
                num_product_a = number_input(num_product_a)
            elif product_b:
                num_product_b = number_input(num_product_b)

        # Key input for step 7
        elif step == 7:
            resultant = word_input(resultant)
            if key == ENTER:
                if resultant != "food":
                    restart_synthesizer = True
                    restart_error_msg = "Check what you collected"

        # Key input for step 9
        elif step == 9:
            cure_name = word_input(cure_name)
            if key == ENTER:
                if cure_name == "":
                    display_message = True
                    pop_up_message = "Please enter a name"