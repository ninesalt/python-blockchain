from block import Block
from random import randint
from pow import pow
import rsa


class Client:

    def __init__(self, name, blockchain):
        self.name = name
        self.reward = 0
        self.power = randint(1, 30)  # mimics variations in hashing power
        self.blockchain = blockchain

        (pubkey, privkey) = rsa.newkeys(512)
        self.pubkey = pubkey
        self.privkey = privkey

    # create a transaction and sign it with the private key
    def create_transaction(self, data):
        data = data.encode('utf8')
        return rsa.sign(data, self.privkey, 'SHA-1')

    def mine(self, data, lastblock, queue, mined):

        newblock = Block(data, lastblock)
        newblock.nonce, newblock.hash = pow(newblock, self.power)

        # check if another miner/thread has already mined this block
        if not mined.is_set():
            newblock.miner = self.name
            self.reward += 5
            self.blockchain.addBlock(newblock)
            queue.put(newblock)

        # set mined event and stop all other threads
        mined.set()
