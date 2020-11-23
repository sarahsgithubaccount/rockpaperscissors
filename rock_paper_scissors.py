from random import randint

#Print welcome message and rules
print ("Wlecome to Rock, Paper, Scissors! We'll play best 2 out of 3. When prompted, please type either 'Rock', 'Paper', or 'Scissors'.") 

t = ["Rock", "Paper", "Scissors"]

#set random play 0-2 because there are 3 possible moves, and the computer counts 0, 1, 2. 
computer = t[randint(0,2)]


#set conditions for the while loop
player = False
game = 0
#nested while loop. The loop relies on three conditions: game < 3 because the rules specify that 3 games are played per round.
#player==false because using the input function is what triggers the player's turn. Once a choice is made, player becomes true, and it needs to be reset to false at the end of the loop.

while game < 3:
    while player == False:
        player = input("Rock, Paper, Scissors? ")
        if player == computer:
            print("Tie! You and the computer chose the same answer.")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose! The computer chose", computer, "which beats", player)
            else:
                print("You win! You chose", player, "which beats", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose! The computer chose", computer, "which beats", player)
            else:
                print("You win! You chose", player, "which beats", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose! The computer chose", computer, "which beats", player)
            else:
                print ("You win! You chose", player, "which beats", computer)
      
    game += 1
    player = False
    computer = t[randint(0,2)] 
