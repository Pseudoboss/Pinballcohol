import gpiozero as gpio
import asyncio

class FakeBumper():
    global_cooldown = 1
    instances = []
    def __init__(self, name, power_pin, button_pin, 
                 cooldown = global_cooldown):
        self.instances.append(self)
        self.loop = asyncio.get_event_loop()
        self.name = name
        self.power = gpio.LED(power_pin)
        self.button = gpio.Button(button_pin, pull_up = False)
        self.was_pressed = False
        self.cooldown = cooldown
        self.power.on()
    async def run(self):
        if self.button.is_pressed and not self.was_pressed:
            self.on_press()
            self.was_pressed = True
        elif not self.button.is_pressed and self.was_pressed:
            self.on_release()
            self.was_pressed = False
            
    def on_press(self):
        print('{} pressed!'.format(self.name))
    def on_release(self):
        self.power.off()
        print('{} released.'.format(self.name))
        self.loop.call_later(self.cooldown, self.on_warmup)
        self.loop.call_later(self.cooldown, self.power.on)
    def on_warmup(self):
        print('{} warm.'.format(self.name))

bumper1 = FakeBumper('1', 27, 17)
bumper2 = FakeBumper('2', 6, 5)

async def mainloop(loop):
    for bumper in FakeBumper.instances:
        await bumper.run()

loop = asyncio.get_event_loop()
loop.run_until_complete(mainloop(loop))
