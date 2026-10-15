age = input ('enter your age:')
age = float (age)
ID = input ('do you have ID yes or no?')
if (age > 18):
    if(ID == 'yes'):
        print ('you qualify to vote')
if (age < 18):
    if(ID == 'no'):
        print ('you do not qualify to vote')

