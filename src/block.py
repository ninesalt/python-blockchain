from time import time
from hashlib import sha256


class Block:

    def __init__(self, data, previousblock):

        timestamp = str(int(time()))

        s = sha256()
        s.update(timestamp.encode())
        s.update(data.encode())

        if previousblock is None:
            s.update(bytes())
            self.previousblockhash = None
        else:
            s.update(previousblock.hash.encode())
            self.previousblockhash = previousblock.hash

        self.timestamp = timestamp
        self.data = data
        self.hash = s.hexdigest()


def createGenesisBlock():
    return Block("block 0", None)
