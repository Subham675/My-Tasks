import random
def otp(len=4):
    chars='0123456789'
    otp_val=''.join(random.choice(chars) for i in range(len))
    return otp_val
o=otp()
print("otp : ",o)