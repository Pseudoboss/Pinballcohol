#! /usr/bin/python3 

import gpiozero as gpio
import asyncio
import time

interrupt_pin = 3
master_pin = 2
code_pins = [4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26]

max_pour_time = 10
min_pour_time = 1
pour_coef = 1/10000

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
        ''' Read the encoded element number from the element pins.
        '''

        return sum([v for k, v in self.elements if k.is_pressed])

class Bumper():
    ''' Bumper game element.
    '''

    def __init__(self, gc, name, element_code):
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
        self._start()
        self.call_later(run_time, self._stop)
    
    def _start(self):
        ''' Internal use only. 
            Start the physcal pump running.
        '''

        if not self.is_running:
            self.pin.on()
        else: 
            raise PumpError("Pump must be off to call 'start'.")
    
    def _stop(self):
        ''' Internal use only.
            stop the physical pump running. 
        ''' 

        if self.is_running:
            self.pin.off()
        else:
            raise PumpError("pump must be on to call 'stop'.")
       
    @property
    def is_running(self):
        ''' True if the pump is running. False otherwise.
        '''

        return self.pin.is_lit


class DrinkController():
    ''' The drink controller. Manages drink mixing and pouring.
        There should only be one DrinkController at a time. 
    '''

    def __init__(self, max_pour_time, min_pour_time, pour_coef):
        ''' Instantiate a new DrinkController.
        
        arguments: 
            max_pour_time: Max pour time to prevent overflowing.
            min_pour_time: Min pour time, to prevent disappointment. 
            pour_coef: Pour coefficient to determine how score 
                       goes to pour time.
        '''
        self.score = 0
        drink_scores = {}

        self.max_pour_time = max_pour_time
        self.min_pour_time = min_pour_time
        self.pour_coef = pour_coef
        pour_time = self.score*self.pour_coef
        pour_time = sorted([self.min_pour_time, 
                            pour_time, 
                            self.max_pour_time])[1]
        drink.pour(pour_time)

    def determine_drink(self):
        winning_drink = None
        winning_score = 0
        for drink, score in self.drink_scores:
            if score > winning_score:
                winning_drink = drink
                winning_score = score
        self.pour_drink(winning_drink)

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
        dc.drink_scores[self] = 0

    @property
    def drink_dict(self):
        ''' Dictionary with pumps and ingredients. Values have been normalized.
        '''
        return self._drink_dict
    
    @drink_dict.setter
    def drink_dict(self, value):
        # Normalize the values in value to 1. 
        total = sum(value.values())
        for k, v in value:
            value[k] = v/total
        self._drink_dict = value

game_controller = GameController(interrupt_pin, master_pin, code_pins)
drink_controller = DrinkController(max_pour_time, min_pour_time, pour_coef)
    
bumper1 = Bumper(game_controller, 'vodka', 27, 17)
bumper2 = Bumper(game_controller, 'rum', 6, 5)

print('starting up.')

print('shutting down.')
