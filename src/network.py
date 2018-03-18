from random import sample, randint
from threading import Thread
from queue import Queue


class Network:

    def __init__(self):
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)

    def get_clients(self):
        return self.clients

    # choose random miners to broadcast the transaction to
    def broadcast_transaction(self, txdata, lastblock):

        # chosen = sample(self.clients, randint(1, len(self.clients)))
        chosen = self.clients
        q = Queue()

        # to simulate concurrent mining, each client will get their own thread
        # and when one of them finds a correct nonce, the others will stop

        for client in chosen:
            Thread(target=client.mine, args=(txdata, lastblock, q)).start()

        return q.get()
