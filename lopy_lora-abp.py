from network import LoRa
from time import sleep

import socket
import binascii
import struct

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, sf=7, tx_power=14)

lora.BW_125KHZ
lora.CODING_4_5

# create an ABP authentication params
dev_addr = struct.unpack(">l", binascii.unhexlify('XX XX XX XX'.replace(' ','')))[0]
nwk_swkey = binascii.unhexlify('XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX'.replace(' ',''))
app_swkey = binascii.unhexlify('XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX'.replace(' ',''))

# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking.
s.setblocking(True)

while True:
    #Do you stuff make data and then send in a loop
    print("sending")
    s.send('hello')
    print("done")
    sleep(5)
