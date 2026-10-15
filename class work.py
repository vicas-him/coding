febD = input ('type a day of febuary')
if febD == '29':
    print ('it is a leap year')
if febD == '28':
    print ('it is not a leap year.')


num = input ('type a positive or negative number')
num = int (num)
if num > 0:
    print ('your number is a positve number')
elif num == 0 :
    print ('your number is negative')
    

age = input ('enter your age')
age = int (age)
if age > 18:
    lisence = input ('do you have a lisence?')
    if lisence == 'no':
        print ('you cannot drive')
        if lisence == 'yes':
            print ('you are able to rent a car')
    
elif age < 18:
    print ('you cannot rent a car')

else:
    ('you cannot rent a car')