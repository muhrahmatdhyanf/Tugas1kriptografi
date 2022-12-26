print("MUHAMMAD RAHMAT DHYAN FAHRUDDIN")
print("E1E120084")
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) -len(key)): 
            key.append(key[i % len(key)])
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
