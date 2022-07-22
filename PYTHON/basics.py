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

txt = "Album sold for {price:.2f} dollars"
x = txt.format(price = 20) # The format() method formats the specified value(s) and insert them inside the string's placeholder
print(x)

# some format method types
txt = "World's population is {:_} and increasing" # Use a underscore as a thousand separator
print(txt.format(1408374094)) 

txt = "The Temperature is between {:+} and {:+}" # Use "+" to always indicate if the number is positive or negative
print(txt.format(-3,7)) 

# More on - https://www.w3schools.com/python/ref_string_format.asp

txt = "Cause there's magic in my bones"
print(txt.index("magic")) # index() method finds the first occurrence of the specified value

txt = "Pickingthepiecesupandbuildingtothesky123456"
print(txt.isalnum()) # Check if all the characters in the text are alphanumeric

txt = "zeronite"
print(txt.isalpha()) # Check if all the characters in the text are letters

txt = "\u0033"
print(txt.isdecimal()) # Check if all the characters in the unicode object are decimals

txt = "12345"
print(txt.isdigit()) # Check if all the characters in the text are digits

txt = "DemoText"
print(txt.isidentifier()) # isidentifier() method returns True if the string is a valid identifier, otherwise False

txt = "2two"
print(txt.isidentifier())

txt = "when i was your man"
print(txt.islower()) # Check if all the characters in the text are in lower case

txt = "hello 123"
print(txt.islower())

txt = "2134345"
print(txt.isnumeric()) # Check if all the characters in the text are numeric

txt = "234.234"
print(txt.isnumeric()) # Returns False

txt = "Hello there!"
print(txt.isprintable()) # Check if all the characters in the text are printable

txt = "Hello \n there !"
print(txt.isprintable()) # Returns False

txt = "        "
print(txt.isspace()) # Check if all the characters in the text are whitespaces

txt = "  p  "
print(txt.isspace()) # Returns False

txt = "I Walk Through The Valley Of The Shadow Of Death"
print(txt.istitle()) # Check if each word start with an upper case letter

txt = "I Walk Through the valley of the shadow of death"
print(txt.istitle()) # Returns False

txt = "HELLO, AND WELCOME TO MY WORLD"
print(txt.istitle()) # Returns False

txt = "This Is %'!?"
print(txt.istitle()) # Returns True

txt = "HELLO, AND WELCOME TO MY WORLD"
print(txt.isupper()) # Check if all the characters in the text are in upper case

myTuple = ("John", "Wick", "Boogeyman")
print("|".join(myTuple)) # Join all items in a tuple into a string  

myDict = {"name": "john", "country": "Italy"}
mySeparator = "FROM"
print(mySeparator.join(myDict)) # Join all items in a dictionary into a string

txt = "Girl, you know I want your love"
print(txt.split()) # Split a string into a list where each word is a list item

txt = "   love   "
print(txt.strip()) # Remove spaces at the beginning and at the end of the string

txt = ",,,...love...zzz,,,"
print(txt.strip(".,z")) # Remove the leading and trailing characters

print(10 > 11)
print(11==11)
print(10 < 11)
print(bool("hello"))
print(bool(99))

# Print a message based on whether the condition is True or False
a = 3
b = 5
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

# The following will return False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Functions can Return a Boolean
def boolfn():
    return True

print(boolfn())

# Operators are used to perform operations on variables and values

