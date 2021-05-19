import hashlib
import base64


iterations = 45454
salt_alice = "43424".encode()
password_alice = "password".encode()
print(hashlib.pbkdf2_hmac("sha512", password_alice, salt_alice, iterations, dklen=128))
print()
value_alice = base64.b64encode(hashlib.pbkdf2_hmac("sha512", password_alice, salt_alice, iterations, dklen=128))
print(value_alice, salt_alice, iterations)

salt_bob = "".encode()
password_bob = "password".encode()
value_bob = base64.b64encode(hashlib.pbkdf2_hmac("sha512", password_bob, salt_bob, iterations, dklen=128))
print(value_bob, salt_bob, iterations)