# Use the Pin method from the machine software library
from machine import Pin
# Define the inputs and outputs and assign them to software objects
# First argument is a GPIO pin number, rather than a physical pin number
led1 = Pin(18, Pin.OUT)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)
led2 = Pin(19, Pin.OUT)
sw4 = Pin(13, Pin.IN, Pin.PULL_DOWN)
led3 = Pin(20, Pin.OUT)
sw3 = Pin(12, Pin.IN, Pin.PULL_DOWN)
led4 = Pin(21, Pin.OUT)
sw2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
led5 = Pin('LED', Pin.OUT)
sw1 = Pin(10, Pin.IN, Pin.PULL_DOWN)
#while True:
# Control the LED output values, based on the received button input
#    if sw5.value() == 1:
#        led1.on()
#    else:
#        led1.off()
#    if sw4.value() == 1:
#        led2.on()
#    else:
#        led2.off()
#    if sw3.value() == 1:
#        led3.on()
#    else:
#        led3.off()
#    if sw2.value() == 1:
#        led4.on()
#    else:
#        led4.off()
#    if sw1.value() == 1:
#        led5.on()
#    else:
#        led5.off()


if (sw5.PULL_UP==0):
    if (sw5.value()==1):
        if (sw5.value()==0):
            led1.on()
        else:
            led1.off()
    else:
        led1.off()
else:
    led1.off()
        
         