# Arithmetic Operators
print(5+5) # Addition
print(3-2) # Subtraction
print(2*7) # Multiplication
print(8/2) # Division
print(7%3) # Modulus
print(3**3) # Exponentiation
print(15//2) # Floor division

# Assignment Operators
x = 5 # Same as X = 5
print(x)

x += 3 # Same as x = x + 3
print(x)

x -= 4 # Same as x = x - 4
print(x)

x *= 2 # Same as x = x * 2
print(x)

x /= 8 # Same as x = x / 8
print(x)

x = 55
x %= 7 # Same as x = x % 7
print(x)

x = 77
x //= 4 # Same as x = x // 4
print(x)

x **= 2
print(x) # Same as x = x ** 2

x = 5
x |= 3
print(x) # Same as x = x | 3

x ^= 2
print(x) # Same as x = x ^ 2

x >>= 4
print(x) # Same as x = x >> 4

x = 5
x <<= 3 # Same as x = x << 3
print(x) 

# Comparison Operators
x = 6
y = 5
print(x == y) # Equal
print(x != y) # Not equal
print(x > y) # Greater than
print(x < y) # Less than
print(x >= y) # Greater than or equal to
print(x <= y) # Less than or equal to

# Logical Operators
x = 5
print(x > 3 and x < 10) # Returns True if both statements are true
print(x > 3 or x < 10) # Returns True if one of the statements is true
print(not(x > 3 and x < 10)) # Reverse the result, returns False if the result is true

# Identity Operators
x = ["Juice", "Wrld"]
y = ["Juice", "Wrld"]
z = x
# Returns True if both variables are the same object
print(x is z)
print(x is y)
print(x == y)

# Returns True if both variables are not the same object	
print(x is not z)
print(x is not y)
print(x != y)

# Membership Operators
print("Juice" in  x) # Returns True if a sequence with the specified value is present in the object	
print("Wrld" not in y) # Returns True if a sequence with the specified value is not present in the object

# Bitwise Operators
print(2^3) # Sets each bit to 1 if only one of two bits is 1
print(5|4) # Sets each bit to 1 if one of two bits is 1
print(7^3) # Sets each bit to 1 if only one of two bits is 1
print(~5) # Inverts all the bits
print(5>>3) # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print(7<<3) # Shift left by pushing zeros in from the right and let the leftmost bits fall off

'''
Lists are used to store multiple items in a single variable
created using square brackets
'''

albums = ["Dawn FM", "Death bed", "lovely"]
print(albums) # Print list
print(len(albums)) # Print the number of items in the list

# List items can be of any data type
list1 = ["Dawn FM", "Death bed", "lovely"]
list2 = [1, 2, 32, 4, 6]
list3 = [True, False, False, True]
print(list1, list2, list3)

# A list can contain different data types
list1 = [23, "twenty three", True, "23"]
print(list1)

print(type(list1)) # From Python's perspective, lists are defined as objects with the data type 'list'

# list() Constructor - use the list() constructor when creating a new list
mylist = list(("Dawn FM", "Death bed", "lovely"))
print(mylist)

print(mylist[1]) # Access items in the list
print(mylist[-1]) # Negative Indexing

albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
print(albums[2:5]) # Range of Indexes

# Check if Item Exists
if "Clouds" in albums:
    print("Yes, album is present")

# Change item Value
albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
albums[1] = "Death bed"
print(albums)

# Change a Range of Item Values
albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
albums[1:3] = ["Folklore", "Divide"]
print(albums)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
albums[1:3] = ["Folklore", "Divide", "Handwritten notes"]
print(albums)

# insert() method inserts an item at the specified index
albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
albums.insert(2, "Starboy")
print(albums)

# To add an item to the end of the list, use the append() method
albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
albums.append("Ticket to my downfall")
print(albums)

# To append elements from another list to the current list, use the extend() method
albums1 = ['Therapy session', 'Perception']
albums2 = ['The Search', 'Clouds', 'Chasing...']
albums1.extend(albums2)
print(albums1)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
albums1 = ['Therapy session', 'Perception']
albums2 = ('The Search', 'Clouds', 'Chasing...') # Tuple
albums1.extend(albums2) # Add elements of a tuple to a list
print(albums1)

# The remove() method removes the specified item
albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
albums.remove("Clouds")
print(albums)

# The pop() method removes the specified index.
albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
albums.pop(2)
print(albums)

# If you do not specify the index, the pop() method removes the last item
albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
albums.pop()
print(albums) 

# The del keyword also removes the specified index
albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
del albums[3]
print(albums)

# The del keyword can also delete the list completely
albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
del albums

# The clear() method empties the list. The list still remains, but it has no content
albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
albums.clear()
print(albums)

# loop through the list items by using a for loop
albums = ['Therapy session', 'Perception', 'The Search', 'Clouds', 'Chasing...']
for x in albums:
    print(x)

# Loop Through the Index Numbers
albums = ['Mainstream sellout', 'Hotel Diablo', 'Ticket to my downfall']
for i in range(len(albums)):
    print(i)

# List Comprehension offers the shortest syntax for looping through list
albums = ['Mainstream sellout', 'Hotel Diablo', 'Ticket to my downfall']
[print(x) for x in albums]
