# Write a program that takes a date as input and outputs the date's season in the northern hemisphere. The input is a string to represent the month and an int to represent the dayOfMonth.
# The dates for each season in the northern hemisphere are:
# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19

print("Welcome to the Season Indicator Program (SIP). Please input the month and number of the date you want to determine the season of.\n")
month = input("What month is it?\n")
dayOfMonth = int(input("\nWhat number day is it?\n"))

if month.lower() == 'january':
    if not (1<=dayOfMonth<=31):
        print("\nInvalid")
    else:
        print("\nWinter")

elif month.lower() == 'february':
    if not (1<=dayOfMonth<=28):
        print("\nInvalid")
    else:
        print("\nWinter")

elif month.lower() == 'march':
    if not (1<=dayOfMonth<=31):
        print("\nInvalid")
    elif dayOfMonth <= 19:
        print("\nWinter")
    else:
        print("\nSpring")

elif month.lower() == 'april':
    if not (1<=dayOfMonth<=30):
        print("\nInvalid")
    else:
        print("\nSpring")

elif month.lower() == 'may':
    if not (1<=dayOfMonth<=31):
        print("\nInvalid")
    else:
        print("\nSpring")

elif month.lower() == 'june':
    if not (1<=dayOfMonth<=30):
        print("\nInvalid")
    elif dayOfMonth <= 20:
        print("\nSpring")
    else:
        print("\nSummer")

elif month.lower() == 'july':
    if not (1<=dayOfMonth<=31):
        print("\nInvalid")
    else:
        print("\nSummer")

elif month.lower() == 'august':
    if not (1<=dayOfMonth<=31):
        print("\nInvalid")
    else:
        print("\nSummer")

elif month.lower() == 'september':
    if not (1<=dayOfMonth<=30):
        print("\nInvalid")
    elif dayOfMonth <= 21:
        print("\nSummer")
    else:
        print("\nAutumn")

elif month.lower() == 'october':
    if not (1<=dayOfMonth<=31):
        print("\nInvalid")
    else:
        print("\nAutumn")

elif month.lower() == 'november':
    if not (1<=dayOfMonth<=30):
        print("\nInvalid")
    else:
        print("\nAutumn")

elif month.lower() == 'december':
    if not (1<=dayOfMonth<=31):
        print("\nInvalid")
    elif dayOfMonth <= 20:
        print("\nAutumn")
    else:
        print("\nWinter")

else:
    print("\nInvalid")