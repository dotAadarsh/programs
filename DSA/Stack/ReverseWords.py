def reverse(s):
    stc = [] # Empty stack
    temp = "" # Temp string

    for i in range(len(s)):
        if s[i] == ' ':
            stc.append(temp)
            temp = ""
        else:
            temp = temp + s[i]

    stc.append(temp) # For last word

    while len(stc) != 0:
        temp = stc[len(stc) - 1]
        print(temp, end = ' ')
        stc.pop()

    print()

s = "wubba lubba dub dub!"
reverse(s)