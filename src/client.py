from block import Block
from random import randint
from pow import pow


class Client:

    def __init__(self, name):
        self.name = name
        self.reward = 0
        self.power = randint(1, 30)  # mimics variations in hashing power

    def mine(self, data, lastblock, queue, mined):

        newblock = Block(data, lastblock)
        newblock.nonce, newblock.hash = pow(newblock, self.power)

        # check if another miner/thread has already mined this block
        if not mined.is_set():
            newblock.miner = self.name
            self.reward += 5
            queue.put(newblock)

        # set mined event and stop all other threads
        mined.set()
