from blockchain import Blockchain
from network import Network
from client import Client

# create blockchain with genesis block
b = Blockchain()

# create a network of miners
n = Network()

c1 = Client("client 1")
c2 = Client("client 2")
c3 = Client("client 3")

# add clients to the network
n.add_client(c1)
n.add_client(c2)
n.add_client(c3)

# broadcast a series of transactions
num = 5
for i in range(1, num+1):
    t = "this is transaction #{}".format(i)
    b.addBlock(n.broadcast_transaction(t, b.getLastBlock()))

# print summary of clients
print('\n ---- Node Summary ----')
for c in n.get_clients():
    print("\n {} reward: {} \n power: {}".format(c.name, c.reward, c.power))
