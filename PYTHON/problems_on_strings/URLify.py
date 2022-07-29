# Write a method to replace all spaces in a string with %20.

max = 1000

def replaceSpace(string):
    # remove white and trailing spaces
    string = string.strip()
    i = len(string)

    # count space and find current length
    space_count = string.count(' ')

    # find new length 
    new_length = i + space_count * 2

    # Check if new length is smaller than the provided string len 
    if new_length > max:
        return -1
    
    # start filling character from the end 
    index = new_length - 1
    string = list(string)

    # Fill string array
    for f in range(i-2, new_length -2):
        string.append('0')

    # fill rest of the string from end
    for j in range(i-1, 0, -1):
        if string[j] == ' ':
            string[index] = '0'
            string[index-1] = '2'
            string[index-2] = '%'
            index = index-3
        else:
            string[index] = string[j]
            index -= 1
    return ' '.join(string)


str1 = "Mr John Smith"
str2 =  replaceSpace(str1)
print(str2)
