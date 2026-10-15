day = input ('enter a day as a number between 1 and 31:')
day = float (day)
month = input ('enter a month as a number between 1 and 12:')
month = float (month)
digit = input ('enter a two digit year')
digit = float (digit)

year = (day * month)
year = float (year)

if year == digit :
    print ('your number is special')
else :
    print ('your number is not special')