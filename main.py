print ("Seconds Calendar")
seconds = 60
minutes = 60
hours = 24
normalYear = 365
leapYear = 366

# Get user input
year = int(input("What year would you like to calculate?"))
yearType= input("Is it a leap year?")
print ("How many seconds are in the year?")
# Calculate seconds in a normal year
if yearType == "no":
    Year_seconds = seconds * minutes * hours * normalYear
    print ("There are", Year_seconds," seconds in the year")

# Calculate seconds in a leap year
else: 
    Year_seconds = seconds * minutes * hours * leapYear
    print ("There are", Year_seconds,"seconds in the year")

