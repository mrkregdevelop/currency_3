'''
A

Taras
['T', 'a', 'r', 'a', 's']
[84, 97, 114, 97, 115] + 1
[85, 98, 115, 98, 116]
['U', 'b', 's', 'b', 't']
Ubsbt

B

A ----> B
'''

key = 2


def encode(message: str):
    encoded = ''

    for char in message:
        encoded += chr(ord(char) + key)

    return encoded


def decode(encrypted: str):
    message = ''

    for char in encrypted:
        message += chr(ord(char) - key)

    return message

breakpoint()
