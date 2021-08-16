#import smart_locker_control

#smart_locker_control.open_door(1)



byte_1 = b'\x8A'

byte_2 = b'\x01'
byte_3 = b'\x11'
byte_4 = b'\x11'

byte_5 = b'\x9B'

byte_example = 17
print(hex(byte_example).encode())
print(str(byte_example).encode())
print(bytes([byte_1[0] | byte_2[0] | byte_3[0] | byte_4[0]]))


exit()
number_door = 1
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (CFG.ip_board, CFG.port_board) #ip y puerto de la placa controladora 
print('connecting to %s port %s' % server_address)

sock.connect(server_address)
keys_instruction_board = read_instruction()
    #busco la instruccion en byte de que puerta debe abrirse
instruction = (keys_instruction_board[CFG.name_board][str(number_door)]["open"])
   #se envia la instruccion
sock.sendall(instruction)

star_time = datetime.now()
response = True
        
while response:
        now_time = datetime.now()-star_time
        data = sock.recv(4096)
        print("Received response:" + str(data))
        if now_time.total_seconds():
           response = False
sock.close()