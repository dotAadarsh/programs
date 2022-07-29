# Check Permutation - assume that there are no whitespaces and that our strings are case sensitive.

def findlen(str):
    length = 0
    for i in str:
        length += 1

    return length

def isPermutation(str1, str2):
    n1 = findlen(str1)
    n2 = findlen(str2)
    
    if n1!=n2:
        return False

    a = sorted(str1) # sortedfindlenns a sorted list of the specified iterable object
    str1 = " ".join(a) # join - Join all items in a tuple into a string
   
    b = sorted(str2)
    str2 = " ".join(b)

    for i in range(0, n1, 1):
        if(str1[i] != str2[i]):
            return False
        return True

str1 = "dog"
str2 = "god"

if(isPermutation(str1,str2)):
    print("Yes")
else:
    print("No")