import random
def generate_key():
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletters=list(letters)
    key={}
    for c in letters:
        key[c]=cletters.pop(random.randint(0,len(cletters)-1))
    return key

def encrypt(message,key):
    string=""
    for c in message:
        if c==" ":
            string+=c
            continue
        string+=key[c]
    return string

def decrypt_keys(key):
    dkey={}
    for i in key:
        dkey[key[i]]=i
    return dkey 

keys=generate_key()
print(keys)
str1=input("Enter your message :")
#encrypt message
string=encrypt(str1,keys)
print(string)
#decrypt message
dkey=decrypt_keys(keys)
str2=encrypt(string,dkey)
print(str2)
