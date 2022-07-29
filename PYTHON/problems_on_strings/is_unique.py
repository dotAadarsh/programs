# implement an algorithm that checks if a string has unique characters

max_char = 256

def isUnique(str):
    if(len(str) > max_char):
        return False
    chars = [False] * max_char
    for i in range(len(str)):
        index = ord(str[i]) # ord - returns the number representing the unicode code of a specified character   
        if(chars[index] == True):
            return False
        chars[index] = True
    return True

input = "LovethwayuliE"

if(isUnique(input) == True):
    print("Unique characters")
else:
    print("Not unique")
