print ("Guess The Number X")
#number of Guesses 9
#number is 18
#number of  guesses left
# print game over
i = 0
n = 18
while(i<9):



    if i==0:
        print("you have 9 guesses")
    else:
        print("you have",9-i,"guesses left")
    x= int(input("Enter your digit : "))
    if x>n:
        print("your number is greater than X")
    elif x<n:
        print("your number is lesser than X")

    else:
        if x == n:
            print("conguratulation you guessed it \n Game Over")
            break

    if i == 8:

        print("Game Over")
    i = i + 1




