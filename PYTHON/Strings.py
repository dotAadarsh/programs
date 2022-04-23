# Strings in python are surrounded by either single quotation marks, or double quotation marks.
print('Lucid Dreams')
print("Hurt Myself")

# Assign String to a Variable
a = "Thinkin of you in my bed"
print(a)

# Multiline Strings - triple quotes
# three single quotes
a = '''I am not the only traveler
Who has not paid his dept
I've been searching for a trail to follow again
Take me back to the night we met'''
print(a)

# three double quotes
a = """I still see your shadows in my room
can't take back the love that i gave you
It's to the point where I love,
and I hate you"""
print(a)

# Arrays - Square brackets can be used to access elements of the string.
a = "When I was your man"
print(a[1])

# Looping Through a String
for x in "Hurts so good" :
    print(x)

# String Length
a = "My Luv"
print(len(a))

# Check String
a = "Just the way you are"
print("you" in a)

# Use it in an if statement:
if "you" in a:
    print("you are beautiful")

print("love" not in a)

if("love" not in a ):
    print("Alone")

# Slicing Strings - You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "you know you love me"
print(b[9:20])  
print(b[:8]) # Slice From the Start
print(b[13:]) # Slice To the End
print(b[-5:-2]) # Negative Indexing

# Upper Case
