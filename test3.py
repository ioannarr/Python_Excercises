# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

string1='montevideo'
string2='buenosaires'

encuentro = {}
def busco():
    for x in range(0, len(string1)):
        for y in range(x+1, len(string1)):
            if string1.count(str(x)) == string1.count(str(y)):
                encuentro[x] =1
                print(encuentro)
            else:
                encuentro[x]=-1
        for i in range(len(string1)):
            if encuentro[x]==1:
                return i
        break

