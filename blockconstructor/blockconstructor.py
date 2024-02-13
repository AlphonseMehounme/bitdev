"""
  Block Constructor Module
"""
import os

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
            parts = line.strip().strip('"').split(',')
            txid = parts[0]
            fee = parts[1]
            weight = parts[2]
            parents = parts[3:]
            transactions.append(MempoolTransaction(txid, fee, weight, parents))
    return transactions


if __name__ == "__main__":
    
    i = 0
    trxinblock = []
    weights = 0
    fees = 0

    transactions = parse_mempool_csv()
    
    while (i < len(transactions)) and ((weights + transactions[i].weight) <= 4000000):
        parentnotincluded = False
        if transactions[i].parents != ['']:
            for id in transactions[i].parents:
                if id not in trxinblock:
                    parentnotincluded = True
                    break
        if not parentnotincluded:
            with open('otherfile.txt', 'a') as otherfile:
                otherfile.write(transactions[i].txid)
                otherfile.write('\n')
            trxinblock.append(transactions[i].txid)
        weights += transactions[i].weight
        fees += transactions[i].fee
        i += 1
    
    with open('otherfile.txt', 'r') as otherfile:
        content = otherfile.read()

    with open('block.txt', 'w') as block:
      block.write(content)

    os.remove('otherfile.txt')
    
    print("Block Successfully Constructed\n")
    print(" - Number of transactions included :", len(trxinblock))
    print(" - Block Weight :", weights)
    print(" - Fees :", fees)