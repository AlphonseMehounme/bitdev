"""
  Transaction Builder Module
"""
import hashlib
import base58
from bitcoinlib.wallets import wallet_create_or_open
from bitcoinlib.transactions import Transaction
from bitcoinlib.mnemonic import Mnemonic


def genredeemscritp(preimage):
  """
    Generate redeem script from preimage
  """
  sha256_hash = hashlib.sha256(preimage).digest()
  lock_hex = sha256_hash.hex()
  redeem_script = f"24{lock_hex}aa"
  return redeem_script

def genp2shaddress(redeem_script):
  """
    Generate Testnet Address from redeem script
  """
  redeem_script_hash = hashlib.sha256(bytes.fromhex(redeem_script)).digest()
  redeem_script_hash_hex = hashlib.new('ripemd160', redeem_script_hash).digest().hex()
  address_bytes = bytes.fromhex('05' + redeem_script_hash_hex)
  checksum = hashlib.sha256(hashlib.sha256(address_bytes).digest()).digest()[:4]
  address_with_checksum = address_bytes + checksum
  address = base58.b58encode(address_with_checksum).decode('utf-8')
  return address

def trxconstructor(wallet, address, amount, utxotrxid, utxoindex):
  """
    Construct a transaction
  """
  wallet = wallet_create_or_open(wallet)
  key = wallet.get_key()
  new_address = key.address
  print("New test address :", new_address)
  tx = Transaction()
  tx.add_input(utxotrxid, utxoindex)
  tx.add_output(amount, address)
  
  #tx.sign(key)
  #serialized_tx = tx.serialize()

if __name__ == "__main__":

  # 1 Generate Redeem Script from Preimage
  preimage = b"Btrust Builders"
  redeem_script = genredeemscritp(preimage)
  print("Redeem Script (hex):", redeem_script)

  # 2 Derive Address from Redeem Script
  address = genp2shaddress(redeem_script)
  print("Address:", address)

  # 3 Construct a transaction that send Bitcoin to the address
  utxotrxid = "67d48b4b6b145f1b0ebbe26a167a6cf8245801a518268a5cb01de9d61db8901a"
  utxoindex = 0
  trxconstructor("Btrust", address, 10000, utxotrxid, utxoindex)
