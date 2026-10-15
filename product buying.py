city = input ('enter the name of thr city:')
product = input ('enter the name of the product:')
amount = input ('enter the quantity you purchased')
amount = float (amount)
dublinC = 0.5
galwayC = 0.4
corkC = 0.45
dublinW = 0.80
quantity = (amount * amount)

if (city == 'Dublin'):
    if (product == 'coffee'):
        print ('your amount is:',dublinC)
if (city == 'Galway'):
    if (product == 'coffee'):
        print ('your amount is:',galwayC)
if (city == 'Cork'):
    if (product == 'coffee'):
        print ('your amount is:',corkC)
if (city == 'Dublin'):
    if (product == 'water'):
        print ('your amount is:',dublinW)
if (city == 'Galway'):
    if (product == 'water'):
        print ('your amount is:',galwayW)
if (city == 'Cork'):
    if (product == 'water'):
        print ('your amount is:',corkW)


        
