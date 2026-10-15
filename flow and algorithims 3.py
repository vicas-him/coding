length1 = input ('enter the length of the right side of your shape')
length2 = input ('enter the length of the left side of your shape')
length3 = input ('enter the length of the bottem side of your shape')
length4= input ('enter the length of the bottem side of your shape')
internal = input ('enter the internal angle of your shape')
internal = int (internal)



if length1 == length2:
    if length1 == length3:
        if length2 == length4:
            if internal == 90:
                print ('IT IS A SQUARE')
            else:
                print ('ITS A RHOMBUS')
        else:
            print ('ITS AN IRREGULAR')
    else:
        print ('ITS AN IRREGULAR QUADRILATERAL')

