"""
Name:          VFX.py
Purpose:       Defined functions for visual effects of the game

Author:        Lin.I

Created:       25/01/2019
"""


def mouse_in_button(cordin_x1, cordin_x2, cordin_y1, cordin_y2):
    '''Check if mouse is in range of the area specified by the parameters

    :param cordin_x1: mouseX must be greater than this x coordinate
    :param cordin_x2: mouseX must be less than this x coordinate
    :param cordin_y1: mouseY must be greater than this y coordinate
    :param cordin_y2: mouseY must be less than this y coordinate
    :return: if mouse is inside area
    '''
    # To return true, mouse must be inside area specified by the params
    if (mouseX > cordin_x1 and mouseX < cordin_x2 and
       mouseY > cordin_y1 and mouseY < cordin_y2):
        return True
    else:
        return False


def text_change(cordin_x1, cordin_x2, cordin_y1, cordin_y2,
                text_size):
    '''Increase text size if mouse hovers above text

    :param cordin_x1: mouseX must be greater than this x coordinate
    :param cordin_x2: mouseX must be less than this x coordinate
    :param cordin_y1: mouseY must be greater than this y coordinate
    :param cordin_y2: mouseY must be less than this y coordinate
    :param text_size: size of text
    :return: same or increased text size
    '''
    # To increase text size, mouse_in_button must return True
    if mouse_in_button(cordin_x1, cordin_x2, cordin_y1, cordin_y2):
        return text_size * 1.5
    else:
        return text_size


def fill_change(cordin_x1, cordin_x2, cordin_y1, cordin_y2, button_fill):
    '''Darken fill if mouse is within the area of the parameters

    :param cordin_x1: mouseX must be greater than this x coordinate
    :param cordin_x2: mouseX must be less than this x coordinate
    :param cordin_y1: mouseY must be greater than this y coordinate
    :param cordin_y2: mouseY must be less than this y coordinate
    :param button_fill: button colour
    :return: same or darker fill
    '''
    # To darken the fill, mouse_in_button must return True
    if mouse_in_button(cordin_x1, cordin_x2, cordin_y1, cordin_y2):
        return button_fill / 2
    else:
        return button_fill


def button(button_pos_x, button_pos_y, button_size_x, button_size_y,
           button_text_size, button_text):
    '''Draw button that text size increases when mouse hovers over button

    :param button_pos_x: button position along x-axis
    :param button_pos_y: button position along y-axis
    :param button_size_x: button size along x-axis
    :param button_size_y: button size along y-axis
    :param button_text_size: text size of button
    :param button_text: text in button
    :return: None
    '''
    # Back Button
    fill(255)
    rectMode(CENTER)
    rect(button_pos_x, button_pos_y, button_size_x, button_size_y)
    fill(0)
    # Text inside button will increase based on text_change
    textSize(text_change(button_pos_x - button_size_x/2,
                         button_pos_x + button_size_x/2,
                         button_pos_y - button_size_y/2,
                         button_pos_y + button_size_y/2,
                         button_text_size))
    textAlign(CENTER, CENTER)
    text(button_text, button_pos_x, button_pos_y)


def command_button(cordin_x, cordin_y, size_x, size_y,
                   button_fill, button_text_size, button_text):
    '''Draw button which the colour darkens when mouse hovers over button

    :param cordin_x: button position along x-axis
    :param cordin_y: button position along y-axis
    :param size_x: button size along x-axis
    :param size_y: button size along y-axis
    :param button_fill: button colour
    :param button_text_size: text size of button
    :param button_text: text in button
    :return: None
    '''
    # To darken button, fill_change must darken fill
    fill(fill_change(cordin_x - size_x/2, cordin_x + size_x/2,
                     cordin_y - size_y/2, cordin_y + size_y/2, button_fill))
    rectMode(CENTER)
    rect(cordin_x, cordin_y, size_x, size_y)
    textSize(button_text_size)
    textAlign(CENTER, CENTER)
    fill(0)
    text(button_text, cordin_x, cordin_y)


def command_buttons(using_synthesizer, show_map, show_inventory):
    '''Display command buttons for navigation

    :param using_synthesizer: if player is using synthesizer
    :param show_map: if map is being displayed
    :return: None
    '''
    # Buttons will only show up in the adventure game screen
    if not using_synthesizer and not show_map and not show_inventory:
        # North
        command_button(860, 390, 50, 50, 255, 40, "N")
        # East
        command_button(910, 440, 50, 50, 255, 40, "E")
        # South
        command_button(860, 490, 50, 50, 255, 40, "S")
        # West
        command_button(810, 440, 50, 50, 255, 40, "W")
        # Up and Down (in elevator)
        command_button(860, 440, 50, 50, 255, 12, "UP/\nDOWN")
        # Map
        command_button(50, 490, 50, 50, 255, 40, "M")
        # Inventory
        command_button(125, 490, 50, 50, 255, 40, "I")
    # Pause Game
    command_button(935, 25, 50, 50, 255, 40, "P")