"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():

    move()
    double_beeper()
    move_back()
    go_home()


def double_beeper():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        turn_around()
        move()
        turn_around()


def move_back():
    move()
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()


def move_back():
    move()
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()


def go_home():
    turn_around()
    move()
    move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()
    """
    Karel will double the beepers
    """
















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)