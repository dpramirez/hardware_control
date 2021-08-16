from easydict import EasyDict as edict
import getpass

__C = edict() 

cfg = __C

#nombre de la placa

__C.name_board = 'AL2445'

# ip y puerto de la placa

__C.ip_board = '172.16.0.10'
__C.port_board = 6666


# cantidad de puertas del locker

__C.doors_number = 6