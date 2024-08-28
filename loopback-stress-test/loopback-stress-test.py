import random
import serial
import string
from tqdm import tqdm

serial_port = '/dev/ttyS0'
serial_baud = 230400
n_bytes = 32
n_cycles = 100

with serial.Serial(serial_port, serial_baud, timeout=1) as test_port:
    
    for i in tqdm(range(n_cycles)):
        tx_bytes = bytes(''.join(random.choices(string.ascii_uppercase + string.digits, k=n_bytes)), encoding='utf-8')
        test_port.write(tx_bytes)
        rx_bytes = test_port.read(n_bytes)
        
        if tx_bytes != rx_bytes:
            print("ERROR! Data mismatch:")
            print(f"TX: {tx_bytes}")
            print(f"RX: {rx_bytes}")
            print("")
