# Print all the duplicates in the input string
def duplicates(songName):
    dupli = {}
    for i in range(len(songName)):
        if(songName[i] in dupli):
            dupli[songName[i]] += 1 
        else:
            dupli[songName[i]] = 1
    
    for i,j in dupli.items():
        if(j>1):
            print(i , ":" , j)
        

songName = "Let me down slowly"
duplicates(songName)