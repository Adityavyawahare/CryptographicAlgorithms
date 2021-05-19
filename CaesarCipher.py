def generate_keys(n):
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key={}
    count=0
    for c in letters:
        key[c]=letters[(count+n)%len(letters)]
        count+=1
    return key

def decrypt_keys(key):
    dkey={}
    for c in key:
        dkey[key[c]]=c
    return dkey

def encrypt(key,message):
    s=""
    for m in message:
        if m==" ":
            s+=m
            continue
        s+=key[m]
    return s

k=int(input("Enter key value :"))
message=input("Enter message to encrypt :")
key=generate_keys(k)
# print(key)
#ENCRYPTION OF DATA
string=encrypt(key,message)
#double encryption
# string=encrypt(key,string)
print(string)
#DECRYPTION OF DATA
# key2=decrypt_keys(key)
# print(key)
# print(key2)
# string=encrypt(key2,string)
# print(string)

#ATTACK ON A CIPHER
for i in range(0,26):
    dkey=generate_keys(i)
    print(encrypt(dkey,string))