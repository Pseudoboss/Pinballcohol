import gpiozero as gpio
import asyncio
import time

interrupt_pin = 2
code_pins = [3, 4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26]

class GameController():
    ''' Monitors and responds to changes in game state. 
    There should only be one GameController at any time.
    '''

    def __init__(self, interrupt_pin, master_pin, code_pins):
        ''' Initialize a new GameController. 

        arguments: 
            interrupt_pin: The interrupt pin for the game controller. 
                           Goes high when an element is pressed.
            master_pin: The pin that controls responsiveness of all components.
            code_pins: List of input code pins, from smallest to largest.
        '''
        self.interrupt = self.set_interrupt(interrupt_pin)
        self.master = set_master(master_pin)
        self.elements = self.set_elements(code_pins)

    def set_master(self, master_pin):
        ''' Set and configure master pin.
        '''
        master = gpio.LED(master_pin)
        return master

    def set_interrupt(self, interrupt_pin):
        ''' Set the interrupt pin for input events.
        '''

        button = gpio.Button(interrupt_pin)
        button.when_pressed = on_interrupt
        return button

    def set_elements(self, code_pins):
        ''' set element pins as inputs, and configure to read them.
        '''

        elements = {}
        for i, pin in enumerate(code_pins):
            bumper = gpio.Button(pin, pull_up = False)
            bumpers[bumper] = 2**i
        return elements

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
        ''' initialize the Bumper.
        
        arguments: 
            gc: The primary GameController.
            name: a readable name for the bumper.
            element_code: The encoded integer representing 
                          when the bumper has been hit.
            pump: The pump to run when the bumper has been hit.
        '''
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
    
    def __init__(self, gc, name, pin, run_time):
        ''' Initialize a new Pump.

        arguments: 
            gc: The primary GameController.
            name: Readable name for the pump.
            pin: Pin the pump is attached to.
            run_time: Default run time for each hit.
        '''
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

class DrinkController():
    ''' The drink controller. Manages drink mixing and pouring.
    '''

    def __init__(self):
        self.drinks = {}

class Drink():
    ''' Drink class. Defines a specific drink and its components.
    '''

    def __init__(self, dc, name, drink_dict):
        ''' Instantiate a new drink.

        arguments: 
            dc: The active Drink controller.
            name: The name of the drink
            drink_dict: The drink recipe as a ratio. 
                        Keys should be pumps, 
                        values should be floats.
        '''

        self.name = name
        self.drink_dict = drink_dict
        dc.drinks[self.name] = drink_dict

game_controller = GameController(interrupt_pin, code_pins)
drink_controller = DrinkController()

interrupt_pin = 2
self.bumpers = [3, 4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26]
    
bumper1 = Bumper('vodka', 27, 17, loop)
bumper2 = Bumper('rum', 6, 5, loop)

print('starting up.')

print('shutting down.')
