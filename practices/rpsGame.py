import random, sys
# random is for generating rps value
# sys is for user to quit the game

print("ROCK, PAPER, SCISSORS")

win = 0
lose = 0
ties = 0

while True:

    print("%s Wins, %s Losses, %s Ties" % (win,lose,ties));

    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")

    #TODO: continuously ask for user input

    userInput = input()

    if userInput == 'r':
        print("ROCK versus...")
    elif userInput == 'p':
        print("PAPER versus...")
    elif userInput == 's':
        print("SCISSORS versus...")
    elif userInput == 'q':
        sys.exit()

    value = random.randint(1,3)
    if value == 1:
        print("PAPER")
        computerMove = 'p'
    elif value == 2:
        print("ROCK")
        computerMove = 'r'
    else:
        print("SCISSORS")
        computerMove = 's'

    if userInput == computerMove:
        print("It is a tie!")
        ties += 1
    elif (userInput == 'p' and computerMove == 'r') or (userInput == 'r' and computerMove == 's') or (userInput == 's' and computerMove == 'p'):
        print("You win!")
        win += 1
    elif (userInput == 'r' and computerMove == 'p') or (userInput == 's' and computerMove == 'r') or (userInput == 'p' and computerMove == 's'):
        print("You lose!")
        lose += 1