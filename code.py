import board
import digitalio
import analogio
# import time
import usb_hid
from gamepad import Gamepad

from adafruit_hid.mouse import Mouse

gamepad = Gamepad(usb_hid.devices)

def get_joystick_value(analog_input):
    # Convert 16-bit analog input to -127 to 127 range
    return int((analog_input.value / 65535 * 254) - 127)

button_values = (
   1,
   2,
   4,
   8,
   16,
   32,
   64,
)

# Setup buttons as inputs with pull-ups
joystick_btn = digitalio.DigitalInOut(board.GP0)
joystick_btn.direction = digitalio.Direction.INPUT
joystick_btn.pull = digitalio.Pull.UP

button1 = digitalio.DigitalInOut(board.GP1)
button1.direction = digitalio.Direction.INPUT

button2 = digitalio.DigitalInOut(board.GP2)
button2.direction = digitalio.Direction.INPUT

button3 = digitalio.DigitalInOut(board.GP3)
button3.direction = digitalio.Direction.INPUT

button4 = digitalio.DigitalInOut(board.GP4)
button4.direction = digitalio.Direction.INPUT

select_btn = digitalio.DigitalInOut(board.GP5)
select_btn.direction = digitalio.Direction.INPUT

start_btn = digitalio.DigitalInOut(board.GP6)
start_btn.direction = digitalio.Direction.INPUT

# Setup joystick as analog inputs
joystick_x = analogio.AnalogIn(board.A0)
joystick_y = analogio.AnalogIn(board.A1)

counter = 0

while True:
  if counter ==  50:
    print("------------")
    print(f"Joy X: {get_joystick_value(joystick_x)}")
    print(f"Joy Y: {get_joystick_value(joystick_y)}")
    print(f"Joy Btn: {not joystick_btn.value}")
    print(f"Btn 1: {button1.value}")
    print(f"Btn 2: {button2.value}")
    print(f"Btn 3: {button3.value}")
    print(f"Btn 4: {button4.value}")
    print(f"Select: {select_btn.value}")
    print(f"Start: {start_btn.value}")
    print("------------")
    counter = 0
    
  counter = counter + 1

  button_state = (
    not joystick_btn.value,
    button1.value,
    button2.value,
    button3.value,
    button4.value,
    select_btn.value,
    start_btn.value,
    )
  for i, button_state in enumerate(button_state):
    gamepad_button_num = button_values[i]
    if not button_state:
      gamepad.release_buttons(gamepad_button_num)
    else:
      gamepad.press_buttons(gamepad_button_num)
  
  gamepad.move_joysticks(get_joystick_value(joystick_x), get_joystick_value(joystick_y))