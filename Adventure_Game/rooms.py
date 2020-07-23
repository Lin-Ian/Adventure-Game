"""
Name:          rooms.py
Purpose:       Defined functions that are used to
               draw the rooms of the game

Author:        Lin.I

Created:       25/01/2019
"""
from items import *
from VFX import *


# Create variable for a list of rooms
room_list = []

# Create rooms and append to list of rooms
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

# Create a variable for a list of people in each room
people_list = []

# Create people and append to list of people
people = [0, False, False, None]
people_list.append(people)
people = [1, False, None, None]
people_list.append(people)
people = [2, None, None, None]
people_list.append(people)
people = [3, None, None, None]
people_list.append(people)
people = [4, None, None, None]
people_list.append(people)
people = [5, None, None, None]
people_list.append(people)
people = [6, None, None, None]
people_list.append(people)
people = [7, False, False, None]
people_list.append(people)
people = [8, None, None, None]
people_list.append(people)
people = [9, None, None, None]
people_list.append(people)
people = [10, None, None, None]
people_list.append(people)
people = [11, None, None, None]
people_list.append(people)
people = [12, False, False, False]
people_list.append(people)
people = [13, None, None, None]
people_list.append(people)
people = [14, False, False, False]
people_list.append(people)
people = [15, None, None, None]
people_list.append(people)

# Variable for floor level
level = 0


# Function to display game by calling other functions that display rooms
def adventure_game(current_room):
    '''Display the rooms when playing the game

    :param current_room: the room the player is in
    :return: None
    '''
    rectMode(CORNER)

    # Draw the appropriate room
    if current_room == 0:
        room_zero()
    elif current_room == 1:
        room_one()
    elif current_room == 2:
        room_two()
    elif current_room == 3:
        room_three()
    elif current_room == 4:
        room_four()
    elif current_room == 5:
        room_five()
    elif current_room == 6:
        room_six()
    elif current_room == 7:
        room_seven()
    elif current_room == 8 or current_room == 9:
        elevator()
    elif current_room == 10:
        room_ten()
    elif current_room == 11:
        room_eleven()
    elif current_room == 12:
        room_twelve()
    elif current_room == 13:
        room_thirteen()
    elif current_room == 14:
        room_fourteen()
    elif current_room == 15:
        room_fifteen()

    # Display room player is in
    fill(255)
    textAlign(CENTER)
    textSize(40)
    text(room_list[current_room][0], width/2, 90)
    draw_items(current_room)


# Entrance Lobby
def room_zero():
    '''Draw entrance lobby

    :return: None
    '''
    background(100)

    # Floor
    fill(145, 41, 3)
    rect(0, 300, 960, 240)

    # Elevator Doors
    fill(200)
    rect(380, 150, 200, 150)
    line(480, 150, 480, 300)

    draw_person(100, 400, people_list[0][1])
    draw_person(600, 300, people_list[0][2])


# Check-in room for Lab
def room_one():
    '''Draw check-in room for lab

    :return: None
    '''
    background(100)

    # Floor
    fill(255)
    rect(0, 350, 960, 190)

    # Door
    rect(200, 200, 100, 150)
    rect(320, 240, 20, 40)

    draw_person(700, 350, people_list[1][1])


# Cleaning Room
def room_two():
    '''Draw the cleaning room

    :return: None
    '''
    background(100)

    # Floor
    fill(255)
    rect(0, 300, 960, 240)

    # Sign
    rect(380, 150, 200, 100)
    textSize(20)
    textAlign(CENTER, CENTER)
    fill(0)
    text("Hazmat suits must\nbe worn at all times\nin the Lab", 480, 200)

    # Shower head
    fill(255)
    ellipse(760, 100, 50, 25)

    # Door
    rect(180, 150, 100, 150)


# Laboratory
def room_three():
    '''Draw laboratory

    :return: None
    '''
    background(100)

    # Floor
    fill(255)
    rect(0, 300, 960, 240)

    # Table
    rect(380, 200, 200, 20)
    rect(380, 220, 20, 90)
    rect(560, 220, 20, 90)
    noStroke()
    rect(470, 140, 20, 40)
    triangle(480, 160, 520, 200, 440, 200)

    # Synthesizer machine
    stroke(0)
    rect(200, 350, 150, 75)
    fill(52, 240, 10)
    rect(225, 310, 100, 40)
    fill(0)
    textSize(25)
    text("Synthesizer", 275, 388)


# Laboratory Storage
def room_four():
    '''Draw laboratory storage

    :return: None
    '''
    background(100)

    # Floor
    fill(255)
    rect(0, 300, 960, 240)

    # Shelf
    for x in range(100, 661, 280):
        fill(255)
        rect(x, 150, 200, 150)
        fill(0)
        line(x, 200, x+200, 200)
        line(x, 250, x+200, 250)


