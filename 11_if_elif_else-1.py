# write a program to calculate bmi and display obesity level of person from given height (foot and inch) and weight (kg).
'''
steps
1)accept height from user in feet and inch
2)accept weight from user in kg
3)calculate total inches
    total_inches= feet*12+inch
4)calculate heaight into meter from total inches
    heaight_m=total_inches*0.0254
5)calculate bmi
    bmi=weight/(heaight_m**2)
6)Check obesity level 
-if bmi < 18.5:then under weight
 elif bmi <= 25: then normal weight
 elif 18.5 <= bmi < 25: then normal weight
 else 25 <= bmi < 30: then overweight
'''
h_feet = int(input("Enter height(feet):"))
h_inch = int(input("Enter height(inches):"))
weight = int(input("Enter aWeight(kg):"))

total_inches = h_feet*12+h_inch
print("Total inches",total_inches)

h_inch_m = total_inches*0.0254
print("Height in to meter:",h_inch_m)

bmi = weight/(h_inch_m**2)
print("BMI:",bmi)

if bmi<18.5:
    level="underweight"
elif 18.5 <= bmi < 25:
    level="normal weight"
elif 25 <= bmi < 30:
    level = "overweight"
else:
    level="obesity"
    
print("obesity level:",level)