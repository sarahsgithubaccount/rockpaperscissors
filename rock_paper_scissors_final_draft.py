from random import randint #imports the random module

#Print welcome message and rules
name = input("Welcome to Rock, Paper, Scissors! What is your name? ") 
print("")
print ("Hello", name+"!", "When prompted, please type either 'Rock', 'Paper', or 'Scissors'. \nThe first to win 3 games is the winner! Time to play!")
print ("")
option_list = ["Rock", "Paper", "Scissors"]

#set random play 0-2 because there are 3 possible moves, and the index operator begins at 0. 
computer = option_list[randint(0,2)]

#player==false because using the input function is what triggers the player's turn. Once a choice is made, player becomes true, and it needs to be reset to false at the end of the loop.
player = False

#this is the score. 
player_wins = 0
computer_wins = 0

while player == False:
    player = input("Rock, Paper, Scissors? ")
    print ("")
    if player == computer:
        print("Tie!", name, "and the computer chose the same answer.")
        print ("")
    elif player == "Rock":
        if computer == "Paper":
            print(name, "loses! The computer chose", computer, "which beats", player)
            print ("")
            computer_wins += 1
        else:
            print(name, "wins! You chose", player, "which beats", computer)
            print ("")
            player_wins += 1
    elif player == "Paper":
        if computer == "Scissors":
            print(name, "loses! The computer chose", computer, "which beats", player)
            print ("")
            computer_wins += 1
        else:
            print(name, "wins! You chose", player, "which beats", computer)
            print ("")
            player_wins += 1
    elif player == "Scissors":
        if computer == "Rock":
            print(name, "loses! The computer chose", computer, "which beats", player)
            print ("")
            computer_wins += 1
        else:
            print (name, "wins! You chose", player, "which beats", computer)
            print ("")
            player_wins += 1
    else:
        print ("Please check your spelling and try again")
        print ("")
      
    player = False #resets the loop condition to false
    computer = option_list[randint(0,2)] #resets the computer's moves
    print (name+"'s", "score: " ,player_wins,)
    print ("Computer's score: " ,computer_wins,)
    #prints out the score
    print ("")
    
    #identify the winner. User confirmation: the player can reset the loop if they want to play again.
    if player_wins == 3:
        print (name, "wins!")
        play_again = input("Enter 'Yes' to play again or 'No' to quit: ")
        if play_again == 'Yes':
            player_wins = 0
            computer_wins = 0
            continue
        else:
            print ("Thanks for playing" ,name+"!",)
            break
    if computer_wins == 3:
        print ("The computer wins!")
        play_again = input("Enter 'Yes' to play again or 'No' to quit: ")
        if play_again == 'Yes':
            player_wins = 0
            computer_wins = 0
            continue
        else:
            print ("Thanks for playing" ,name+"!",)
            break
                    
