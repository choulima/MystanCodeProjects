"""
File: StepUp.py
Name: Liam
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *


def main():
    #Algorithm
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_99_beepers()
    move()

def turn_right():
    for i in range(5):
        turn_left()
        turn_left()
        turn_left()

def put_99_beepers():
    for i in range(33):
        put_beeper()
        put_beeper()
        put_beeper()











# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
