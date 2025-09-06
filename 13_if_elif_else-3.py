#  write a program to accept birth date and month from user. decide zodiac sign from below table 
    # Aries: March 21–April 19
    # Taurus: April 20–May 20
    # Gemini: May 21–June 21
    # Cancer: June 22–July 22
    # Leo: July 23–August 22
    # Virgo: August 23–September 22
    # Libra: September 23–October 22
    # Scorpio: October 24–November 21
    # Sagittarius: November 22–December 21
    # Capricorn: December 22–January 19
    # Aquarius: January 20–February 18
    # Pisces: February 19–March 20
'''
steps
1)accept two inputs
    date=enter date
    month=enter month
2)if (mont == march and date >= 21) or (month == april and date <= 19) then print Aries
3)elif (mont == april and date >= 20) or (month == may and date <= 20) then print Taurus
4)elif (mont == may and date >= 21) or (month == june and date <= 21) then print Gemini
5)elif (mont == june and date >= 22) or (month == july and date <= 22) then print Cancer
6)elif (mont == july and date >= 23) or (month == august and date <= 22) then print Leo
7)elif (mont == augast and date >= 23) or (month == september and date <= 22) then print Virgo
8)elif (mont == september and date >= 23) or (month == october and date <= 22) then print Libra
9)elif (mont == october and date >= 24) or (month == november and date <= 21) then print Scorpio
10)elif (mont == november and date >= 22) or (month == december and date <= 21) then print Sagittarius
11)elif (mont == december and date >= 22) or (month == january and date <= 20) then print capricorn
12)elif (mont == january and date >= 20) or (month == february and date <= 18) then print Aquarius
13)elif (mont == febrarury and date >= 19) or (month == march and date <= 20) then print pices
14)else print(invalid date or month)
'''

date = int(input("Enter date of birt(eg.1-31)"))
month = input("Enter month of bith(eg.january)")

zodiac=""
    
if(month=="march" and date >= 21) or (month == "april" and date <= 19):
    zodiac = "Aries"
elif(month=="june" and date >= 22) or (month == "july" and date <= 22):
    zodiac="taurus"
elif(month == "may" and date >= 21) or (month == "june" and date <= 21):
    zodiac="Gemini"
    
    print(zodiac)
