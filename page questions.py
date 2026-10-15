word = input ('enter a word')
lenght =(len(word))
if lenght  <10:
    print ('get more imaginative with your names')
if lenght  >10:
    print ('your imaginative')
for x in word:
    print (x)
    

item1 = input ('enter the cost of the item you would like to purchase')
item1 = float (item1)
item2 = input ('enter the cost of the second item you would like to purchase')
item2 = float (item2)
item3 = input ('enter the cost of the third item you would like to purchase')
item3 = float (item3)
preVAT = item1 + item2 + item3
preVAT = float (preVAT)
print (preVAT)
VAT = preVAT * 1.2
VAT = float (VAT)
discount = input ('do you have a discount answer yes or no:')
if discount == 'yes':
    print (VAT * 0.85)
if discount == 'no':
    print (VAT)
    
    
word1 
