import gpiozero as gpio
from signal import pause
import asyncio

class InputController():
    def __init__(self, interrupt_pin, input_pin_list):
        self.interrupt = gpio.Button(button_pin, pull_up)
        self.interrupt.on_press = self.on_interrupt
        self.bumpers = {}

        self.inputs = {}
        for index, pin in enumerate(input_pin_list):
            button = gpio.Button(pin)
            self.inputs[button] = 2**index

    def on_interrupt(self): 
        self.bumpers[self.read_inputs()]()
    
    def read_inputs(self):
        return sum([value for button, value 
                    in self.inputs.items() if button.is_pressed])

class FakeBumper():
    global_cooldown = 1
    def __init__(self, controller, name, input_number, 
                 cooldown = global_cooldown): 
        self.input_number = input_number
        self.loop = asyncio.get_event_loop()
        self.name = name
        self.controller.bumpers[self.input_number] = self.on_hit

    def on_hit(self):
        print('{} was hit!'.format(self.name))


bumper1 = FakeBumper('1', 27, 17)
bumper2 = FakeBumper('2', 6, 5)

loop = asyncio.get_event_loop()
loop.run_until_complete(mainloop(loop))
