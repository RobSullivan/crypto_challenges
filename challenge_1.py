"""
Convert hex to base64
The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

"""

import base64

#first decode hex string

decoded_b16 = base64.b16decode(b'49276D206B696C6C696E6720796F757220627261696E206C696B65206120706F69736F6E6F7573206D757368726F6F6D')

#result is b"I'm killing your brain like a poisonous mushroom"
#then encode as base64

encoded_base64 = base64.b64encode(decoded_b16)




