from sense_hat import SenseHat
import random
from math import floor, ceil
import time
import sys
import os

sense = SenseHat()

color_blue = (0, 0, 255)
color_black = (0, 0, 0)

while True:
  try:
    pattern = ""
    matrix = []
    for r in range(0,8):
        temp = ""
        for c in range(0, 4):
            temp = temp + str(round(random.random()))

        temp = temp + temp[::-1]
        pattern = pattern + temp                   
                    
    for p in range(0,64):
        bit = int(pattern[p])
        color = color_blue if bit == 1 else color_black
        matrix.append(color)
        
    sense.set_pixels(matrix)
    time.sleep(3)
  except KeyboardInterrupt:
    print('Interrupted')
    sense.clear()
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)