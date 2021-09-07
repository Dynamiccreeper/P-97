import random
    number=random.Randint(0,9)

    count =5
    while (count>=0):
        print(count)
        count=count-1
    if(guess == number):
        print("Congratulation YOU WIN!")
        break
    if not chances <5:
      print("You Lose !!! the Number is ", number)  
    print("Number guessing game")
    print("Guess a number (between 1 to 9)")
    guess=input("Enter your guess:-")




