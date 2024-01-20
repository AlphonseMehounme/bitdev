#!/usr/bin/env python3
"""
    Payment request Module
    
   Simple payment request scripts
"""


import segno

def payrequest(addr, amount, label, message):
    return "bitcoin:" + addr + "?amount=" + str(amount) + "&label=" + label + "&message=" + message


if __name__ == "__main__":

    addr = input("Addresse: ")
    amount = int(input("Amount: "))
    label = input("Label: ")
    message = input("Message: ")

    payreq = payrequest(addr, amount, label, message)
    print("Payment request : ", payreq)

    qr_code = segno.make_qr(payreq)
    qr_code.save("pay.png")
    print(qr_code.terminal())
    #qr_code.show()    
