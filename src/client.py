from blockchain import Blockchain

# create blockchain with genesis block
b = Blockchain()

for i in range(1, 5):
    nextnum = "block " + str(i)
    b.addBlock(nextnum)
