def decoder():
    trx_h = "010000000104dde43b0e4724f1e3b45782a9bfbcc91ea764c7cb1c245fba1fefa175c3a5d0010000006a4730440220519f7867349790ee441e83e545afbd25b954a34e0733cd4da3b5f1e5588625050220166730d053c3672973bcb2bb1a977b747837023b647e3af2ac9c15728b0681da01210236ccb7ee3a9f154127f384a05870c4fd86a8727eab7316f1449a0b9e65bfd90dffffffff025d360100000000001976a91478364a559841329304188cd791ad9dabbb2a3fdb88ac605b0300000000001976a914064e0aa817486573f4c2de09f927697e1e6f233f88ac00000000"
    print("Raw Transaction in Hex:", trx_h, end="\n\n")
    trx_bytes = bytes.fromhex(trx_h)
    i = 4

    # Version
    version_bytes = trx_bytes[0:i]
    version = int(version_bytes[::-1].hex(), 16)
    print("Version : {}\n".format(version))
    i = 4

    # Inputs
    print("-----Inputs-----")
    num_input = trx_bytes[i]
    print("Number of input :", num_input)
    for j in range(num_input):
        print("Input_{}".format(j))
        i += 1
        inputjtrxid = trx_bytes[i:i + 32][::-1].hex()
        print("Input_{} Trx ID : {}".format(j, inputjtrxid))
        i += 32
        inputjindex = int(trx_bytes[i:i + 4][::-1].hex(), 16)
        print("Input_{} index : {}".format(j, inputjindex))
        i += 4
        unlockscriptsize = trx_bytes[i]
        print("Input_{} unlock Script Size : {}".format(j, unlockscriptsize))
        i += 1
        unlockscript = trx_bytes[i:i+unlockscriptsize].hex()
        print("Input_{} unlock Script : {}".format(j, unlockscript))
        i += unlockscriptsize
        sequencenumber = trx_bytes[i:i + 4][::-1].hex()
        print("Input_{} Sequence number : {}".format(j, sequencenumber))
        i += 4
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
        print("Output_{} Script : {}".format(k, lockscript))
        i += lockscriptsize - 1
    print()
    i += 1

    #Locktime is the last 4 Bytes
    print("Locktime :", trx_bytes[i:].hex())

if __name__ == "__main__":
    decoder()
