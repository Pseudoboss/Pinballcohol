import gpiozero as gpio
import asyncio
import time

class GameController():
    ''' Monitors and responds to changes in game state. 
    There should only be one GameController at any time.
    '''

    def __init__(self, interrupt_pin, bumper_pins):
        self.interrupt = self.set_interrupt(interrupt_pin)
        self.element_codes = self.set_elements(bumper_pins)

    def set_interrupt(self, interrupt_pin):
        '''Set the interrupt pin for on_press events.
        '''

        button = gpio.Button(interrupt_pin)
        button.when_pressed = on_interrupt
        return button

    def set_elements(self, code_pins):
        ''' set element pins as inputs, and configure to read them.
        '''

        code_pins = {}
        for i, pin in enumerate(code_pins):
            bumper = gpio.Button(pin, pull_up = False)
            bumpers[bumper] = 2**i
        return code_pins

    def on_interrupt(self):
        '''called whenever the interrupt pin goes high.'''

        time.sleep(0.001)
        read_bumpers()

    def read_element_code(self):
        ''' Read the encoded bumper number from the bumper pins.
        '''

        return sum([v for k, v in self.bumpers if k.is_pressed])

class Bumper():
    ''' Bumper game element.
    '''

    def __init__(self, gc, name, element_code, pump):
        self.name = name
        self.element_code = element_code
        self.pump = pump
        gc.elements[self.element_code] = self        

    def on_hit(self):
        ''' Called when the bumper has been hit.
        '''
        print('{} has been hit!'.format(self.name))
        self.pump.run()

class Pump():
    ''' Pump game element.
    '''
    
    def __init__(self, name, pin, run_time):
        self.name = name
        self.pin = gpio.LED(pin)
        self.run_time = run_time

    def run(self, run_time = self.run_time):
        ''' Run the pump for run_time seconds.
        '''
        pass

    @property
    def is_running(self):
        ''' Whether the pump is running or not.
        '''
        pass

interrupt_pin = 2
self.bumpers = [3, 4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26]
    
bumper1 = Bumper('vodka', 27, 17, loop)
bumper2 = Bumper('rum', 6, 5, loop)

loop.run_forever()
print('shut down.')
