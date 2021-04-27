#
# a file to store a bunch of useful tools
#

def raise_to_pow(num, pow):
    result = 1
    for index in range(pow):
        result = result*num
    return result

#num = int(input('enter number... '))
#pow = int(input('enter exponent... '))
#print(raise_to_pow(num, pow))

def str_int(string):
    return int(string)

#string1 = "234"
#print(type(str_int(string1)))
#print(str_int(string1))

