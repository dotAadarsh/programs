# open() function returns a file object, which has a read() method for reading the content of the file

f = open("demofile.txt", "r")
''' print(f.read()) '''

# Read Only Parts of the File
''' print(f.read(2))'''

# You can return one line by using the readline() method
'''
print(f.readline())
print(f.readline())
'''

# Loop through the file line by line:
for x in f:
    print(x)

# Close the file when you are finish with it
f.close()