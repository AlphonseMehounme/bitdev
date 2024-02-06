"""
  Transaction Builder Module
"""
import hashlib
import base58


def genredeemscritp(preimage):
  """
    Generate redeem script from preimage
  """
  sha256_hash = hashlib.sha256(preimage).digest()
  lock_hex = sha256_hash.hex()
  redeem_script = f"20{lock_hex}24aa"
  return redeem_script

def genp2shaddress(redeem_script):
  """
    Generate p2sh Address from redeem script
  """
  redeem_script_hash = hashlib.sha256(bytes.fromhex(redeem_script)).digest()
  redeem_script_hash_hex = hashlib.new('ripemd160', redeem_script_hash).digest().hex()
  address_bytes = bytes.fromhex('05' + redeem_script_hash_hex)
  checksum = hashlib.sha256(hashlib.sha256(address_bytes).digest()).digest()[:4]
  address_with_checksum = address_bytes + checksum
  p2sh_address = base58.b58encode(address_with_checksum).decode('utf-8')
  return p2sh_address

if __name__ == "__main__":
  preimage = b"Btrust Builders"

  redeem_script = genredeemscritp(preimage)
  print("Redeem Script (hex):", redeem_script)
  
  p2sh_address = genp2shaddress(redeem_script)
  print("P2SH Address:", p2sh_address)
