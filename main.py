from blockchain import Blockchain
from network import Network
from client import Client
from random import choice
from copy import deepcopy

# create blockchain with genesis block
b = Blockchain()

# create a network of miners
n = Network()

# add some miners to the network
nodes = 5
clients = []

for i in range(1, nodes+1):
    c = Client("Client #{}".format(i), deepcopy(b))
    clients.append(c)
    n.add_client(c)

n.print_network()

# broadcast a series of transactions
num = 10
for i in range(1, num+1):

    t = "this is transaction #{}".format(i)
    sender = choice(clients)
    transaction = sender.create_transaction(t)
    block = n.broadcast_transaction(
        transaction, sender.blockchain.getLastBlock())

    # b.addBlock(block)

# print summary of clients
print('\n -------- Node Summary -------')
for c in n.get_clients():
    print("\n {} \n Reward: {} \n Mined: {} blocks \n Power: {}".format(
        c.name, c.reward, int(c.reward/5), c.power))
