from block import *


class Blockchain():

    def __init__(self):
        genesisblock = createGenesisBlock()
        self.blocks = [genesisblock]

    def getLastBlock(self):
        return self.blocks[-1]

    def addBlock(self, data):
        newblock = Block(data, self.getLastBlock())
        self.blocks.append(newblock)
