

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
                "response": b"\x80\x01\x07\x11\x97",
                "feedback_status":{
                    "open": b"\x80\x01\x07\x11\x97",
                    "close": b"\x80\x01\x07\x00\x86"
                },
                "status": b"\x80\x01\x07\x33\xb5"
            },                        
            "8": {
                "open":b"\x8A\x01\x08\x11\x92",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x08\x11\x98",
                    "close": b"\x80\x01\x08\x00\x89"
                },
                "status": b"\x80\x01\x08\x33\xba"
            },                        
            "9": {
                "open":b"\x8A\x01\x09\x11\x93",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x09\x11\x99",
                    "close": b"\x80\x01\x09\x00\x88"
                },
                "status": b"\x80\x01\x09\x33\xbb"
            },                        
            "10": {
                "open":b"\x8A\x01\x0A\x11\x90",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x0A\x11\x9a",
                    "close": b"\x80\x01\x0A\x00\x8b"
                },
                "status": b"\x80\x01\x0A\x33\xb8"
            },                        
            "11": {
                "open":b"\x8A\x01\x0B\x11\x91",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x0B\x11\x9b",
                    "close": b"\x80\x01\x0B\x00\x8a"
                },
                "status": b"\x80\x01\x0B\x33\xb9"
            },                        
            "12": {
                "open":b"\x8A\x01\x0C\x11\x96",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x0C\x11\x9c",
                    "close": b"\x80\x01\x0C\x00\x8d"
                },
                "status": b"\x80\x01\x0C\x33\xbe"
            },                        
            "13": {
                "open":b"\x8A\x01\x0D\x11\x97",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x0D\x11\x9d",
                    "close": b"\x80\x01\x0D\x00\x8c"
                },
                "status": b"\x80\x01\x0D\x33\xbf"
            },                        
            "14": {
                "open":b"\x8A\x01\x0E\x11\x94",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x0E\x11\x9e",
                    "close": b"\x80\x01\x0E\x00\x8f"
                },
                "status": b"\x80\x01\x0E\x33\xbc"
            },                        
            "15": {
                "open":b"\x8A\x01\x0F\x11\x95",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x0F\x11\x9f",
                    "close": b"\x80\x01\x0F\x00\x8e"
                },
                "status": b"\x80\x01\x0F\x33\xbd"
            },                        
            "16": {
                "open":b"\x8A\x01\x10\x11\x8A",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x10\x11\x80",
                    "close": b"\x80\x01\x10\x00\x91"
                },
                "status": b"\x80\x01\x10\x33\xa2"
            },                        
            "17": {
                "open":b"\x8A\x01\x11\x11\x8b",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x11\x11\x81",
                    "close": b"\x80\x01\x11\x00\x90"
                },
                "status": b"\x80\x01\x11\x33\xa3"
            },                        
            "18": {
                "open":b"\x8A\x01\x12\x11\x88",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x12\x11\x82",
                    "close": b"\x80\x01\x12\x00\x93"
                },
                "status": b"\x80\x01\x12\x33\xa0"
            },                        
            "19": {
                "open":b"\x8A\x01\x13\x11\x89",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x13\x11\x83",
                    "close": b"\x80\x01\x13\x00\x92"
                },
                "status": b"\x80\x01\x13\x33\xa1"
            },                        
            "20": {
                "open":b"\x8A\x01\x14\x11\x8e",
                "response": b"",
                "feedback_status":{
                    "open": b"\x80\x01\x14\x11\x84",
                    "close": b"\x80\x01\x14\x00\x95"
                },
                "status": b"\x80\x01\x14\x33\xa6"
            }                         
        }
    }


    dbfile = open("save.p", "wb")
    pickle.dump(instruction, dbfile)
    dbfile.close()

    return True

def byte_xor(bar1, bar2):
        return bytes([_a ^ _b for _a, _b in zip(bar1, bar2)])

number_door = b'\x0E'
#print(byte_xor(byte_xor(byte_xor(b'\x80', b'\x01'), number_door), b'\x00'))

#for i in range(1, 21):
    #number_door = i.to_bytes(1, byteorder='big')
    #print(i, byte_xor(byte_xor(byte_xor(b'\x80', b'\x01'), number_door), b'\x33'))
    

create()




#number_door = b'\x06'
#print(byte_xor(byte_xor(byte_xor(b'\x80', b'\x01'), number_door), b'\x33'))