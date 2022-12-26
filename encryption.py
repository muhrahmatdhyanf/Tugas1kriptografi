

# # # var = input("Masukan plainteks = ")
# # # key = input("Masukan key berupa huruf = ")
# # # binary = " ".join(map(bin,bytearray(var)))
# # # binaryes = " ".join(format(ord(x), "b")for x in key)

# # # # ts = binary ^ binaryes

# # # print (binary)
# # # print (binaryes)
# # # # print (bin(ts))

# # # # for var in range(key):
# # # #     print(var)    

# # # A = 0b1100
# # # B = 0b0010

# # # print(bin(A^B))

# # # Python program to illustrate the
# # # conversion of ASCII to Binary


# # # Python program to illustrate the
# # # conversion of ASCII to Binary

# # # Calling string.encode() function to
# # # turn the specified string into an array
# # # of bytes
# byte_array = input("masukan teks : ").encode()

# # # Converting the byte_array into a binary
# # integer
# binary_int = int.from_bytes(byte_array,"big")

# # Converting binary_int to a string of
# # binary characters
# binary_string = bin(binary_int)


# byte_arrays = input("masukan key : ").encode()

# # Converting the byte_array into a binary
# # integer
# binary_integer = int.from_bytes(byte_arrays,"big")

# # Converting binary_int to a string of
# # binary characters
# binary_strings = bin(binary_integer)



# ts = binary_int ^ binary_integer

# # Getting the converted binary characters
# print(bin(ts))


# var  =  input("masukan plain teks = ")
# key  =  input("masukan key = ")

# binary = " ".join(format(ord(x), "b")for x in var )
# binaryes = " ".join(format(ord(c), "b")for c in key )
# normal = "".join(format(chr(int(c, 2))for c in var.split(" ")))

# kali  = len(str(binary))

# print (normal)
# print(kali)

# print (binary)
# print (binaryes)
# print (binary)
# print (binaryes)



def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(string): 
        return(key) 
    else: 
        for i in range(len(string) -len(string)): 
            key.append(key[i % len(string)])
    # print (binary)
    return("".join(key))
    

def enkripsixor(string,key):
    chiper= ""
    for i in string:
        for j in key :
            chiper += chr(ord(i)^ord(j))
    print("Maka chiperteks dari ",string,"adalah ",chiper)
    
    # print(binary)
    # chiperteks = ""
    # for C in string:
    #     chiperteks += format(ord(C) ^ key)
    # print ("chipertext dari ",string,"yaitu : ",chiperteks)

string = input('Masukan string : ')
key = input('Masukan key : ')
key = generateKey(string,key)
enkripsixor(string,key)