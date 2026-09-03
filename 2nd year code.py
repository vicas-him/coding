username = input ("input your name")
year = 2026
birth = input ("enter your year")
birth = float (birth)
age = (year- birth)
age = float (age)
print ("you are",age)


number = input ("enter a number")
number = int (number)
if number %2 == 0:
    print ("your number is even")
else:
    print ("your number is odd")

sentence = input ("enter a random sentence")
total = 0 
for letter in sentence:
    if letter == "a":
        total = total + 1
    elif letter == "o":
            total = total + 1
    elif letter == "i":
        total = total + 1
    elif letter == "w":
        total = total + 1
    elif letter == "u":
        total = total + 1
print ("you have ",(total),"vowels")
        
