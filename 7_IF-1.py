# Entered year is Millenium or not
'''
Steps
1)Take input from user
2)if number % 1000 == 0:
    print(Year is millenium)
3)if number % 1000 != 0:
    print(Year is not millenium)
'''
year = int(input("Enter Year:"))

if year % 1000 == 0:
    print(year,"year is millenium")
if year % 1000 != 0:
    print(year,"year is not millenium")
print("Good byy")
