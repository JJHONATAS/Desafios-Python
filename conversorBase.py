
from pwn import *

sh = remote('2019shell1.picoctf.com', 20836)

binary_data = sh.recvuntil('Input:\n').split('\n')[2].split(' ')[3:-3]
binary_data = ''.join(map(lambda x: chr(int(x, 2)), binary_data))
sh.sendline(binary_data)

oct_data = sh.recvuntil('Input:\n').split('\n')[0].split('the  ')[-1].split(' as')[0].split(' ')
oct_data = ''.join(map(lambda x: chr(int(x, 8)), oct_data))
sh.sendline(oct_data)

hex_data = sh.recvuntil('Input:\n').split('\n')[0].split('the ')[-1].split(' as')[0]
hex_data = hex_data.decode('hex')
sh.sendline(hex_data)

sh.interactive()
