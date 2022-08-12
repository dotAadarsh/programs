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

albums = ['Mainstream sellout', 'Hotel Diablo', 'Ticket to my downfall']
newlist = []
for x in albums:
    if "H" in x:
        newlist.append(x)

print(newlist)

albums = ['Mainstream sellout', 'Hotel Diablo', 'Ticket to my downfall']
newlist = [ x for x in albums if "M" in x] # With list comprehension
print(newlist)      

# Sort List Alphanumerically
colors = ['Green', 'Yellow', 'Blue', 'Black', 'Brown']
colors.sort() # ascending, by default
print(colors)

colors = ['Green', 'Yellow', 'Blue', 'Black', 'Brown']
colors.sort(reverse=True) # Sort Descending
print(colors)

# Customize Sort Function
def myfunc(n):
    return abs(n-10)

nums = [43, 56, 77, 8678, 454]
nums.sort(key = myfunc)
print(nums)

# case-insensitive sort function
colors = ['Green', 'Yellow', 'Blue', 'black', 'brown']
colors.sort(key=str.lower)
print(colors)

# Reverse Order
colors = ['Green', 'Yellow', 'Blue', 'black', 'brown']
colors.reverse()
print(colors)

# Copy a List
colors = ['Green', 'Yellow', 'Blue', 'black', 'brown']
mylist = colors.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list()
colors = ['Green', 'Yellow', 'Blue', 'black', 'brown']
mylist = list(colors)
print(mylist)

# Join Two Lists

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
list3 = list1 + list2
print(list3)

#  join two lists is by appending all the items
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
for x in list2:
    list1.append(x)
print(list1)

# using extend() method
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
list1.extend(list2)
print(list1)

# TUPLE -  used to store multiple items in a single variable #
exampleTuple = ("GitHub", "Stackoverflow", "Dev.to")
print(exampleTuple)

# Tuple items are ordered, unchangeable, and allow duplicate values

# Tuples allow duplicate values
exampleTuple = ("GitHub", "Stackoverflow", "Dev.to", "GitHub")
print(exampleTuple)

# To determine how many items a tuple has, use the len() function
exampleTuple = ("GitHub", "Stackoverflow", "Dev.to", "Medium")
print(len(exampleTuple))

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
exampleTuple = ("GitHub",)
print(type(exampleTuple))

exampleTuple = ("GitHub")
print(exampleTuple)

# The tuple() Constructor
exampleTuple = tuple(("GitHub", "Stackoverflow", "Dev.to", "Medium"))
print(exampleTuple)

# Access Tuple Items
exampleTuple = ("GitHub", "Stackoverflow", "Dev.to", "Medium")
print(exampleTuple[2])
print(exampleTuple[-2]) # Negative Indexing
print(exampleTuple[1:3]) # Range of Indexes

# Check if Item Exists
exampleTuple = ("GitHub", "Stackoverflow", "Dev.to", "Medium")
if "Medium" in exampleTuple:
    print("Medium exist in the tuple")

thisSet = {"Twitch, Twitter", "Telegram"} # Sets are used to store multiple items in a single variable.
print(thisSet)

# Set items are unordered, unchangeable, and do not allow duplicate values.

print(len(thisSet)) # Len of set

# Set can be of any data type and can contain different data types
set1 = {"python", "is", "awesome"}
set2 = {1, 2, 3, 4, 5}
set3 = {True, False, True}
set4 = {"abc", 123, True, "def"}

print(set1, set2, set3, set4)

print(type(set4)) # sets are defined as objects with the data type 'set'

# Dictionaries are used to store data values in key:value pairs.

# Python Conditions and If statements

a = 12
b = 232
if b>a:
    print("b is greater than a")


a = 5
b = 5
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")


a = 55
b = 5
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Short Hand If
a = 4
b = 12
print("A") if a>b else print("B")

# and
a = 200
b = 33
c = 898
if a>b and c>b:
    print("Both conditions are True")

a = 200
b = 23
c = 3
if a>b or c>a:
    print("At least one of the condition is true")

# Nestedn if 
x = 40
if x>10:
    print("Above 10")
    if x>30:
        print("Above 30")
    else:
        print("Below 30")

# The pass statement - if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 45
b = 55
if b>a:
    pass 

# The while loop

