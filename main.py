from art import rock,paper,scissors
import random

points = int(input("For how many points would you like to play?"))
user_points = 0
computer_points = 0

while points != user_points and points != computer_points:

    computer_choice=random.randint(0,2)
    user_choice=int(input("What do you want to choose? Type 0 for rock, 1 for paper and 2 for scissors."))
    if user_choice > 2:
        print("Invalid input.")
    else:
        if user_choice==0:
            print(rock)
        elif user_choice==1:
            print(paper)
        else:
            print(scissors)
        if computer_choice==0:
            print("computer's choice:\n"+rock)
        elif computer_choice==1:
            print("computer's choice:\n"+paper)
        else:
            print("computer's choice:\n"+scissors)
        if computer_choice==user_choice:
            print("it's draw.")
            print("Your points = "+str(user_points))
            print("Computer's points = "+str(computer_points))
        elif user_choice==0:
            if computer_choice==1:
                computer_points += 1
                print("You lose!")
                print("Your points = "+str(user_points))
                print("Computer's points = "+str(computer_points))
            else:
                user_points += 1
                print("You win!")
                print("Your points = "+str(user_points))
                print("Computer's points = "+str(computer_points))
        elif user_choice==1:
            if computer_choice==0:
                print("You win!")
                user_points += 1
                print("Your points = "+str(user_points))
                print("Computer's points = "+str(computer_points))
            else:
                print("You lose!")
                computer_points += 1
                print("Your points = "+str(user_points))
                print("Computer's points = "+str(computer_points))
        else:
            if computer_choice==0:
                print("You lose!")
                computer_points += 1
                print("Your points = "+str(user_points))
                print("Computer's points = "+str(computer_points))
            else:
                user_points += 1
                print("You win!")
                print("Your points = "+str(user_points))
                print("Computer's points = "+str(computer_points))


if computer_points >= points:
    print("Computer is the winner of this game!")
elif user_points >= points:
    print("You are the winner of this game.")