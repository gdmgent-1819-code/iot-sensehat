from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Generate a random colour
def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)

n_loops = 3
c_loop = 1

while c_loop <= n_loops:
  sense.show_letter("N", pick_random_colour())
  sleep(1)
  sense.show_letter("M", pick_random_colour())
  sleep(1)
  sense.show_letter("D", pick_random_colour())
  sleep(1)

  c_loop += 1

sense.clear()