"""
File: craps.py

This module studies and plays the game of craps.
"""

from die import Die

class Player(object):

    def __init__(self):
        """Has a pair of dice and an empty rolls list."""
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []

    def __str__(self):
        """Returns a string representation of the list of rolls."""
        result = ""
        for (v1, v2) in self.rolls:
            result = result + str((v1, v2)) + " " +\
                     str(v1 + v2) + "\n"
        return result

    def getNumberOfRolls(self):
        """Returns the number of the rolls."""
        return len(self.rolls)

    def play(self):
        """Plays a game, saves the rolls for that game, 
        and returns True for a win and False for a loss."""
        self.rolls = []
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getValue(),
                    self.die2.getValue())
        self.rolls.append((v1, v2))
        initialSum = v1 + v2
        if initialSum in (2, 3, 12):
            return False
        elif initialSum in (7, 11):
            return True
        while (True):
            self.die1.roll()
            self.die2.roll()
            (v1, v2) = (self.die1.getValue(),
                        self.die2.getValue())
            self.rolls.append((v1, v2))
            laterSum = v1 + v2
            if laterSum == 7:
                return False
            elif laterSum == initialSum:
                return True

def playOneGame():
    """Plays a single game and prints the results."""
    player = Player()
    youWin = player.play()
    print(player)
    if youWin:
        print("You win!")
    else:
        print("You lose!")

def playManyGames(number):
    """Plays a number of games and prints statistics."""
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in range(number):
        hasWon = player.play()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    print("The average number of rolls per win is %0.2f" % \
          (winRolls / wins))
    print("The average number of rolls per loss is %0.2f" % \
          (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins / number))

def main():
    """Plays a number of games and prints statistics."""
    number = int(input("Enter the number of games: "))
    playManyGames(number)

if __name__ == "__main__":
    main()
    import random

class Player:
    def __init__(self):
        # State variables initialized
        self.roll = ""          # String representation of last roll
        self.rollsCount = 0     # Number of rolls in current game
        self.atStartup = True   # True before first roll
        self.winner = False     # True if player has won
        self.loser = False      # True if player has lost
        self.point = None       # Point established after first roll

    def rollDice(self):
        # Roll two dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        # Update roll count and string representation
        self.rollsCount += 1
        self.roll = f"({die1}, {die2}) total = {total}"
        print(self.roll)

        if self.atStartup:
            # First roll logic
            self.atStartup = False
            if total in (7, 11):
                self.winner = True
            elif total in (2, 3, 12):
                self.loser = True
            else:
                self.point = total  # Establish point
        else:
            # Subsequent roll logic
            if total == self.point:
                self.winner = True
            elif total == 7:
                self.loser = True

        return (die1, die2)

    def getNumberOfRolls(self):
        return self.rollsCount

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser

    def reset(self):
        # Optional helper to reset player state before new game
        self.roll = ""
        self.rollsCount = 0
        self.atStartup = True
        self.winner = False
        self.loser = False
        self.point = None
def playOneGame():
    player = Player()
    player.reset()
    while not (player.isWinner() or player.isLoser()):
        player.rollDice()
    if player.isWinner():
        print("You win!")
        return (True, player.getNumberOfRolls())
    else:
        print("You lose!")
        return (False, player.getNumberOfRolls())

def playManyGames():
    num_games = int(input("Enter the number of games: "))
    wins = 0
    losses = 0
    rolls_win = 0
    rolls_loss = 0

    for _ in range(num_games):
        won, rolls = playOneGame()
        if won:
            wins += 1
            rolls_win += rolls
        else:
            losses += 1
            rolls_loss += rolls

    print(f"The total number of wins is {wins}")
    print(f"The total number of losses is {losses}")
    print(f"The average number of rolls per win is {rolls_win / wins if wins else 0:.2f}")
    print(f"The average number of rolls per loss is {rolls_loss / losses if losses else 0:.2f}")
    print(f"The winning percentage is {wins / num_games:.3f}")
