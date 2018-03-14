from hashlib import sha256
from block import *


def pow(block):

    nonce = 0
    proof = block.hashblock(nonce)

    while proof[:5] != "00000":
        nonce += 1
        proof = block.hashblock(nonce)

    return nonce, proof
