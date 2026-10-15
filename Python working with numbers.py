#Ask the user to enter a number
#REMEMBER: All input is string/text
number1 = input('Enter a number: ')
#tell the computer this input is an decimal number
number1 = float(number1)
#Complete the code to ask the user to enter a second number
number2 = input("please enter a second number")
#Tell the computer this input is a decimal number
number2 = float(number2)

#Add number1 and number2 and store the answer in a new variable
sum_of_number1_and_number2 = number1 + number2
#Multiply number1 and number2 and store the answer in a new variable

multiplication_of_number1_and_number2 = number1 * number2
#Subtract number2 from number1 and store the answer in a new variable
sub_of_number1_and_number2 = number1 - number2

#Divide number1 by number2 and store the answer in a new variable
divide_of_number1_and_number2 = number1 / number2

#print a message stating the result of adding the two numbers
print('The sum of the two numbers you entered is: ',sum_of_number1_and_number2)
#print a message stating the result of multiplying the two numbers
print('the multiplication of your numbers is:  ',multiplication_of_number1_and_number2)
#print a message stating the result of subtracting number2 from number1
print('the subtraction of your numbers is:   ',sub_of_number1_and_number2)
#print a message stating the result of dividing number1 by number2
print('the division of your numbers are:   ',divide_of_number1_and_number2)
