name = input ("enter your name")
number = input ("enter a number")
number = int (number)

if number < 10 :
    for x in range (number):
        print (name)
else:
    print ("too high")