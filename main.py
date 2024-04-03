import keyboard
import pyperclip

array = ['hello','bye']
num = 0
while True:
    for x in range(len(array)):
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'alt': 
                print('pressed')
                pyperclip.copy(array[num])
                num +=1
                if num >= len(array):
                    num = 0