i = 1
while i < 6:
    print(i)
    i += 1

# The break Statement
i = 1
while i<6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue Statement
i = 0
while i<6:
    i += 1
    if i == 3:
        continue
    print(i)

# for loops

media = ["Twitter", "Telegram", "Twitch"]
for x in media:
    print(x)

# looping through string

for x in "Gitpod":
    print(x)

# The range function
for x in range(6):
    print(x)

for x in range(20, 25):
    print(x)

for x in range(90, 100, 2):
    print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# creating a function

# A function is a block of code which only runs when it is called.

def my_function():
    print("Hello from function")

my_function() 

# Information can be passed into functions as arguments.

def greeting(fname):
    print("Hello " + fname)

greeting("MADMAX")

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def myFunction(*kids):
    print("The youngest child is " + kids[2])

myFunction("Hannah", "Baker", "Mark" ) 

# Keyword arguments
def my_function(child3, child2, child1):
    print("The youngest child is "+ child3)

my_function(child1 = "Emily",child2 = "Hannah", child3 = "Baker")

# Arbitrary Keyword Arguments, **kwargs

def my_function(**kid):
    print("the last name is " + kid["lname"])

my_function(fname = "Hannah", lname = "Baker")

# Passing a List as an Argument

def beverage(name):
    for x in name:
        print(x)

drinks = ["Coffee", "Tea", "Milk", "Beer"]
beverage(drinks)

# Return values

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(9))
print(my_function(15))

# Recursion
def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
    else:
        result = 0
    return result

print(tri_recursion(6))

# Lambda - A lambda function is a small anonymous function.

x = lambda a : a + 20
print(x(5))

# Lambda functions can take any number of arguments
x = lambda a,b : a*b
print(x(4, 5))

def myfun(n):
    return lambda a: a*n

mydoubler = myfun(2)
mytripler = myfun(3)
print(mydoubler(2))
print(mytripler(3))

# Classes and Objects
class MyClass:
    x = 1234

p1 = MyClass() 
print(p1.x) 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 32)

print(p1.name)
print(p1.age)

# Object Methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is "+ self.name)

p1 = Person("Eminem", 49)
p1.myfunc()

# The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belongs to the class

# Modify Object Properties
p1.age = 50
print(p1.name, p1.age)

# Delete Object Properties
del p1.age

# Inheritance
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Create a parent class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Aadarsh", "Kannan")
x.printname()

# Create a Child Class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("Aadarsh", "Kannan")
x.printname()

# Add the __init__() Function
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname): 
        
        '''# When you add the __init__() function, 
        the child class will no longer inherit the parent's __init__() function
        To keep the inheritance of the parent's __init__() function, 
        add a call to the parent's __init__() function:
        '''
        Person.__init__(self, fname, lname)

x = Student("Mad", "MAX")
x.printname()

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname): 
        
        '''Python also has a super() function that will make the child class 
        inherit all the methods and properties from its parent
        '''
        super().__init__(fname, lname)

x = Student("Altered", "Carbon")
x.printname()

# Add Properties

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Aadarsh", "Kannan", "2023")
print(x.graduationyear)

# Add Methods

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    
    def __init__(self, fname, lname, year): 
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome ", self.firstname, self.lastname, "to the class of ", self.graduationyear)

x = Student("Aadarsh", "Kannan", "2023")
x.welcome()

# Iterators - s an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# Return an iterator from a tuple, and print each value:
mytuple = ("favourite crime", "Drivers license", "Happier")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# Even strings are iterable objects, and can return an iterator
mystr = "Golden"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))

# Create an Iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# The example above would continue forever if you had enough next() statements, 
# or if it was used in a for loop.

# To prevent the iteration to go on forever, 
# we can use the StopIteration statement.

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <=10:
            x = self.a 
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

# Local Scope

def myfunc():
    x = 100
    print(x)

myfunc()

# Function Inside Function
def myfunc():
    x = 100
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

# Global scope
x = 69
def myfun():
    print(x)
myfun()
print(x)

# If you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables

x = 81
def fun():
    x = 11
    print(x)
fun()
print(x)

# Global Keyword - makes the variable globa
def myfun():
    global x
    x = 90
