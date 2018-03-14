from block import *
from pow import pow


class Blockchain():

    def __init__(self):
        genesisblock = createGenesisBlock()
        self.blocks = [genesisblock]

    def getLastBlock(self):
        return self.blocks[-1]

    def addBlock(self, data):

        newblock = Block(data, self.getLastBlock())
        newblock.nonce, newblock.hash = pow(newblock)
        self.blocks.append(newblock)

        print("\n Added block #{} \n Nonce: {} \n Hash {}".format(
            len(self.blocks), newblock.nonce, newblock.hash))
