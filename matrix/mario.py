from sense_hat import SenseHat
from time import sleep
import sys
import os

sense = SenseHat()

black = (0, 0, 0)
blue = (0, 0, 255)

x_pos = 0
y_pos = 0
n_rows = 7
n_cols = 7
clear_before_every_loop = True

while x_pos <= n_cols and y_pos <= n_rows:
  try:
    if clear_before_every_loop:
      sense.clear()
    sense.set_pixel(x_pos, y_pos, blue)
    y_pos = (y_pos + 1) if (x_pos + 1 == n_cols + 1) else (y_pos)
    x_pos = (x_pos + 1) if (x_pos + 1 <= n_cols) else (0)
    sleep(0.1)
  except KeyboardInterrupt:
    print('Interrupted')
    sense.clear()
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

sense.clear()