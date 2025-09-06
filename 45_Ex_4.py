# create function that has arbitary arguments of string type and it display all strings into lower case.
# toLowerCase('Apple','bAnana','ManGO','KIWI','graps')
# output 
#     apple banana mango kiwi graps

# def tolower(*fruits):
#     print(f.lower() for f in fruits)
# tolower("Apple","BAnana","GRAPes")

def tolower(*fruits):
    print([n.lower() for n in fruits])
    
tolower("Apple","BAnana","GRAPes")
