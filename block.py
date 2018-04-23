from time import time
from hashlib import sha256


class Block:

    def __init__(self, data, prevblockhash=None):

        self.timestamp = str(int(time()))
        self.data = data
        self.prevblockhash = prevblockhash

    def hashblock(self, nonce):

        s = sha256()
        s.update(self.timestamp.encode())

        for tx in self.data:
            s.update(tx)

        # if genesis block
        if self.prevblockhash is None:
            s.update(bytes())
        else:
            s.update(str(self.prevblockhash).encode())

        s.update(str(nonce).encode())
        return s.hexdigest()
