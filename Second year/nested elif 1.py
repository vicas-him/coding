mood = input ("enter your mood happy or sad:")
weather = input ("enter the weather sunny or rainy:")
if mood == "happy":
    if weather == "sunny":
        print ("default suggesting to 'pop-music' ")
    elif weather == "rainy":
                print ("default suggesting to 'top charts' ")
elif mood == "sad":
    if weather == "rainy":
            print ("default suggesting calming 'acoustic'")
    