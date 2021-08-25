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
    #print('connecting to %s port %s' % server_address)

    sock.connect(server_address)

    #logger.info('Conexion completada con exito --> puerto %s y IP %s'%(CFG.port_board, CFG.ip_board))

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
        #logger.warning('El archivo con las instrucciones no existe.')

    else: 
        ci.create()
        #logger.info('Creando archivo de instrucciones')
   

    objects = []
    with (open("save.p", "rb")) as openfile:
        objects.append(pickle.load(openfile))
    
    return objects[0]



def status_door(number_door):
    '''
    Esta funcion retorna el estado en el que esta la puerta determinada 
    '''
    sock = initial_sock()
    keys_instruction_board = read_instruction()

    if number_door == 'all':
        #logger.info('Abriendo todas las puertas:')
        register_dicc = {}
        register = ''
        for iter_door in range(1, CFG.doors_number+1):
            #busco la instruccion en byte de que puerta debe abrirse
            instruction = (keys_instruction_board[CFG.name_board][str(iter_door)]["status"])
            #se envia la instruccion
            #print('instriction sending ... ->: %s'%(str(instruction)))
            sock.sendall(instruction)
            #logger.info('  -->Preguntando estado de puerta %s'%(iter_door))
            #logger.info('  -----> Enviando instruccion de estado %s'%(instruction))
            star_time = datetime.now()
            response = True
                
            while response:
                now_time = datetime.now()-star_time
                data = sock.recv(4096)
                #print("Received response:" + str(data))
                
                if now_time.total_seconds():
                    response = False

            #logger.info('  -----> Respuesta de instruccion de apertura %s'%(data))
            #print('byte recibido', data)
            #print('byte open', keys_instruction_board[CFG.name_board][str(iter_door)]["feedback_status"]['open'])
            if data == (keys_instruction_board[CFG.name_board][str(iter_door)]["feedback_status"]['open']):
                register += 'Door: %s -> State: Open\n'%iter_door
                register_dicc[str(iter_door)] = True
                #logger.info('  -------> Puerta: %s - Estado: Open'%(iter_door))
            if data == (keys_instruction_board[CFG.name_board][str(iter_door)]["feedback_status"]['close']):
                register += 'Door: %s -> State: Close\n'%iter_door
                register_dicc[str(iter_door)] = False

                #logger.info('  -------> Puerta: %s - Estado: Close'%(iter_door))    
            #return data_str 
            time.sleep(0.1)
        sock.close()
        #logger.info('###############################\n# Termino de estado de puertas#\n###############################')
        return register, register_dicc

    else:
            
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
        #print('byte recibido', data)
        #print('byte open', keys_instruction_board[CFG.name_board][str(number_door)]["feedback_status"]['open'])
        if data == (keys_instruction_board[CFG.name_board][str(number_door)]["feedback_status"]['open']):
            return True
        if data == (keys_instruction_board[CFG.name_board][str(number_door)]["feedback_status"]['close']):
            return False    
        #return data_str    

def open_door(number_door):
    '''
    Funcion que abre una puerta o todas 
    Esta funcion
    '''
    
    
    sock = initial_sock()

    
    keys_instruction_board = read_instruction()
    if number_door == 'all':
        # se abren todas las puertas del locker
        for iter_door in range(1, CFG.doors_number+1):
            
            instruction = (keys_instruction_board[CFG.name_board][str(iter_door)]["open"])
            #se envia la instruccion
            #print('instriction sending ... ->: %s'%(str(instruction)))
            sock.sendall(instruction)

            star_time = datetime.now()
            response = True
                
            while response:
                now_time = datetime.now()-star_time
                data = sock.recv(4096)
                #print("Received response:" + str(data))
                
                if now_time.total_seconds():
                    response = False
            time.sleep(2)

        
    else:
    #busco la instruccion en byte de que puerta debe abrirse
        instruction = (keys_instruction_board[CFG.name_board][str(number_door)]["open"])
        #se envia la instruccion
        #print('instriction sending ... ->: %s'%(str(instruction)))
        sock.sendall(instruction)

        star_time = datetime.now()
        response = True
           
        while response:
            now_time = datetime.now()-star_time
            data = sock.recv(4096)
            #print("Received response:" + str(data))
            #print(now_time)
            if now_time.total_seconds()%5>=0:
                response = False
        sock.close()
        return True

    #print('Done')
    sock.close()
    




    