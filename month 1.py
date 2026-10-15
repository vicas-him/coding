month = input ('enter a month from 1 to 12:')
month = float (month)
if (month<=3):
    print ('is in the first quarter of the year')
elif (month<=6):
    print ('is in the second quarter of the year')
elif (month<=9):
    print ('is in the third year of the year')
elif (month<=12):
    print ('is in the last quarter of the year')
elif (month>12):
    print ('error quarter is not found')
      