# Maintenance/Storage Room
def room_five():
    '''Draw maintenace/storage room

    :return: None
    '''
    background(100)

    # Floor
    fill(255)
    rect(0, 300, 960, 240)

    # Shelf
    for x in range(100, 661, 280):
        fill(255)
        rect(x, 150, 200, 150)
        fill(0)
        line(x, 200, x+200, 200)
        line(x, 250, x+200, 250)

    # Buckets
    fill(255)
    for y in range(275, 325, 10):
        quad(50, y, 100, y, 85, y+50, 65, y+50)


# Boiler Room
def room_six():
    '''Draw boiler room

    :return: None
    '''
    background(100)

    # Floor
    fill(200)
    rect(0, 300, 960, 240)

    # Water tank
    fill(0)
    rect(0, 200, 250, 20)
    fill(255)
    noStroke()
    ellipse(250, 350, 100, 50)
    rect(200, 150, 100, 200)
    stroke(0)
    ellipse(250, 150, 100, 50)

    # Furnace
    rect(650, 150, 170, 250)
    fill(0)
    rect(670, 0, 20, 150)


# Front Desk
def room_seven():
    '''Draw front desk

    :return: None
    '''
    background(100)

    # Floor
    fill(255)
    rect(0, 300, 960, 240)

    # Clock
    ellipse(280, 60, 100, 100)
    line(280, 60, 280, 20)
    line(280, 60, 250, 60)
    draw_person(300, 200, people_list[7][1])
    draw_person(700, 200, people_list[7][2])

    # Desk
    fill(100)
    rect(150, 250, 660, 210)
    fill(255)
    rect(200, 300, 560, 110)


# Rooms 8 and 9
def elevator():
    '''Draw elevator

    :return: None
    '''
    background(100)

    # Floor
    fill(255)
    rect(0, 400, 960, 140)

    # Elevator doors
    fill(200)
    rect(280, 150, 400, 250)
    line(480, 150, 480, 400)

    # Railings
    rect(0, 270, 190, 20)
    rect(770, 270, 190, 20)

    # Choose level
    rect(710, 250, 40, 60)


# Hallway
def room_ten():
    '''Draw hallway

    :return: None
    '''
    background(100)

    # Floor
    fill(255)
    rect(0, 400, 960, 140)

    # Vending Machine
    fill(200)
    rect(150, 200, 120, 200)
    rect(380, 200, 120, 200)

    # Tree plant
    quad(700, 320, 770, 320, 750, 410, 720, 410)
    rect(730, 250, 10, 70)
    fill(20, 250, 0)
    ellipse(735, 200, 120, 180)


# Washroom
def room_eleven():
    '''Draw washroom

    :return: None
    '''
    background(200)

    # Floor
    fill(255)
    rect(0, 420, 960, 120)

    # Mirror
    fill(207, 237, 250)
    rect(100, 100, 760, 150)

    # Table
    fill(255)
    rect(50, 270, 860, 150)

    # Faucets
    rect(320, 255, 20, 10)
    rect(640, 255, 20, 10)


# Break Room
def room_twelve():
    '''Draw break room

    :return: None
    '''
    background(100)

    # Floor
    fill(255)
    rect(0, 300, 960, 240)

    draw_person(200, 350, people_list[12][1])
    draw_person(500, 350, people_list[12][2])
    draw_person(700, 350, people_list[12][3])


# Printing Room
def room_thirteen():
    '''Draw printer room

    :return: None
    '''
    background(100)
    # Floor
    fill(255)
    rect(0, 400, 960, 140)

    # Table
    rect(700, 350, 200, 10)
    rect(700, 360, 10, 80)
    rect(880, 360, 10, 80)

    # Photocopier machine
    rect(200, 300, 200, 150)
    rect(270, 305, 60, 40)
    quad(120, 300, 200, 300, 200, 340, 120, 315)
    quad(120, 350, 200, 350, 200, 390, 120, 365)
    quad(400, 300, 480, 300, 480, 315, 400, 340)
    quad(400, 350, 480, 350, 480, 365, 400, 390)


# Offices
def room_fourteen():
    '''Draw Offices

    :return: None
    '''
    background(100)

    # Floor
    fill(255)
    rect(0, 300, 960, 240)

    # Table
    for x in range(50, 850, 300):
        rect(x, 350, 200, 10)
        rect(x, 360, 10, 80)
        rect(x+190, 360, 10, 80)

    draw_person(100, 350, people_list[14][1])
    draw_person(400, 350, people_list[14][2])
    draw_person(700, 350, people_list[14][3])


