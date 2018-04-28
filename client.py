from block import Block
from random import randint, choice
from pow import pow
import rsa


class Client:

    def __init__(self, name, blockchain):

        self.name = name
        self.reward = 0
        self.power = randint(1, 30)  # mimics variations in hashing power
        self.blockchain = blockchain
        self.txbuffer = []
        self.cache = []
        self.blocksize = 1  # max number of txs in a block

        (pubkey, privkey) = rsa.newkeys(512)
        self.pubkey = pubkey
        self.privkey = privkey

    # create a transaction and sign it with the private key
    def create_transaction(self, data):
        data = data.encode('utf8')
        return rsa.sign(data, self.privkey, 'SHA-1')

    def receivetransaction(self, txdata, lastblock, q, mined):

        self.txbuffer.append(txdata)

        # create a block if 5 transactions are received
        if len(self.txbuffer) >= self.blocksize:
            self.mine(txdata, lastblock, q, mined)

    def receiveblock(self, block):

        # if the block can be added now
        if block.prevblockhash == self.blockchain.blocks[-1].hash:

            # no blocks in cache, add right to chain right away
            if len(self.cache) == 0:
                self.blockchain.blocks.append(block)

            else:  # choose a random block from the cache
                self.cache.append(block)
                chosen = choice(self.cache)
                self.cache.remove(chosen)
                self.blockchain.blocks.append(chosen)

        else:  # invalid last block hash, check cache and swap if necessary
            for b in self.cache:
                if block.prevblockhash == b.hash:
                    self.blockchain.blocks[-1] = b
                    self.blockchain.blocks.append(block)
                    break

    def mine(self, data, lastblock, queue, mined):

        newblock = Block(self.txbuffer[-self.blocksize:], lastblock)
        newblock.nonce, newblock.hash = pow(newblock, self.power)

        # check if another miner/thread has already mined this block
        if not mined.is_set():
            newblock.miner = self.name
            self.reward += 5
            self.txbuffer = []
            self.blockchain.addBlock(newblock)
            queue.put(newblock)

        # set mined event and stop all other threads
        mined.set()


'''
 If a user receives two blocks B1 and B1' both building on the last block he has which we will call it B0, he will choose one at random, 
 let's assume it to be B1 and append it to his chain, however he must save B1' in his cache. 
 If the user receives block B2' that builds on B1', he will swap B1' with B1 and append B2' to his newly changed chain. 
 He will then return B1 to the cache and wait if he receives any block building on it. By this he is choosing the longest chain.
'''
