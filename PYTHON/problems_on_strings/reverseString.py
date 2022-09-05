# Print reverse of a string using recursion

def reverse(string):
    if len(string) == 0:
        return

    temp = string[0]
    reverse(string[1:])
    print(temp, end = '')
    


string = "Like a snake and then forsake"
reverse(string)
print()