# Program: Zodiac Sign Finder

# Accept date and month
date = int(input("Enter birth date (1-31): "))
month = input("Enter birth month (e.g. March): ").strip().lower()

# Determine zodiac sign
zodiac = ""

if (month == "march" and date >= 21) or (month == "april" and date <= 19):
    zodiac = "Aries"
elif (month == "april" and date >= 20) or (month == "may" and date <= 20):
    zodiac = "Taurus"
elif (month == "may" and date >= 21) or (month == "june" and date <= 21):
    zodiac = "Gemini"
elif (month == "june" and date >= 22) or (month == "july" and date <= 22):
    zodiac = "Cancer"
elif (month == "july" and date >= 23) or (month == "august" and date <= 22):
    zodiac = "Leo"
elif (month == "august" and date >= 23) or (month == "september" and date <= 22):
    zodiac = "Virgo"
elif (month == "september" and date >= 23) or (month == "october" and date <= 22):
    zodiac = "Libra"
elif (month == "october" and date >= 23) or (month == "november" and date <= 21):
    zodiac = "Scorpio"
elif (month == "november" and date >= 22) or (month == "december" and date <= 21):
    zodiac = "Sagittarius"
elif (month == "december" and date >= 22) or (month == "january" and date <= 19):
    zodiac = "Capricorn"
elif (month == "january" and date >= 20) or (month == "february" and date <= 18):
    zodiac = "Aquarius"
elif (month == "february" and date >= 19) or (month == "march" and date <= 20):
    zodiac = "Pisces"
else:
    zodiac = "Invalid date or month entered!"

# Display result
print("Your Zodiac Sign is:", zodiac)
