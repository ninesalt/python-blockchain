from time import time
from block import *
from pow import pow


class Blockchain():

    def __init__(self):
        genesisblock = createGenesisBlock()
        self.blocks = [genesisblock]

    def getLastBlock(self):
        return self.blocks[-1]

    def addBlock(self, block):
        self.blocks.append(block)

        print("\n Added block #{} \n Nonce: {} \n Hash {} \n Mined by: {} \n Timestamp: {}".format(
            len(self.blocks), block.nonce, block.hash, block.miner, block.timestamp))
