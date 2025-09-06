# create function that has any number of arguments (Arbitrary Argument)
# we can call such function with 1,2,3 or more arguments 
def getmax(*number):
    max = number[0]
    for num in number:
        if max<num:
            max=num
    return max
max=getmax(500,200,1000,600)
print(max)
