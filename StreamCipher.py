import random
class KeyStream:
    def __init__(self,key=1):
        self.next=key
    def rand(self):
        self.next=(1103515245*self.next + 12345)%2**31
        return self.next
    def get_key_byte(self):
        return (self.rand()//2**23)%256

def encrypt(key,message):
    length=len(message)
    return bytes([message[i]^key.get_key_byte() for i in range(length)])

def encrypt_Stream_key(key,message):
    length=min(len(key),len(message))
    return bytes([key[i]^message[i] for i in range(length)])

def transmit(cipher,likelyhood):
    b=[]
    for c in cipher:
        if random.randrange(0,likelyhood)==0:
            c=c^2**(random.randrange(0,8))
        b.append(c)
    return bytes(b)

def modification(cipher):
    mod=[0]*len(cipher)
    mod[12]=ord(' ')^ord('1')
    mod[13]=ord(' ')^ord('0')
    mod[14]=ord('1')^ord('0')
    return bytes([cipher[i]^mod[i] for i in range(len(cipher))])

def brute_force(plain,cipher):
    for i in range(2**31):
        bf=KeyStream(i)
        for j in range(len(plain)):
            xor_value=plain[j]^cipher[j]
            if xor_value != bf.get_key_byte():
                break
        else:
            return i
    return False

secret_key=random.randrange(0,2**20)
print(secret_key)
key=KeyStream(secret_key)
header="MESSAGE: "
message=header+"Send Aditya   10$"
message=message.encode()
print(message)
cipher=encrypt(key,message)
print(cipher)

#CHANGING A BIT
# cipher=transmit(cipher,5)

#CHECKING AUTHENTICATION
# cipher=modification(cipher)

#SAME KEY CANNOT BE USED
# stream_cipher_key=encrypt_Stream_key(message,cipher)

#DECRYPTING
key=KeyStream(secret_key)
message=encrypt(key,cipher)
print(message)

# key=KeyStream(12)
# message="Yo Now What".encode()
# print(message)
# cipher=encrypt(key,message)

# message_stolen=encrypt_Stream_key(stream_cipher_key,cipher)
# print(message_stolen)


bf_key=brute_force(header.encode(),cipher)
key=KeyStream(bf_key)
print(bf_key)
message=encrypt(key,cipher)
print(message)


