import block
from time import sleep


def pow(block, power):

    nonce = 0
    difficulty = 5
    sleep(1/power)
    proof = block.hashblock(nonce)

    while proof[: difficulty] != "0" * difficulty:
        nonce += 1
        proof = block.hashblock(nonce)

    return nonce, proof
