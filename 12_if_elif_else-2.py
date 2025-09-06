# write a program to accept day of week and then display divas and ratri choghadiya
'''
steps
1)accept day of week Eg:-monday
2)check choghadiya according to input
    if day=monday then
'''
day=input("Enter day of week:")

if day == "monday":
    print("Divas Choghadiya: Udveg, Char, Labh, Amrit, Kaal, Shubh, Rog")
    print("Ratri Choghadiya: Shubh, Amrit, Char, Rog, Kaal, Labh, Udveg")

elif day == "tuesday":
    print("Divas Choghadiya: Rog, Udveg, Char, Labh, Amrit, Kaal, Shubh")
    print("Ratri Choghadiya: Labh, Shubh, Amrit, Char, Rog, Kaal, Udveg")

elif day == "wednesday":
    print("Divas Choghadiya: Labh, Amrit, Kaal, Shubh, Rog, Udveg, Char")
    print("Ratri Choghadiya: Kaal, Rog, Amrit, Shubh, Char, Labh, Udveg")

elif day == "thursday":
    print("Divas Choghadiya: Rog, Udveg, Char, Labh, Amrit, Kaal, Shubh")
    print("Ratri Choghadiya: Shubh, Amrit, Char, Rog, Kaal, Labh, Udveg")

elif day == "friday":
    print("Divas Choghadiya: Shubh, Rog, Udveg, Char, Labh, Amrit, Kaal")
    print("Ratri Choghadiya: Amrit, Char, Rog, Kaal, Labh, Shubh, Udveg")

elif day == "saturday":
    print("Divas Choghadiya: Kaal, Shubh, Rog, Udveg, Char, Labh, Amrit")
    print("Ratri Choghadiya: Char, Rog, Kaal, Amrit, Shubh, Labh, Udveg")

elif day == "sunday":
    print("Divas Choghadiya: Udveg, Char, Labh, Amrit, Kaal, Shubh, Rog")
    print("Ratri Choghadiya: Labh, Shubh, Amrit, Char, Rog, Kaal, Udveg")

else:
    print("Invalid day entered. Please enter a valid weekday (e.g., Monday).")