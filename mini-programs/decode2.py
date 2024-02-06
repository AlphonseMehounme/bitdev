"""
  Transaction Decoder Module
"""

trx_h = input("Raw Transaction in Hex: ")
trx_bytes = bytes.fromhex(trx_h)
i = 0

version_bytes = trx_bytes[0:4]
version = int(version_bytes[::-1].hex(), 16)
print("Version : {}\n".format(version))
i = 4

if trx_bytes[4] == 00:
    marker_bytes = 00
    flag_bytes = trx_bytes[5]
    i = 6

print("Inputs :")
num_input = trx_bytes[i]
print("Number of input", num_input)
for j in range(num_input):
    print("Input_{}".format(j))
    i += 1
    inputjtrxid = trx_bytes[i:i + 32][::-1].hex()
    print("Input TRX ID :", inputjtrxid)

print()

print("Outputs...\n")

print("Locktime", trx_bytes[189:193].hex())