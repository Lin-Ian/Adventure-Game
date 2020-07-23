"""
Name:          items.py
Purpose:       Defined functions to draw items that
               player needs to collect in the rooms

Author:        Lin.I

Created:       25/01/2019
"""
from VFX import *


# Create variable for a list of items
item_list = []

# Create item and append to list of items
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

# Create variable for a list of items player has
user_items = []


def draw_items(current_room):
    '''Draw items player needs to find in the rooms

    :param current_room: the room the player is in
    :return: None
    '''
    rectMode(CENTER)
    textAlign(CENTER, CENTER)
    # Check if player does not have item and if item is in room
    if (item_list[current_room] not in user_items and
       item_list[current_room][1] is not None):
        if current_room == 2:
            draw_hazmat_suit(500, 300)
        elif current_room == 4:
            draw_needles(500, 300)
        elif current_room == 5:
            draw_cleaning_products(500, 300)
        elif current_room == 7:
            draw_plant(500, 300)
        elif current_room == 10:
            draw_water(440, 280)
        elif current_room == 11:
            draw_soap(500, 300)
        elif current_room == 12:
            draw_food(500, 300)
        elif current_room == 13:
            draw_toner(500, 300)
        elif current_room == 14:
            draw_money(500, 300)
        elif current_room == 15:
            draw_credentials(500, 300)


def draw_hazmat_suit(x_pos, y_pos):
    '''Draw hazmat suit based on the x and y coordinates given

    :param x_pos: x coordinate of item
    :param y_pos: y coordinate of item
    :return: None
    '''
    fill(255)
    rect(x_pos, y_pos, 100, 100)
    fill(0)
    textSize(20)
    text("Hazmat\n Suit", x_pos, y_pos)


def draw_needles(x_pos, y_pos):
    '''Draw needles based on the x and y coordinates given

    :param x_pos: x coordinate of item
    :param y_pos: y coordinate of item
    :return: None
    '''
    fill(255)
    rect(x_pos, y_pos, 100, 100)
    fill(0)
    textSize(20)
    text("Needles", x_pos, y_pos)


def draw_cleaning_products(x_pos, y_pos):
    '''Draw cleaning products based on the x and y coordinates given

    :param x_pos: x coordinate of item
    :param y_pos: y coordinate of item
    :return: None
    '''
    fill(255)
    rect(x_pos, y_pos, 100, 100)
    fill(0)
    textSize(20)
    text("Cleaning\nProducts", x_pos, y_pos)


def draw_plant(x_pos, y_pos):
    '''Draw plants based on the x and y coordinates given

    :param x_pos: x coordinate of item
    :param y_pos: y coordinate of item
    :return: None
    '''
    fill(255)
    rect(x_pos, y_pos, 100, 100)
    fill(0)
    textSize(20)
    text("Plants", x_pos, y_pos)


def draw_water(x_pos, y_pos):
    '''Draw water based on the x and y coordinates given

    :param x_pos: x coordinate of item
    :param y_pos: y coordinate of item
    :return: None
    '''
    fill(255)
    rect(x_pos, y_pos, 100, 100)
    fill(0)
    textSize(20)
    text("Water", x_pos, y_pos)
    # if item_list[14] not in user_items:
    #     text("You need money for this item", x_pos, y_pos+100)


def draw_soap(x_pos, y_pos):
    '''Draw soap based on the x and y coordinates given

    :param x_pos: x coordinate of item
    :param y_pos: y coordinate of item
    :return: None
    '''
    fill(255)
    rect(x_pos, y_pos, 100, 100)
    fill(0)
    textSize(20)
    text("Soap", x_pos, y_pos)


def draw_food(x_pos, y_pos):
    '''Draw food based on the x and y coordinates given

    :param x_pos: x coordinate of item
    :param y_pos: y coordinate of item
    :return: None
    '''
    fill(255)
    rect(x_pos, y_pos, 100, 100)
    fill(0)
    textSize(20)
    text("Food", x_pos, y_pos)


def draw_toner(x_pos, y_pos):
    '''Draw toner based on the x and y coordinates given

    :param x_pos: x coordinate of item
    :param y_pos: y coordinate of item
    :return: None
    '''
    fill(255)
    rect(x_pos, y_pos, 100, 100)
    fill(0)
    textSize(20)
    text("Toner", x_pos, y_pos)


def draw_money(x_pos, y_pos):
    '''Draw money based on the x and y coordinates given

    :param x_pos: x coordinate of item
    :param y_pos: y coordinate of item
    :return: None
    '''
    fill(255)
    rect(x_pos, y_pos, 100, 100)
    fill(0)
    textSize(20)
    text("Money", x_pos, y_pos)


def draw_credentials(x_pos, y_pos):
    '''Draw credentials based on the x and y coordinates given

    :param x_pos: x coordinate of item
    :param y_pos: y coordinate of item
    :return: None
    '''
    fill(255)
    rect(x_pos, y_pos, 100, 100)
    fill(0)
    textSize(20)
    text("Credentials", x_pos, y_pos)


def inventory():
    background(255)
    textSize(40)
    textAlign(CENTER, CENTER)
    fill(0)
    text("Inventory", 480, 30)

    rectMode(CORNER)
    fill(255)
    for x in range(100, 760, 380):
        for y in range(100, 450, 70):
            rect(x, y, 380, 70)

    fill(0)
    # Display Hazmat suit if in inventory
    if (item_list[2] in user_items and item_list[2][1] is not None):
        text(item_list[2][1], 290, 135)
    # Display Needles if in inventory
    if (item_list[4] in user_items and
       item_list[4][1] is not None):
        text(item_list[4][1], 290, 205)
    # Display Cleaning Products if in inventory
    if (item_list[5] in user_items and
       item_list[5][1] is not None):
        text(item_list[5][1], 290, 275)
    # Display Plants if in inventory
    if (item_list[7] in user_items and
       item_list[7][1] is not None):
        text(item_list[7][1], 290, 345)
    # Display Water if in inventory
    if (item_list[10] in user_items and
       item_list[10][1] is not None):
        text(item_list[10][1], 290, 415)
    # Display Soap if in inventory
    if (item_list[11] in user_items and
       item_list[11][1] is not None):
        text(item_list[11][1], 670, 135)
    # Display Food if in inventory
    if (item_list[12] in user_items and
       item_list[12][1] is not None):
        text(item_list[12][1], 670, 205)
    # Display Toner if in inventory
    if (item_list[13] in user_items and
       item_list[13][1] is not None):
        text(item_list[13][1], 670, 275)
    # Display Money if in inventory
    if (item_list[14] in user_items and
       item_list[14][1] is not None):
        text(item_list[14][1], 670, 345)
    # Display Credentials if in inventory
    if (item_list[15] in user_items and
       item_list[15][1] is not None):
        text(item_list[15][1], 670, 415)

    # Back button from inventory
    button(50, 490, 100, 100, 20, "BACK\n<--")