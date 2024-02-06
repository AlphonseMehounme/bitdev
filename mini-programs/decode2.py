"""
  Transaction Decoder Module
"""

trx_h = "020000000001010ccc140e766b5dbc884ea2d780c5e91e4eb77597ae64288a42575228b79e234900000000000000000002bd37060000000000225120245091249f4f29d30820e5f36e1e5d477dc3386144220bd6f35839e94de4b9cae81c00000000000016001416d31d7632aa17b3b316b813c0a3177f5b6150200140838a1f0f1ee607b54abf0a3f55792f6f8d09c3eb7a9fa46cd4976f2137ca2e3f4a901e314e1b827c3332d7e1865ffe1d7ff5f5d7576a9000f354487a09de44cd00000000"
print("Raw Transaction in Hex:", trx_h, end="\n\n")
trx_bytes = bytes.fromhex(trx_h)
i = 4

# Version
version_bytes = trx_bytes[0:i]
version = int(version_bytes[::-1].hex(), 16)
print("Version : {}\n".format(version))
i = 4

# Marker and Flag
if trx_bytes[i] == 00:
    marker_bytes = trx_bytes[i]
    i += 1
    flag_bytes = trx_bytes[i]
    i += 1

# Inputs
print("-----Inputs-----")
num_input = trx_bytes[i]
print("Number of input :", num_input)
for j in range(num_input):
    print("Input_{}".format(j))
    i += 1
    inputjtrxid = trx_bytes[i:i + 32][::-1].hex()
    print("Input Trx ID :", inputjtrxid)
    i += 41
print()

# Outputs
print("-----Outputs-----")
num_output = trx_bytes[i]
print("Number of output :", num_output)
for k in range(num_output):
    print("Output_{}".format(k))
    i += 1
    amountoutputk = int(trx_bytes[i:i+8][::-1].hex(), 16)
    print("Amount Output_{} : {}".format(k, amountoutputk))
    i += 8
    lockscriptsize = trx_bytes[i]
    i += 1
    lockscript = trx_bytes[i:i+lockscriptsize].hex()
    i += lockscriptsize - 1
    print("Output_{} Script : {}".format(k, lockscript))
print()

#Locktime is the last 4 Bytes
print("Locktime", trx_bytes[-4:].hex())