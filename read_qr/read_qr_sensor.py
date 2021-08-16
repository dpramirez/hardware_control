import time
from serial import Serial

import socket
import sys




def serial_read_qr():
    """
    Conexion directa del QR a la espera 
    """
    ser = Serial(
        port='/dev/ttyACM0',
        baudrate=9600
    )
    ser.isOpen()
    print(ser.is_open)
    print("connected to: " + ser.portstr)
    while True:
        return ser.read(22)

    
def socket_comunication():
    # configure the serial connections (the parameters differs on the device you are connecting to)
    ser = Serial(
        port='/dev/ttyACM0',
        baudrate=9600
    )

    ser.isOpen()

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    while True:
        try:

            # Send data
            message = ser.read(22)
            print('sending {!r}'.format(message))
            sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))

        finally:
            print('closing socket')
            #sock.close()

print(serial_read_qr())            