weight = input ('enter an object that is over 100 metres in weight')
weight = float (weight)
item = weight *9.8
item = float (item)
if (item > 500):
    print ('YOUR.ITEM.IS.TO.HEAVY')
elif (item < 100):
    print ('YOUR.ITEM.IS.TO.LIGHT')
else :
    print ('your item is below the required hight please enter another number')