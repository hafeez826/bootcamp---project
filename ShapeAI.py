import hashlib
import string
import random

my_string = input('Enter your string to hash: ')
hash_obj = hashlib.md5(my_string.encode())
hashCode = hash_obj.hexdigest()
print(hashCode)
generated = input("hash code generated from online tool: ")
if(hashCode == generated):
    print("yeah it's correct")
else:
    print("not correct")
    


print("------hashlib algorithms-----")
#print(hashlib.algorithms_guaranteed)
newString = input("enter another string: ")

newHash = hashlib.blake2s()
hashCode_1 = newHash.hexdigest()
print("balke2s of entered string ","'", newString, "'", " is ", hashCode_1)

newHash = hashlib.sha3_256()
hashCode_2 = newHash.hexdigest()
print("sha3_256 of entered string ", "'", newString, "'", " is ", hashCode_2)

newHash = hashlib.sha3_384()
hashCode_3 = newHash.hexdigest()
print("balke2s of entered string ", "'", newString, "'", " is ", hashCode_3)

M = 7
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = M))
res_1 = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = M))
abc = res + newString + res_1
hash_obj = hashlib.md5(abc.encode())
hashCode_4 = hash_obj.hexdigest()
print("---salting of string--")
print("STRING added at starting of string: ", res)
print("STRING added at end of string: ",  res_1)
print("actual string: ", newString)
print("after salting: ", hashCode_4)
print("---ITERATION---")

hash_obj = hashlib.md5(abc.encode())
hashCode_5 = hash_obj.hexdigest()



N = int(input("enter no of times you want iteration: "))
for i in range(N):
    hash_obj = hashlib.md5(hashCode_5.encode())
    hashCode_5 = hash_obj.hexdigest()
print("after" , N, "iterations hashing is: ", hashCode_5)