# Locker Room
def room_fifteen():
    '''Draw locker room

    '''
    # Floor
    fill(100)
    rect(0, 400, 960, 240)

    # Lockers
    for x in range(0, 960, 96):
        for y in range(0, 400, 200):
            fill(50, 50, 250)
            rect(x, y, 96, 200)
            fill(100)
            rect(x+56, y+160, 20, 20)

    # Bench
    rect(100, 450, 800, 25)
    rect(300, 475, 25, 65)
    rect(500, 475, 25, 65)
    rect(700, 475, 25, 65)


# Function to draw people in the rooms
def draw_person(x_pos_person, y_pos_person, cured):
    '''Draw person based on x and y coordinates and if they are cured

    :param x_pos_person: the x coordinate of the person's head
    :param y_pos_person: the y coordinate of the person's head
    :param cured: if the person is cured
    :return: None
    '''
    # Body
    line(x_pos_person, y_pos_person, x_pos_person, y_pos_person + 70)
    if cured:
        fill(120, 200, 120)
    else:
        fill(200, 120, 120)

    # Head
    ellipse(x_pos_person, y_pos_person, 50, 50)

    # Arms
    line(x_pos_person, y_pos_person + 30, x_pos_person + 25, y_pos_person + 60)
    line(x_pos_person, y_pos_person + 30, x_pos_person - 25, y_pos_person + 60)

    # Legs
    line(x_pos_person, y_pos_person + 70,
         x_pos_person + 20, y_pos_person + 120)
    line(x_pos_person, y_pos_person + 70,
         x_pos_person - 20, y_pos_person + 120)


def building_map(level):
    '''Display map of building

    :param level: building floor of the map
    :return: None
    '''
    background(255)
    rectMode(CORNER)
    # Display rooms on first floor of building map
    if level == 0:
        fill(0)
        textAlign(CENTER, TOP)
        textSize(40)
        text("First Floor", 480, 0)

        # Draw Rooms
        for x in range(0, width, 320):
            for y in range(60, height, 160):
                fill(255)
                rect(x, y, 320, 180)

        # Label Rooms
        fill(0)
        textAlign(CENTER, CENTER)
        textSize(30)
        text("Storage/\nMaintenance Room", 160, 140)
        text("Laboratory Storage", 160, 300)
        text("Laboratory", 160, 460)
        text("Boiler Room", 480, 140)
        text("Elevator\n(First Floor)", 480, 300)
        text("Cleaning Room", 480, 460)
        text("Front Desk", 800, 140)
        text("Entrance Lobby", 800, 300)
        text("Check-in Room", 800, 460)

        # Doorways
        fill(255)
        rect(310, 110, 20, 50)  # Storage to boiler room
        rect(630, 110, 20, 50)  # Boiler room to front desk
        rect(775, 210, 50, 20)  # Front desk to lobby
        rect(630, 275, 20, 50)  # Lobby to elevator
        rect(775, 370, 50, 20)  # Lobby to check-in
        rect(630, 430, 20, 50)  # Check-in to cleaning room
        rect(310, 430, 20, 50)  # Cleaning room to lab
        rect(135, 370, 50, 20)  # Lab to lab storage

    # Display rooms on second floor of building map
    elif level == 1:
        fill(0)
        textAlign(CENTER, TOP)
        textSize(40)
        text("Second Floor", 480, 0)

        # Draw Rooms
        fill(255)
        rect(0, 60, 640, 160)
        rect(0, 220, 320, 160)
        rect(0, 380, 640, 160)
        rect(320, 220, 320, 160)
        rect(640, 60, 320, 160)
        rect(640, 220, 320, 160)
        rect(640, 380, 320, 160)

        # Label Rooms
        fill(0)
        textAlign(CENTER, CENTER)
        textSize(30)
        text("Break Room", 320, 140)
        text("Printer Room", 160, 300)
        text("Offices", 320, 460)
        text("Elevator\n(Second Floor)", 480, 300)
        text("Washroom", 800, 140)
        text("Hallway", 800, 300)
        text("Locker Room", 800, 460)

        # Doorways
        fill(255)
        rect(630, 110, 20, 50)  # Break room to washroom
        rect(775, 210, 50, 20)  # Washroom to hallway
        rect(630, 275, 20, 50)  # Hallway to elevator
        rect(775, 370, 50, 20)  # Hallway to locker room
        rect(630, 430, 20, 50)  # Locker room to offices
        rect(135, 370, 50, 20)  # Offices to printer room
        rect(135, 210, 50, 20)  # Printer room to break room

    # Back button
    button(25, 515, 50, 50, 10, "BACK\n<--")
    # Turn map over button
    button(910, 515, 100, 50, 20, "Flip Map")