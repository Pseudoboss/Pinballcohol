import gpiozero as gpio
import concurrent.futures as futures
import time

class GameController():
    ''' Monitors and responds to changes in game state. 
    There should only be one GameController at any time.
    '''
    def __init__(self, interrupt_pin, bumper_pins):
        self.interrupt = self.set_interrupt(interrupt_pin)
        self.bumper_codes = self.set_bumpers(bumper_pins)

    def set_interrupt(self, interrupt_pin):
        '''Set the interrupt pin for on_press events.
        '''
        button = gpio.Button(interrupt_pin)
        button.when_pressed = on_interrupt
        return button

    def set_bumpers(self, bumper_pins):
        ''' set bumper pins as inputs, and configure to read them.
        '''
        bumper_codes = {}
        for i, pin in enumerate(bumper_pins):
            bumper = gpio.Button(pin, pull_up = False)
            bumpers[bumper] = 2**i
        return bumper_codes

    def on_interrupt(self):
        '''called whenever the interrupt pin goes high.'''
        time.sleep(0.001)
        read_bumpers()

    def read_bumpers(self):
        ''' Read the encoded bumper number from the bumper pins.
        '''
        return sum([v for k, v in self.bumpers if k.is_pressed])

class FakeBumper():
    def __init__(self, name, bumper_number):
        pass

interrupt_pin = 2
self.bumpers = [3, 4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26]
    
bumper1 = FakeBumper('vodka', 27, 17, loop)
bumper2 = FakeBumper('rum', 6, 5, loop)

loop.run_forever()
print('shut down.')
