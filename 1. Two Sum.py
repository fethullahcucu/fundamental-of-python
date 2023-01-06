


target = 12
numbers = [4,5,1,2,3,8]

for i in numbers:
    for x in numbers:
        if x + i == 12:
            print ("index number is " + str(numbers.index(x))+ " and " +str(numbers.index(i)))
            break
        else:
            print ("continue")
    
        
