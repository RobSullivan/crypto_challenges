"""
===========================================
Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179

=========================================

From wikipedia: "a string of text can be encrypted by applying 
the bitwise XOR operator to every character using a given key"

How can a string be made a hex string? 

base64.b16decode.('1c0111001f010100061a024b53535009181c') 
raise binascii.Error('Non-base16 digit found')

binascii.hexlify(bytes('1c0111001f010100061a024b53535009181c', 'utf-8'))
outputs b'316330313131303031663031303130303036316130323462353335333530303931383163'

Python3 doesn't support string.encode("hex")

(Full log at end of file)


solution to produce the desired output found on stackoverflow, in the end.

http://stackoverflow.com/a/11119660
hex(int('1c0111001f010100061a024b53535009181c', 16) ^ int('686974207468652062756c6c277320657965', 16))



But what's happening?


By "hex decoding" it must mean take a string and make into a hex string not decode this string to base16.

More discussion here https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch06s09.html

Python supports hex

From the SO answer and from Python3.4 docs 

can use int(x, 16). 

If base is given then x must be a string, bytes or bytearray 

so...
>>hexed_1 = int('1c0111001f010100061a024b53535009181c', 16)
2439506885960970423528311773783961071327260
#hex converts an int to a hexadecimal string prefixed with 0x

hex(2439506885960970423528311773783961071327260)

'0x1c0111001f010100061a024b53535009181c'



A function then needs to check length of buffers are equal-length
"""




def xor_combo(a, b):

	if len(a) is len(b):
		hex_a = int(a, 16)
		hex_b = int(b, 16)

		xord = hex_a ^ hex_b
		hex_string = hex(xord)
		return hex_string.lstrip('0x')
	else:
		return print('strings are unequal length')












