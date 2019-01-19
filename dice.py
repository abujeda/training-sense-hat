from sense_hat import SenseHat
from time import sleep
from random import choice
import sys

RUN_PROGRAM = True;

sense = SenseHat()
sense.low_light = True

X = [55, 0, 0]  # Red
O = [0, 0, 0]  # Red

DICE_ONE = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
]

DICE_TWO = [
        O, O, O, O, O, O, O, O,
        O, X, X, O, O, O, O, O,
        O, X, X, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, X, X, O,
        O, O, O, O, O, X, X, O,
        O, O, O, O, O, O, O, O,
]

DICE_THREE = [
        X, X, O, O, O, O, O, O,
        X, X, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, X, X,
        O, O, O, O, O, O, X, X,
]

DICE_FOUR = [
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
]

DICE_FIVE = [
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
        O, O, O, O, O, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, O, O, O, O, O,
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
]

DICE_SIX = [
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
        O, O, O, O, O, O, O, O,
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
        O, O, O, O, O, O, O, O,
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
]

NUMBERS = [DICE_ONE, DICE_TWO, DICE_THREE, DICE_FOUR, DICE_FIVE, DICE_SIX]
def endDice():
    global RUN_PROGRAM;
    RUN_PROGRAM = False;

def readMovement():
    while True:
        acceleration = sense.get_accelerometer_raw()
        x = abs(round(acceleration['x'], 0))
        y = abs(round(acceleration['y'], 0))
        z = abs(round(acceleration['z'], 0))
        #print("x={0}, y={1}, z={2}".format(x, y, z))
        if (x > 2 or y > 2 or z > 2):
            return

def animation():
    sense.show_letter("3");
    sleep(1)
    sense.show_letter("2");
    sleep(1)
    sense.show_letter("1");
    sleep(1)

sense.stick.direction_middle = endDice

while RUN_PROGRAM:
    readMovement();
    animation();
    randomNumber = choice(NUMBERS);
    sense.set_pixels(randomNumber);
    print(RUN_PROGRAM);
    sleep(3)

sense.clear(O);
