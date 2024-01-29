"""
    Simple Bitcoin Wallet

"""

# Imports
from bitcoinlib.wallets import *

# Get wallet name from user
walletName = input("Wallet Name : ")

# Get witness type from user
print("Choose witness type : \n")
types = ['P2PK', 'P2PKH', 'P2SH', 'P2WPKH', 'P2WSH', 'P2TR']
for i in range(len(types)):
    print(str(i + 1) + ' : ' + types[i])
wtype = int(input("\n> "))
if wtype - 1 not in range(len(types)):
    print("error")
    exit(1)

# Create wallet
try:
    wallet = wallet_create_or_open(walletName, network='testnet')
    print("\n(Wallet {} successfully created or imported.)\n".format(walletName))
except:
    print("\nWallet {} exits\n".format(walletName))
    exit(1)

# Print Address
key = wallet.get_key()
testnet_address = key.address
print("Testnet Address: ", str(testnet_address))

# Reload wallet and print balance
wallet.utxos_update()
print("\nYour balance is {} sats.".format(wallet.balance()))

# Try sending some some
ctn = int(input("Try getting some sat to the address from a tesnet faucet and click 1 to try sending or 0 to exit : \n > "))
if ctn == 1:
    wallet.utxos_update()
    if wallet.balance() < 500:
        print("Balance {} too low".format(wallet.balance()))
        exit(1)
    trx = wallet.send_to("mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB", 1000, 300, offline=False)
    trx.info()
else:
    print("Exit...")
    exit(1)
