

import pickle

def create():
    instruction = {
        "AL2445":{
            "1": {
                "open":b"\x8A\x01\x01\x11\x9B",
                "response": b"\x80\x01\x01\x11\x91",
                "feedback_status":{
                    "open":b"\x80\x01\x01\x11\x91",
                    "close": b"\x80\x01\x01\x00\x80"
                },
                "status": b"\x80\x01\x01\x33\xb3"
            },
            "2": {
                "open":b"\x8A\x01\x02\x11\x98",
                "response": b"\x80\x01\x02\x11\x92",
                "feedback_status":{
                    "open":b"\x80\x01\x02\x11\x92",
                    "close": b"\x80\x01\x02\x00\x83"
                },
                "status": b"\x80\x01\x02\x33\xb0"
            },
            
            "3": {
                "open":b"\x8A\x01\x03\x11\x99",
                "response": b"\x80\x01\x03\x11\x93",
                "feedback_status":{
                    "open": b"\x80\x01\x03\x11\x93",
                    "close": b"\x80\x01\x03\x00\x82"
                },
                "status": b"\x80\x01\x03\x33\xb1"
            },
            "4": {
                "open":b"\x8A\x01\x04\x11\x9e",
                "response": b"",
                "feedback_status":{
                    "open":  b"\x80\x01\x04\x11\x94",
                    "close": b"\x80\x01\x04\x00\x85"
                },
                "status": b"\x80\x01\x04\x33\xb6"
            },
            "5": {
                "open":b"\x8A\x01\x05\x11\x9f",
                "response": b"",
                "feedback_status":{
                    "open":  b"\x80\x01\x05\x11\x95",
                    "close": b"\x80\x01\x05\x00\x84"
                },
                "status": b"\x80\x01\x05\x33\xb7"
            },                        
            "6": {
                "open":b"\x8A\x01\x06\x11\x9c",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x06\x11\x96",
                    "close": b"\x80\x01\x06\x00\x87"
                },
                "status": b"\x80\x01\x06\x33\xb4"
            }, # Desde aca los feedback no estan buenos hay que arreglarlos                       
            "7": {
                "open":b"\x8A\x01\x07\x11\x9d",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x06\x11\x96",
                    "close": b"\x80\x01\x06\x00\x87"
                },
                "status": b"\x80\x01\x06\x33\xb4"
            },                        
            "8": {
                "open":b"\x8A\x01\x08\x11\x92",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x06\x11\x96",
                    "close": b"\x80\x01\x06\x00\x87"
                },
                "status": b"\x80\x01\x06\x33\xb4"
            },                        
            "9": {
                "open":b"\x8A\x01\x09\x11\x93",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x06\x11\x96",
                    "close": b"\x80\x01\x06\x00\x87"
                },
                "status": b"\x80\x01\x06\x33\xb4"
            },                        
            "10": {
                "open":b"\x8A\x01\x0A\x11\x90",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x06\x11\x96",
                    "close": b"\x80\x01\x06\x00\x87"
                },
                "status": b"\x80\x01\x06\x33\xb4"
            },                        
            "11": {
                "open":b"\x8A\x01\x0B\x11\x91",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x06\x11\x96",
                    "close": b"\x80\x01\x06\x00\x87"
                },
                "status": b"\x80\x01\x06\x33\xb4"
            },                        
            "12": {
                "open":b"\x8A\x01\x0C\x11\x96",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x06\x11\x96",
                    "close": b"\x80\x01\x06\x00\x87"
                },
                "status": b"\x80\x01\x06\x33\xb4"
            }                 
        }
    }


    dbfile = open("save.p", "wb")
    pickle.dump(instruction, dbfile)
    dbfile.close()

    return True

def byte_xor(bar1, bar2):
        return bytes([_a ^ _b for _a, _b in zip(bar1, bar2)])

number_door = b'\x0C'
print(byte_xor(byte_xor(byte_xor(b'\x8A', b'\x01'), number_door), b'\x11'))


create()




#number_door = b'\x06'
#print(byte_xor(byte_xor(byte_xor(b'\x80', b'\x01'), number_door), b'\x33'))