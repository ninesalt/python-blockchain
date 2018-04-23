from random import sample, randint, choice
from threading import Thread, Event
from queue import Queue


class Network:

    def __init__(self):
        self.clients = []
        self.graph = {}

    def add_client(self, client):

        if len(self.clients) > 0:

            connections = sample(self.clients, randint(1, len(self.clients)))

            for c in connections:
                self.graph[c].append(client)

            self.graph[client] = connections

        else:
            self.graph[client] = []

        self.clients.append(client)

    # get all peers indrectly connected (this well get all clients?)

    def get_connections(self, client):

        connections = self.graph[client]

        for c in self.clients:
            if c not in connections:
                connections.append(c)

        return connections

    def broadcast_block(self, block):
        for client in self.clients:
            client.receieveblock(block)

    def print_network(self):

        print('\nNetwork connections \n')

        for key, values in self.graph.items():
            connections = [c.name for c in values]
            connections = ', '.join(connections)
            print(key.name, ' is connected to', connections)

    def get_clients(self):
        return self.clients

    # choose random miners to broadcast the transaction to
    def broadcast_transaction(self, txdata, lastblock):

        # chosen = sample(self.clients, randint(1, len(self.clients)))
        chosen = self.get_connections(choice(self.clients))
        q = Queue()

        # to simulate concurrent mining, each client will get their own thread
        # and when one of them finds a correct nonce, the others will stop
        mined = Event()

        for client in chosen:
            Thread(target=client.receivetransaction, args=(
                txdata, lastblock, q, mined)).start()

        newblock = q.get()
        # self.broadcast_block(newblock)
        return newblock
