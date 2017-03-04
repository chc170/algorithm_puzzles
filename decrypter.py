"""
Decrpyt Google Foo.bar encrypted message

1. Decode the message by base64 decoder.
2. Use google account as the key to run XOR character by character against
   the decoded message.

Reference: @Jaconotar
"""

import base64

TEXT = '''
H04dFgwAChcaSUNVQ0gDGwsCG0RDRE4NDAMPCgUOGwZIQ1VETgsQGwYKCQwKRENDSAEPCAwdFxxD
SVRDSAoBBxsLBwYBAwFOQkNIAgwMAAsVCg4KCh1JQ1VDSBEHAgwMCAoATkJDSBEOBgsHFxxET15J
SRAOBQpDRU5ECQwAQ0lUQ0gUBgpISR4=
'''

KEY = 'dincoco'

result = []
for i, c in enumerate(base64.b64decode(TEXT)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))