import random
def generate_key_stream(n):
    return bytes([random.randrange(0,256) for i in range(0,n)])

def xor_bytes(key_stream,message):
    length=min(len(key_stream),len(message))
    return bytes([key_stream[i]^message[i] for i in range(0,length)])
def print_data(dic):
    length=len(dic)
    for i in range(0,length):
        print(dic[i])

message="YOU ARE AWESOME"
message=message.encode()
print(len(message))
key_stream=generate_key_stream(len(message))
cipher=xor_bytes(key_stream,message)
print(key_stream)
print_data(key_stream)
print(cipher)
print(xor_bytes(key_stream,cipher))

