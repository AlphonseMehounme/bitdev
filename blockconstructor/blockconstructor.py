"""
  Block Constructor Module
"""

class MempoolTransaction:
    """
      Class MempoolTransaction
    """

    def __init__(self, txid, fee, weight, parents):
        """
          Instanciate a MempoolTransaction Object
        """
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parents = parents

def parse_mempool_csv():
    """
      parse_mempool_csv function parse the CSV file 
      and return a list of MempoolTransactions.
    """
    transactions = []
    with open('mempool.csv') as f:
        for line in f.readlines():
            parts = line.strip().split(',')
            txid = parts[0]
            fee = parts[1]
            weight = parts[2]
            parents = parts[3:]
            transactions.append(MempoolTransaction(txid, fee, weight, parents))
    return transactions

transactions = parse_mempool_csv()
weights = 0
i = 0
trxinblock = []


while (i < len(transactions)) and ((weights + transactions[i].weight) <= 4000000):
    parentnotincluded = False
    if transactions[i].parents != None:
        for id in transactions[i].parents:
            if id not in trxinblock:
                parentnotincluded = True
                break
    if parentnotincluded:
        with open('block.txt', 'a') as blockfile:
            blockfile.write(transactions[i].txid)
            blockfile.write('\n')
        trxinblock.append(transactions[i].txid)
        weights += transactions[i].weight
    i += 1

for trx in trxinblock:
    print(trx)
