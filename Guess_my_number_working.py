print ("Please think of a number between 0 and 100!")
minimum = 0
maximum = 100
guess = minimum + (maximum-minimum)//2
print ("Is your secret number " + str(int(guess)) + "?")
ans = str (input("Enter 'h' to indicate the guess is too high. "+\
            "Enter 'l' to indicate the guess is too low. "+\
            "Enter 'c' to indicate I guessed correctly. "))


while guess > 0 and guess < 100:
    
    if ans == "l":
        minimum = guess
        guess = minimum + (maximum-minimum)//2
        print ("Is your secret number " + str(int(guess)) + "?")
        ans = str (input("Enter 'h' to indicate the guess is too high. "+\
        "Enter 'l' to indicate the guess is too low. "+\
        "Enter 'c' to indicate I guessed correctly. "))
    #print (ans)
        
                               
    elif ans == "h":
        maximum = guess
        guess = minimum + (maximum-minimum)//2 
        print ("Is your secret number " + str(int(guess)) + "?")
        ans = str (input("Enter 'h' to indicate the guess is too high. "+\
            "Enter 'l' to indicate the guess is too low. "+\
            "Enter 'c' to indicate I guessed correctly. "))
        #print (ans)
    elif ans == "c":
        print("Thanks for fun! Dzieki za zabawe!")
        break
        
