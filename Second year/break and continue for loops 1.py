count = 0
while count < 7:
    count += 1
    if count == 8:
        continue
    print (count)
    
    
for count2 in range (1,21):
    if count2 %2 == 0:
        continue
    print (count2)
    
    
count3 = input ("enter a word or sentence:")
for apple in count3:
    if apple == "e":
        print ("an e was detected in the word/sentence:",count3)
        break
    print ("no e was detected inside of the word/sentence:",count3)


count = 0
while count < 100:
    count += 1
    if count == 101:
        break
    print (count)



