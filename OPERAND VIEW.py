num1 = input ('enter your first number')
num1 = float (num1)
num2 = input ('enter your second number')
num2 = float (num2)
oper = input ('enter an opperand [+ - * / %:')




if (oper == '+'):
    print (num1 + num2)
elif (oper == '-'):
    print (num1 - num2)
elif (oper == '*'):
    print (num1 * num2)
elif (oper == '/'):
    print (num1 / num2)
elif (oper == '%'):
    print (num1 % num2)
else :
    print ('ERROR OPERAND OR NUMBER NOT FOUND')