"""

Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import base64
>>> base64.b16decode(b'1c0111001f010100061a024b53535009181c')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    base64.b16decode(b'1c0111001f010100061a024b53535009181c')
  File "C:\Python34\lib\base64.py", line 282, in b16decode
    raise binascii.Error('Non-base16 digit found')
binascii.Error: Non-base16 digit found
>>>  base64.b16decode('1c0111001f010100061a024b53535009181c')
 
SyntaxError: unexpected indent
>>> base64.b16decode('1c0111001f010100061a024b53535009181c')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    base64.b16decode('1c0111001f010100061a024b53535009181c')
  File "C:\Python34\lib\base64.py", line 282, in b16decode
    raise binascii.Error('Non-base16 digit found')
binascii.Error: Non-base16 digit found
>>> base64.standard_b64decode(b'1c0111001f010100061a024b53535009181c')
b'\xd5\xcd5\xd7]4\xd5\xfd5\xd3]4\xd3\xadZ\xd3n\x1b\xe7~w\xe7M=\xd7\xcd\\'
>>> print(12^42)
38
>>> print(9 | 4)
13
>>> 9 |4
13
>>> 5 >> 4
0
>>> 5 << 1
10
>>> bytes('1c0111001f010100061a024b53535009181c', 'utf-8')
b'1c0111001f010100061a024b53535009181c'
>>> base64.decode
<function decode at 0x02E59108>
>>> base64.decode(bytes('1c0111001f010100061a024b53535009181c', 'utf-8'))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    base64.decode(bytes('1c0111001f010100061a024b53535009181c', 'utf-8'))
TypeError: decode() missing 1 required positional argument: 'output'
>>> base64.b16decode(bytes('1c0111001f010100061a024b53535009181c', 'utf-8'))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    base64.b16decode(bytes('1c0111001f010100061a024b53535009181c', 'utf-8'))
  File "C:\Python34\lib\base64.py", line 282, in b16decode
    raise binascii.Error('Non-base16 digit found')
binascii.Error: Non-base16 digit found
>>> import binascii
>>> bytes('686974207468652062756c6c277320657965', 'utf-8')
b'686974207468652062756c6c277320657965'
>>> bytes('1c0111001f010100061a024b53535009181c', 'utf-8') ^ bytes('686974207468652062756c6c277320657965', 'utf-8')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    bytes('1c0111001f010100061a024b53535009181c', 'utf-8') ^ bytes('686974207468652062756c6c277320657965', 'utf-8')
TypeError: unsupported operand type(s) for ^: 'bytes' and 'bytes'
>>> binascii.hexlify(bytes('1c0111001f010100061a024b53535009181c', 'utf-8'))
b'316330313131303031663031303130303036316130323462353335333530303931383163'
>>> binascii.unhexlify(b'316330313131303031663031303130303036316130323462353335333530303931383163')
b'1c0111001f010100061a024b53535009181c'
>>> hexlified = binascii.hexlify(bytes('1c0111001f010100061a024b53535009181c', 'utf-8'))
>>> hexlified ^ '686974207468652062756c6c277320657965'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    hexlified ^ '686974207468652062756c6c277320657965'
TypeError: unsupported operand type(s) for ^: 'bytes' and 'str'
>>> base64.b64decode('1c0111001f010100061a024b53535009181c')
b'\xd5\xcd5\xd7]4\xd5\xfd5\xd3]4\xd3\xadZ\xd3n\x1b\xe7~w\xe7M=\xd7\xcd\\'
>>> hexed1 = base64.b64decode('1c0111001f010100061a024b53535009181c')
>>> hexed2 = base64.b64decode('686974207468652062756c6c277320657965')
>>> hexed1 ^ hexed2
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    hexed1 ^ hexed2
TypeError: unsupported operand type(s) for ^: 'bytes' and 'bytes'
>>> hexed1 = base64.b64decode(b'1c0111001f010100061a024b53535009181c')
>>> hexed2 = base64.b64decode(b'686974207468652062756c6c277320657965')
>>> type(hexed1)
<class 'bytes'>
>>> hexed1 ^ hexed 2
SyntaxError: invalid syntax
>>> hexed1 ^ hexed2
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    hexed1 ^ hexed2
TypeError: unsupported operand type(s) for ^: 'bytes' and 'bytes'
>>> print(hex(hexed1 ^ hexed2))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(hex(hexed1 ^ hexed2))
TypeError: unsupported operand type(s) for ^: 'bytes' and 'bytes'
>>> base64.b16
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    base64.b16
AttributeError: 'module' object has no attribute 'b16'
>>> base64.b16decode(b'1c0111001f010100061a024b53535009181c')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    base64.b16decode(b'1c0111001f010100061a024b53535009181c')
  File "C:\Python34\lib\base64.py", line 282, in b16decode
    raise binascii.Error('Non-base16 digit found')
binascii.Error: Non-base16 digit found
>>> '1c0111001f010100061a024b53535009181c'.decode('hex')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    '1c0111001f010100061a024b53535009181c'.decode('hex')
AttributeError: 'str' object has no attribute 'decode'
>>> binascii.hexlify('1c0111001f010100061a024b53535009181c', 'utf-8'))
SyntaxError: invalid syntax
>>> binascii.hexlify('1c0111001f010100061a024b53535009181c', 'utf-8')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    binascii.hexlify('1c0111001f010100061a024b53535009181c', 'utf-8')
TypeError: b2a_hex() takes exactly 1 argument (2 given)
>>> binascii.hexlify('1c0111001f010100061a024b53535009181c')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    binascii.hexlify('1c0111001f010100061a024b53535009181c')
TypeError: 'str' does not support the buffer interface
>>> binascii.hexlify(b'1c0111001f010100061a024b53535009181c', 'utf-8')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    binascii.hexlify(b'1c0111001f010100061a024b53535009181c', 'utf-8')
TypeError: b2a_hex() takes exactly 1 argument (2 given)
>>> binascii.hexlify(b'1c0111001f010100061a024b53535009181c')
b'316330313131303031663031303130303036316130323462353335333530303931383163'
>>> binascii.hexlify(b'686974207468652062756c6c277320657965')
b'363836393734323037343638363532303632373536633663323737333230363537393635'
>>> binascii.hexlify(b'1c0111001f010100061a024b53535009181c') ^ binascii.hexlify(b'686974207468652062756c6c277320657965')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    binascii.hexlify(b'1c0111001f010100061a024b53535009181c') ^ binascii.hexlify(b'686974207468652062756c6c277320657965')
TypeError: unsupported operand type(s) for ^: 'bytes' and 'bytes'
>>> int(binascii.hexlify(b'686974207468652062756c6c277320657965'))
363836393734323037343638363532303632373536633663323737333230363537393635
>>> hexed_int1 = int(binascii.hexlify(b'686974207468652062756c6c277320657965'))
>>> hexed_int2 = int(binascii.hexlify(b'686974207468652062756c6c277320657965'))
>>> hexed_int1 ^ hexed_int2
0
>>> hexed_int1 ^ 686974207468652062756c6c277320657965
SyntaxError: invalid syntax
>>> int1 = 686974207468652062756c6c277320657965
SyntaxError: invalid syntax
>>> base64.b16decode(b'1c0111001f010100061a024b53535009181c')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    base64.b16decode(b'1c0111001f010100061a024b53535009181c')
  File "C:\Python34\lib\base64.py", line 282, in b16decode
    raise binascii.Error('Non-base16 digit found')
binascii.Error: Non-base16 digit found
>>> import binhex
>>> binascii.rledecode_hqx('1c0111001f010100061a024b53535009181c')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    binascii.rledecode_hqx('1c0111001f010100061a024b53535009181c')
TypeError: 'str' does not support the buffer interface
>>> binascii.rledecode_hqx(b'1c0111001f010100061a024b53535009181c')
b'1c0111001f010100061a024b53535009181c'
>>> b'\xd5\xcd5\xd7]4\xd5\xfd5\xd3]4\xd3\xadZ\xd3n\x1b\xe7~w\xe7M=\xd7\xcd\\' ^ b'\xd5\xcd5\xd7]4\xd5\xfd5\xd3]4\xd3\xadZ\xd3n\x1b\xe7~w\xe7M=\xd7\xcd\\'
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    b'\xd5\xcd5\xd7]4\xd5\xfd5\xd3]4\xd3\xadZ\xd3n\x1b\xe7~w\xe7M=\xd7\xcd\\' ^ b'\xd5\xcd5\xd7]4\xd5\xfd5\xd3]4\xd3\xadZ\xd3n\x1b\xe7~w\xe7M=\xd7\xcd\\'
TypeError: unsupported operand type(s) for ^: 'bytes' and 'bytes'
>>> hex(b'\xd5\xcd5\xd7]4\xd5\xfd5\xd3]4\xd3\xadZ\xd3n\x1b\xe7~w\xe7M=\xd7\xcd\\' ^ b'\xd5\xcd5\xd7]4\xd5\xfd5\xd3]4\xd3\xadZ\xd3n\x1b\xe7~w\xe7M=\xd7\xcd\\')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    hex(b'\xd5\xcd5\xd7]4\xd5\xfd5\xd3]4\xd3\xadZ\xd3n\x1b\xe7~w\xe7M=\xd7\xcd\\' ^ b'\xd5\xcd5\xd7]4\xd5\xfd5\xd3]4\xd3\xadZ\xd3n\x1b\xe7~w\xe7M=\xd7\xcd\\')
TypeError: unsupported operand type(s) for ^: 'bytes' and 'bytes'
>>> \xd5\xcd5\xd7]4\xd5\xfd5\xd3]4\xd3\xadZ\xd3n\x1b\xe7~w\xe7M=\xd7\xcd\\
SyntaxError: unexpected character after line continuation character
>>> int('1c0111001f010100061a024b53535009181c', '16')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    int('1c0111001f010100061a024b53535009181c', '16')
TypeError: 'str' object cannot be interpreted as an integer
>>> hex(int("12ef", 16) ^ int("abcd", 16))
'0xb922'
>>> int('1c0111001f010100061a024b53535009181c', 16)
2439506885960970423528311773783961071327260
>>> hex(int('1c0111001f010100061a024b53535009181c', 16))
'0x1c0111001f010100061a024b53535009181c'
>>> hex(int('686974207468652062756c6c277320657965', 16))
'0x686974207468652062756c6c277320657965'
>>> hex(int('1c0111001f010100061a024b53535009181c', 16)) ^ hex(int('686974207468652062756c6c277320657965', 16))
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    hex(int('1c0111001f010100061a024b53535009181c', 16)) ^ hex(int('686974207468652062756c6c277320657965', 16))
TypeError: unsupported operand type(s) for ^: 'str' and 'str'
>>> hex(int('1c0111001f010100061a024b53535009181c', 16) ^ int('686974207468652062756c6c277320657965', 16))
'0x746865206b696420646f6e277420706c6179'
>>> base64.b16encode('1c0111001f010100061a024b53535009181c')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    base64.b16encode('1c0111001f010100061a024b53535009181c')
  File "C:\Python34\lib\base64.py", line 264, in b16encode
    return binascii.hexlify(s).upper()
TypeError: 'str' does not support the buffer interface
>>> base64.b16encode(b'1c0111001f010100061a024b53535009181c')
b'316330313131303031663031303130303036316130323462353335333530303931383163'
>>> hex(base64.b16encode(b'1c0111001f010100061a024b53535009181c'))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    hex(base64.b16encode(b'1c0111001f010100061a024b53535009181c'))
TypeError: 'bytes' object cannot be interpreted as an integer
>>> hex('0x746865206b696420646f6e277420706c6179')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    hex('0x746865206b696420646f6e277420706c6179')
TypeError: 'str' object cannot be interpreted as an integer
>>> int("12ef", 16)
4847
>>> hexed_1 = int('1c0111001f010100061a024b53535009181c', 16)
>>> hexed_2 = int('686974207468652062756c6c277320657965', 16)
>>> hexed_1
2439506885960970423528311773783961071327260
>>> hex(hexed_1)
'0x1c0111001f010100061a024b53535009181c'
>>> hex(2439506885960970423528311773783961071327260)
'0x1c0111001f010100061a024b53535009181c'
>>> '0x1c0111001f010100061a024b53535009181c' ^ '0x686974207468652062756c6c277320657965'
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    '0x1c0111001f010100061a024b53535009181c' ^ '0x686974207468652062756c6c277320657965'
TypeError: unsupported operand type(s) for ^: 'str' and 'str'
>>> type(hex(2439506885960970423528311773783961071327260))
<class 'str'>
>>> hexed_1 ^ hexed_2
10140548954603607733141837726260044841640313
>>> hex(hexed_1 ^ hexed_2)
'0x746865206b696420646f6e277420706c6179'
>>> '1c0111001f010100061a024b53535009181c'.encode('hex')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    '1c0111001f010100061a024b53535009181c'.encode('hex')
LookupError: 'hex' is not a text encoding; use codecs.encode() to handle arbitrary codecs
>>> "hello".encode("hex")
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    "hello".encode("hex")
LookupError: 'hex' is not a text encoding; use codecs.encode() to handle arbitrary codecs
>>> 

"""