myfun()
print(x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword
x = 30
def globalfun():
    global x
    x = 20

globalfun()
print(x)

# Module
# Built-in-Modules
import platform
x = platform.system()
print(x)

#  dir() Function - function to list all the function names (or variable names) in a module. The dir() function
x = dir(platform)
print(x)

# Dates - date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects

import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) # takes one parameter, format, to specify the format of the returned string

# Math
x = min(10, 20, 30)
y = max(100, 123, 221)
z = abs(-5.123)
a = pow(2, 3)
print(x)
print(y)
print(z)
print(a)

import math
x = math.sqrt(81) # Returns square root
y = math.ceil(2.4) # rounds a number upwards to its nearest integer
z = math.floor(2.4) # rounds a number downwards to its nearest integer
a = math.pi #returns the value of pi

print(x)
print(y)
print(z)
print(a)

#JSON - JavaScript Object Notation
import json

# Parse JSON - Convert from JSON to Python
x  = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
print(y["city"])

# Convert from Python to JSON

# a py obj (dict)
x = {
    "name": "John",
    "age" : 30,
    "city": "New York"
}

y = json.dumps(x)
print(y)

# dict, list, tuple, string, int, float, True, False, None - you can convert these py objects to JSON strings

print(json.dumps({"name":"John", "age":30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(23))
print(json.dumps(3.1413))
print(json.dumps(True))
print(json.dumps(None))

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent

x = {
  "activity": "Color",
  "type": "relaxation",
  "participants": 1,
  "price": 0.1,
  "link": "",
  "key": "5322987",
  "accessibility": 0
}
print(json.dumps(x, indent=4, sort_keys=True)) # Order the Result using sort_keys

# RegEx - Regular Expression - used to check if a string contains the specified search pattern
import re
txt = "You'll find me alone at midnight"
x = re.search("midnight$", txt) # search if end with "midnight"

if x:
    print("Yes! Match found")
else:
    print("No match")

txt = "Seasons change and our love went cold"
x = re.findall("ol", txt) # Return a list containing every occurrence of "ol"
print(x)

# search() function searches the string for a match, and returns a Match object if there is a match
txt = "My hands are full, what else should I carry for you?"
x  = re.search("\s", txt)
print("The first white-space character is located in position: ", x.start())

# split() function returns a list where the string has been split at each match

x = re.split("\s", txt)
print(x)

# sub() function replaces the matches with the text of your choice

x = re.sub("\s", "_", txt)
print(x)

# Replace the first 3 occurrences:
x = re.sub("\s", "_", txt, 3)
print(x)

# Match object 
txt = "I know that dress is karma, perfume regret"
x = re.search("re", txt)
print(x)

# Try Except
'''
try - let you test a block of code for error
except - let you handle the error
else - lets you execute code when there is no error
finally - lets you execute code, regardless of the result of try- and except blocks
'''
# Exception handling

try:
    print(r)
except:
    print("An exception occured")  # Executed as r is not defined 

# Many exceptions
try:
    print(r)
except NameError:
    print("Variable r is not defined")   
except:
    print("Someting else went wrong")

# use the else keyword to define a block of code to be executed if no errors were raised

try:
    print("hello")
except:
    print("Something went wrong!")
else:
    print("Nothing went wrong")


# Finally - use regardless of try and except
try:
    print(r)
except:
    print("Something went wrong")
finally:
    print("The try-except is finished")

# Raise an exception
'''
x = -1
if x<0:
    raise Exception("Sorry, number is below zero")

# Raise a TypeError if x is not an integer
x = "hell"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
'''
# The above has been commented as it ends the program

# User Input

username = input("Enter username: ")
print("Username is: ", username)

# String formatting

# format() method allows you to format selected parts of a string
queue = 90
txt = "Number of songs in the queue is {}"
print(txt.format(queue))

# You can add parameters inside the curly brackets to specify how to convert the value
price = 55
txt = "The price of the product is {:.2f} dollars"
print(txt.format(price))

# Multiple values
quantity = 3
itemno = 123
price = 90
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders
quantity = 3
itemno = 123
price = 90
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# if you want to refer to the same value more than once, use the index number
quantity = 3
itemno = 123
price = 90
myorder = "I want {1} pieces of item number {1} for {2:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# Named indexes
myorder = "I have ordered a {carname}, it is a {model}"
print(myorder.format(carname = "Ford", model = "Mustang"))
