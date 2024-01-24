from bitcoinlib.wallets import Wallet

# Define the name for your wallet
wallet_name = 'my_bitcoin_wallet'

# Create a new wallet
wallet = Wallet.create(wallet_name)

# Print the wallet information
print(f"Wallet Name: {wallet_name}")
print(f"Address: {wallet.get_key().address}")
print(f"Private Key: {wallet.get_key().wif()}")

