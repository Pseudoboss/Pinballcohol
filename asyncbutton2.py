import gpiozero as gpio
import asyncio
import time

interrupt_pin = 3
master_pin = 2
code_pins = [4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26]

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
        self.master = self.set_master(master_pin)
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
        button.when_pressed = self.on_interrupt
        return button

    def set_elements(self, code_pins):
        ''' set element pins as inputs, and configure to read them.
        '''

        elements = {}
        for i, pin in enumerate(code_pins):
            element = gpio.Button(pin, pull_up = False)
            elements[element] = 2**i
        return elements

    def on_interrupt(self):
        '''called whenever the interrupt pin goes high.'''

        time.sleep(0.001)
        read_element_code()

    def read_element_code(self):
        ''' Read the encoded bumper number from the bumper pins.
        '''

        return sum([v for k, v in self.elements if k.is_pressed])

class Bumper():
    ''' Bumper game element.
    '''

    def __init__(self, gc, name, element_code, pump):
        ''' initialize a new Bumper.
        
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
        if self.element_code in gc.elements.keys():
            raise ValueError('element_code must be unique.')
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

    def run(self, run_time = None):
        ''' Run the pump for run_time seconds.

        arguments:
            run_time: The time that the pump should run for before turning off.
        '''
        if run_time == None: 
            run_time = self.run_time
        
    @property
    def is_running(self):
        ''' Whether the pump is running or not.
        '''

        pass

class DrinkController():
    ''' The drink controller. Manages drink mixing and pouring.
        There should only be one DrinkController at a time. 
    '''

    def __init__(self):
        self.drinks = {}

    def pour_drink(self, drink):
        pass

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

game_controller = GameController(interrupt_pin, master_pin, code_pins)
drink_controller = DrinkController()
    
bumper1 = Bumper(game_controller, 'vodka', 27, 17)
bumper2 = Bumper(game_controller, 'rum', 6, 5)

print('starting up.')

print('shutting down.')
