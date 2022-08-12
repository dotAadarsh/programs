'''
"a" - Append - will append at end of the file
"w" - Write - will overwrite any existing content
'''
f = open("demofile2.txt", "a")
f.write("Now the file has more content")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

# overwrite the content
f = open("demofile3.txt", "w")
f.write("Oops! I have deleted the content.")
f.close()

f = open("demofile3.txt", "r")
print(f.read())


# Create a new file
'''
"x" - create - will create a file, returns an error if the file exist
"a" - append - will crate afile if the specified does not exist
"w" - write - will create a file if the specified file does not exist
'''

f = open("myfile.txt", "x") # Empty file is created
f = open("myfile.txt", "w") # Create a new file if it does not exist