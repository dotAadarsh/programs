def isAnagram(a, b):
    if (len(a) != len(b)):
        return False

    map = {}

    for i in range(len(a)):
        if(a[i] in map):
            map[a[i]] += 1
        else:
            map[a[i]] = 1
    
    for i in range(len(b)):
        if(b[i] in map):
            map[b[i]] -= 1
        else:
            return False

    keys = map.keys()

    for key in keys:
        if(map[key] != 0):
            return False
    return True

string1 = "secure"
string2 = "rescue"

if isAnagram(string1, string2):
    print("Given two string are anagram of each other")
else:
    print("Given two string are not anagram of each other")