from blockchain import Blockchain
from network import Network
from client import Client
from random import choice

# create blockchain with genesis block
b = Blockchain()

# create a network of miners
n = Network()

# add some miners to the network
nodes = 5
clients = []

for i in range(1, nodes+1):
    c = Client("Client #{}".format(i), b)
    clients.append(c)
    n.add_client(c)

# broadcast a series of transactions
num = 7
for i in range(1, num+1):

    t = "this is transaction #{}".format(i)
    sender = choice(clients)
    transaction = sender.create_transaction(t)
    block = n.broadcast_transaction(transaction, b.getLastBlock())

    b.addBlock(block)
    sender.blockchain.addBlock(block)

# print summary of clients
print('\n -------- Node Summary -------')
for c in n.get_clients():
    print("\n {} reward: {} \n power: {}".format(c.name, c.reward, c.power))
