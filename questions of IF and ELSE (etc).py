age = input ('what age are you?')
age = float (age)
if (age > 17):
    print ('you are eligible to vote')
elif (age < 18):
    print ('you are not eligible to vote')
else:
    print ('please enter only numbers next time please')
    
print ('.')
print ('.')
print ('.')
    
print('please iset a score from 1-100')
maths = input ('what did you get for your maths exam?')
maths = int (maths)
physics = input ('what did you get for your physics exam?')
physics = int (physics)
chemistry = input ('what did you get for your chemistry exam?')
chemistry = int (chemistry)
all_together = (maths + physics + chemistry)
all_together = int (all_together)
print ('you got:')
print (all_together)
if (all_together > 190):
    print ('you will make it on to the course')
elif (all_together < 190):
    print ('you did not make it on to the course')
    
