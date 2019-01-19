from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.low_light = True

RED = (0, 0, 200);
sense.clear(RED);
sleep(1)
sense.show_message("Hola bb", scroll_speed=0.05)
sense.show_letter("A");
sleep(1);
sense.clear(RED);
sleep(1);
sense.clear();
temp = sense.get_temperature()
print("Temperature: %s C" % temp)

# alternatives
print(sense.temp)
print(sense.temperature)

from random import uniform
num = uniform(0,10)

from random import choice
deck = ['Ace', 'King', 'Queen', 'Jack']
card = choice(deck)
