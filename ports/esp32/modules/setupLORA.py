# modified from https://github.com/lemariva/uPyLoRaWAN/blob/master/main.py
from config import *
from machine import Pin, SPI
from sx127x import SX127x
import axp202
###################################
#### if needed, activate axp202 ###
axp = axp202.PMU(address=axp202.AXP192_SLAVE_ADDRESS)
# axp.setDCDC1Voltage(3300) # esp32 core VDD    3v3
axp.setLDO2Voltage(3300)   # T-Beam LORA VDD   3v3
axp.setLDO3Voltage(3300)   # T-Beam GPS  VDD    3v3
axp.enablePower(axp202.AXP192_LDO2)
axp.enablePower(axp202.AXP192_LDO3)
###################################

device_spi = SPI(1, baudrate = 10000000, 
        polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
        sck = Pin(device_config['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_config['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_config['miso'], Pin.IN, Pin.PULL_UP))

lora = SX127x(device_spi, pins=device_config, parameters=lora_parameters)

# def lora (lora):
#     return lora

def receive(lora):
    while True:
        if lora.received_packet():
            print('something here')
            payload = lora.read_payload()
            print(payload)

def send(lora):
    counter = 0
    print("LoRa Sender")
    while True:
        payload = 'Hello ({0})'.format(counter)
        lora.println(payload)
        counter += 1
        sleep(5)


if __name__ == '__main__':
    pass