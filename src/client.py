from block import Block
from random import randint
from pow import pow


class Client:

    def __init__(self, name):
        self.name = name
        self.reward = 0
        self.power = randint(1, 30)  # mimics variations in hashing power

    def get_reward(self):
        return self.reward

    def mine(self, data, lastblock, queue, mined):

        newblock = Block(data, lastblock)
        newblock.nonce, newblock.hash = pow(newblock, self.power, mined)
        mined = True
        newblock.miner = self.name
        self.reward += 5

        queue.put(newblock)
