# This is a Comment
'''
Since Python will ignore string literals that are not assigned to a variable, 
you can add a multiline string (triple quotes) in your code, and place your comment inside it:
This is a comment
written in
more than just one line
'''

print("Hello, World!")

#Python uses indentation to indicate a block of code.
if 7>2:
    print("Seven is greater than two")
# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

# Variables are containers for storing data values.
x = 5 # type int
y = "wubba lubba dub dub" # type str
print(x)
print(y)

# Casting
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0
print(x,y,z)

# Get the Type
x = 21
y = "Bones"
print(type(x))
print(type(y))

# String var can be declared either by using single or double quotes
x = "Hannah"
# is the same as
y = 'Hannah'

# Variable names are case-sensitive
Y = 45
y = "Enemy"
#y will not overwrite Y

'''
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
'''
myvar  ="Taylor"
my_var = "Taylor"
_my_var = "Taylor"
myVar = "Taylor"
MYVAR = "Taylor"
myvar1 = "Taylor"

# Multi Words Variable Names
myVariableName = "Bruno" # Camel case
MyVariableName = "Bruno" # Pascal case
my_variable_name = "Bruno" # Snake case

# Many Values to Multiple Variables
x, y, z = "Twitter", "Github", "Spotify"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Spotify"
print(x)
print(y)
print(z)

# Unpack a Collection
languages = ["Java", "Python", "Ruby"]
x, y, z = languages # unpacking.
print(x)
print(y)
print(z)

# Output Variables - output multiple variables, separated by a comma

x = "Java"
y = "is"
z = "awesome"
print(x, y, z)

# use the + operator to output multiple variables
x = "Java "
y = "is "
z = "awesome"
print(x + y + z)

# when you try to combine a string and a number with the + operator, Python will give you an error
# Output multiple variables in the print() function is to separate them with commas, which even support different data types
x = 5
y = "five"
print(x, y)

# Global Variables
x = "Let me down slowly"
def myfun():
    print(x + " by Alec Benjamin")
myfun()

x = "DJ Snake"
def song():
    x = "Ariana Grande" #Local
    print("Let me love you by " + x)
song()
print("Let me love you by " + x)

# To create a global variable inside a function, you can use the global keyword

def artist():
    global x
    x = "Eminem"
artist()
print("Godzilla by " + x)

# Data Types
x = "Let you down"
print(type(x))

x = 20
print(type(x))

x = 20.55
print(type(x))

x = 1j
print(type(x))

x = ["fake", "love", "dont", "last"]
print(type(x))

X = ("Staring", "at", "the", "sun")
print(type(x))

x = range(5)
print(type(x))

x = {"name": "Frank", "age": 32}
print(type(x))

x = {"Die", "for", "you"}
print(type(x))

x = frozenset({"Die", "for", "you"})
print(type(x))

x = False
print(type(x))

x = b'Burn'
print(type(x))

x = bytearray(4)
print(type(x))

x = memoryview(bytes(6))
print(type(x))

x = None
print(type(x))

#Strings are Arrays
a = "Hate the other side"
print(a[2])

# Strings are Arrays
for x in a:
    print(x)

# To get the length of a string, use the len() function
print(len(a))

# Check String - use in keyword
text = "The best things in life are free!"
if "best" in text:
    print("best is present")

# To check if a certain phrase or character is NOT present in a string use the keyword not in
text = "The best things in life are free!"
if "live" not in text:
    print("live is not present")

# You can return a range of characters by using the slice syntax.
q = "Take what you want from me"
print(q[5:18]) 
print(q[:4]) # Slice From the Start
print(q[10:]) # Slice To the End
print(q[-7: -2]) # Negative Indexing

print(q.upper()) # returns the string in upper case
print(q.lower()) # returns the string in lower case

q = " Take what you want from me                "
print(q.strip()) # removes any whitespace from the beginning or the end

q = "Take what you want from me"
print(q.replace("t", "m")) # replaces a string with another string
print(q.split(" ")) # split() method splits the string into substrings if it finds instances of the separator

# String Concatenation (+)
a = "Machine "
b = "Gun "
c = "Kelly"
d  = a+b+c
print(d)

# String Format - combine strings and numbers by using the format() method
songs = 20
text = "total songs in the queue {}"
print(text.format(songs))

# format() method takes unlimited number of arguments, and are placed into the respective placeholders
total_songs = 30
songs_played = 17
songs_in_queue = 13
status = "Total number of songs: {}\nTotal songs played: {}\nSongs in queue: {}"
print(status.format(total_songs, songs_played, songs_in_queue))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
status = "Total number of songs: {0}\nTotal songs played: {2}\nSongs in queue: {1}"
print(status.format(total_songs,songs_in_queue , songs_played))

# Escape Character (\)
print('It\'s all right!') # Single Quote
print('Inseting backslash \\') #Backslash
print("Emo\ngirl") # New line
print("Fell\rin") # Carriage Return
print("Hurts\tso\tgood") # Tab
print("love  \bthe way  \byou lie") # Backspace

#A backslash followed by three integers will result in a octal value
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

# String Methods - All string methods returns new values. They do not change the original string

txt = "One Night at the Call Centre"
x = txt.capitalize() # Upper case the first letter
print(x)

x = txt.casefold() # String casefold() - lowercase
print(x)

txt = "Eminem"
x = txt.center(10) # Returns a centered string
print(x)

txt = "Eminem"
x = txt.center(10, 'O') # Using the letter "O" as the padding character
print(x)

txt = "My baby, I'm just being honest"
x = txt.count("baby")
print(x)

txt = "You only get one shot, [shot] do not miss your chance to blow"
x = txt.count("shot", 10, 30)
print(x)

txt = "My name is Ståle"
x = txt.encode() # UTF-8 encode the string
print(x)

#These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

txt = "This is my life and these times are so hard."
x = txt.endswith(".") # Check if the string ends with a punctuation sign (.)
print(x) # return in bool

x = txt.endswith("so hard.") # Check if the string ends with the phrase "so hard."
print(x) 

x = txt.endswith("these times", 5, 10) # Check if position 5 to 10 ends with the phrase "these times"
print(x) 

txt = "E\tm\ti\tn\te\tm"
x =  txt.expandtabs(2) # Set the tab size to 2 whitespaces
print(x)

txt = "The club isn't the best place to find a lover"
x = txt.find("best") # Where in the text is the word
print(x)

# If the value is not found, the find() method returns -1, but the index() method will raise an exception:

txt = "Hello, welcome to my world."
print(txt.find("q"))
# print(txt.index("q")) raises exception