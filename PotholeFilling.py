"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at the (2,1)
    Post-condition: Karel is at the (2,7)
    """
    for i in range(3):
        go_in()
        put_99()
        go_out()

def go_in():
    """
    Pre-condition: Karel is at the upper left of the pothole,facing East
    Post-condition: Karel is in the pothole,facing South
    """
    move()
    turn_right()
    move()

def turn_right():
    """
    Pre-condition: Karel faces North
    Pre-condition: Karel faces East
    """
    for i in range(3):
        turn_left()
def put_99():
    """
    Karel will put 99 beepers
    """
    for i in range(99):
        put_beeper()

def go_out():
    """
    Pre-condition: Karel is in the pothole,facing South
    Post-condition: Karel is at the upper left of the pothole,facing East
    """
    turn_around()
    move()
    turn_right()
    move()

def turn_around():
    """
    Pre-condition: Karel faces South
    Post-condition: Karel faces North
    """
    for i in range(2):
        turn_left()




# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
