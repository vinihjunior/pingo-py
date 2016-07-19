"""
Implementation of a Serial Monitor for reading the value (LOW or HIGH) of a PushButton.

"""

import pingo
import time

board = pingo.detect.MyBoard()

buttonState = board.pins[2]
buttonState.mode = pingo.IN

while True:
	print(buttonState.state) #Serial Monitor 
	time.sleep(0.05)