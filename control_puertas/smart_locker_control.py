import socket
import sys
import json
import codecs
from datetime import datetime
from .config import global_config 
import pickle
import os
from .create_instruction import create_instruction as ci
import time
CFG = global_config.cfg

def initial_sock():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (CFG.ip_board, CFG.port_board) #ip y puerto de la placa controladora 
    print('connecting to %s port %s' % server_address)

    sock.connect(server_address)
    return sock

def read_instruction():
    '''
    Esta funcion lee un archivo tiple pickle
    y lo retorna como una variable
    '''
    
    # Create a TCP/IP socket


    fileName = 'control_puertas/save.p'
    if os.path.exists(fileName):
        print('El archivo no existe')
    else: ci.create()   

    objects = []
    with (open("save.p", "rb")) as openfile:
        objects.append(pickle.load(openfile))
    
    return objects[0]

def open_door(number_door):
    '''
    Funcion que abre una puerta o todas 
    Esta funcion
    '''
    
    
    sock = initial_sock()

    
    keys_instruction_board = read_instruction()
    if number_door == 'all':
        
        for iter_door in range(1, 7):
            
            instruction = (keys_instruction_board[CFG.name_board][str(iter_door)]["open"])
            #se envia la instruccion
            print('instriction sending ... ->: %s'%(str(instruction)))
            sock.sendall(instruction)

            star_time = datetime.now()
            response = True
            response = ''    
            while response:
                now_time = datetime.now()-star_time
                data = sock.recv(4096)
                print("Received response:" + str(data))
                
                if now_time.total_seconds():
                    response = False
            time.sleep(2)

        
    else:
    #busco la instruccion en byte de que puerta debe abrirse
        instruction = (keys_instruction_board[CFG.name_board][str(number_door)]["open"])
        #se envia la instruccion
        print('instriction sending ... ->: %s'%(str(instruction)))
        sock.sendall(instruction)

        star_time = datetime.now()
        response = True
        response = ''    
        while response:
            now_time = datetime.now()-star_time
            data = sock.recv(4096)
            print("Received response:" + str(data))
            
            if now_time.total_seconds():
                response = False
    print('Done')
    sock.close()
    
    
def status_door(number_door):
    sock = initial_sock()
    keys_instruction_board = read_instruction()
    #busco la instruccion en byte de que puerta debe abrirse
    instruction = (keys_instruction_board[CFG.name_board][str(number_door)]["status"])
    #se envia la instruccion
    print('instriction sending ... ->: %s'%(str(instruction)))
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
    if data == (keys_instruction_board[CFG.name_board][str(number_door)]["feedback_status"]['open']):
        return 'open'
    if data == (keys_instruction_board[CFG.name_board][str(number_door)]["feedback_status"]['open']):
        return 'close'    
    #return data_str
    



    