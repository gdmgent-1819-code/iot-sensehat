from sense_hat import SenseHat
from time import sleep
import sys
import os

sense = SenseHat()

Bk = (0,0,0)
Wh = (255,255,255)
Rd = (255, 0, 77)
Bl = (41, 173, 255)
Br = (187, 90, 59)
Pk = (255, 208, 174)
Yl = (250, 252, 44)

mario = [
    Bk, Bk, Bk, Rd, Rd, Rd, Wh, Bk,
    Bk, Bk, Bk, Rd, Rd, Rd, Rd, Rd,
    Bk, Bk, Br, Pk, Br, Bk, Pk, Bk,
    Bk, Bk, Br, Pk, Pk, Br, Br, Pk,
    Bk, Bk, Bk, Br, Pk, Pk, Pk, Bk,
    Bk, Rd, Rd, Yl, Bl, Bl, Yl, Bk,
    Wh, Bk, Bl, Bl, Bl, Bl, Bk, Bl,
    Bk, Bk, Br, Bk, Bk, Bk, Rd, Bk  
    
]

mario_jump = [
    Bk, Bk, Bk, Rd, Rd, Rd, Rd, Rd,
    Bk, Bk, Br, Pk, Br, Bk, Pk, Bk,
    Bk, Bk, Br, Pk, Pk, Br, Br, Pk,
    Bk, Bk, Bk, Br, Pk, Pk, Pk, Bk,
    Wh, Rd, Bl, Yl, Bl, Bl, Yl, Bl,
    Bk, Bk, Br, Bk, Bk, Bk, Rd, Bk,  
    Bk, Bk, Bk, Bk, Bk, Bk, Bk, Bk,   
    Bk, Bk, Bk, Bk, Bk, Bk, Bk, Bk    
]

jump = False;

while True:
  try:
    if jump:
      sense.set_pixels(mario_jump)
    else :
      sense.set_pixels(mario)
  
    sleep(1)
    jump = True if (jump == False) else False

  except KeyboardInterrupt:
    print('Interrupted')
    sense.clear()
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

sense.clear()