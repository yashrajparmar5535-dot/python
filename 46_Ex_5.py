# create function that returns average of player score of all 11 players (arbitary arguments)

def getaverage(*p11):
    
    total= sum(p11)
    average=len(p11)
         
    return total/average
n = getaverage(11,52,42,10,0,2,55,21,65,45,4)
print(n)