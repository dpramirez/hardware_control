

import pickle

def create():
    instruction = {
        "AL2445":{
            "1": {
                "open":b"\x8A\x01\x01\x11\x9B",
                "response": b"\x80\x01\x01\x11\x91",
                "feedback_status":{
                    "open":b"\x80\x01\x01\x00\x91",
                    "close": b"\x80\x01\x01\x00\x80"
                },
                "status": b"\x80\x01\x01\x33\xb3"
            },
            "2": {
                "open":b"\x8A\x01\x02\x11\x98",
                "response": b"\x80\x01\x02\x11\x92",
                "feedback_status":{
                    "open":b"",
                    "close": b""
                },
                "status": b"\x80\x01\x02\x33\xb0"
            },
            
            "3": {
                "open":b"\x8A\x01\x03\x11\x99",
                "response": b"\x80\x01\x03\x11\x93",
                "feedback":{
                    "open":b"",
                    "close": b""
                },
                "status": b"\x80\x01\x03\x33\xb1"
            },
            "4": {
                "open":b"\x8A\x01\x04\x11\x9e",
                "close": b"",
                "feedback":{
                    "open":b"",
                    "close": b""
                },
                "status": b"\x80\x01\x04\x33\xb6"
            },
            "5": {
                "open":b"\x8A\x01\x05\x11\x9f",
                "close": b"",
                "feedback":{
                    "open":b"",
                    "close": b""
                },
                "status": b"\x80\x01\x05\x33\xb7"
            },                        
            "6": {
                "open":b"\x8A\x01\x06\x11\x9c",
                "close": b"",
                "feedback":{
                    "open":b"",
                    "close": b""
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

#number_door = b'\x06'
#print(byte_xor(byte_xor(byte_xor(b'\x8A', b'\x01'), number_door), b'\x11'))

create()

#number_door = b'\x06'
#print(byte_xor(byte_xor(byte_xor(b'\x80', b'\x01'), number_door), b'\x33'))