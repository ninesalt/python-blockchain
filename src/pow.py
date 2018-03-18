from hashlib import sha256
from block import *
from time import sleep


def pow(block, power, mined):

    nonce = 0
    difficulty = 2
    sleep(1/power)
    proof = block.hashblock(nonce)

    while not mined and proof[: difficulty] != "0" * difficulty:
        nonce += 1
        proof = block.hashblock(nonce)

    return nonce, proof
