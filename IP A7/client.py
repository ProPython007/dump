import socket


port = 6969
portClient = 8989
host = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((host, portClient))
client.connect((host, port))
key = '1001'


def xor(a, b):
    # initialize result
    result = []
 
    # Traverse all bits, if bits are
    # same, then XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
 
    return ''.join(result)


# Performs Modulo-2 division
def mod2div(dividend, divisor):
    # Number of bits to be XORed at a time.
    pick = len(divisor)
 
    # Slicing the dividend to appropriate
    # length for particular step
    tmp = dividend[0 : pick]
 
    while pick < len(dividend):
 
        if tmp[0] == '1':
 
            # replace the dividend by the result
            # of XOR and pull 1 bit down
            tmp = xor(divisor, tmp) + dividend[pick]
 
        else: # If leftmost bit is '0'
 
            # If the leftmost bit of the dividend (or the
            # part used in each step) is 0, the step cannot
            # use the regular divisor; we need to use an
            # all-0s divisor.
            tmp = xor('0'*pick, tmp) + dividend[pick]
 
        # increment pick to move further
        pick += 1
 
    # For the last n bits, we have to carry it out
    # normally as increased value of pick will cause
    # Index Out of Bounds.
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
 
    checkword = tmp
    return checkword


# Function used at the sender side to encode
# data by appending remainder of modular division
# at the end of data.
def encodeData(data, key):
 
    l_key = len(key)
 
    # Appends n-1 zeroes at end of data
    appended_data = data + '0'*(l_key-1)
    print("Appended data:", appended_data)
    remainder = mod2div(appended_data, key)
    print("CRC:", remainder)

    # Append remainder in the original data
    codeword = data + remainder

    return codeword


while True:
    data = input("\nEnter your message: ")
    
    bdata = (''.join(format(ord(x), 'b') for x in data))
    print("Entered data in binary format:", bdata)
    print('Key to be used:', key)
    
    sdata = encodeData(bdata, key)
    print("Encoded data to be sent to server in binary format:", sdata)

    client.send(sdata.encode())

    # receive data from the server
    print("Received feedback from server:", client.recv(1024).decode())