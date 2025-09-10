'''List 
------------------------------------
create program & do following task 
    1) create list store any 5 values 
    2) display list 
    3) insert 3 items one by one at begining 
    4) display list 
    5) insert 1 item @ 2nd position 
    6) display list 
    7) remove item at 1st position
    8) display list 
    9) remove last item 
    10) edit 1st item store "india"
    11) display list 
    12) clear list 
    13) display list 
    '''
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print(fruits)
fruits.insert(0,"Pineapple")
fruits.insert(0,"Strawberry")
fruits.insert(0,"Papaya")
print(fruits)
fruits.insert(2,"Kiwi")
print(fruits)
fruits.insert(1,"Guava")
print(fruits)
del fruits[1]
print(fruits)
del fruits[8]
print(fruits)
fruits[0] = "India"
print(fruits)
fruits.clear()
print(fruits)

