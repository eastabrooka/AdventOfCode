
class RockPaperSissorsRound:
    def __init__(self,Opponent,Response):
        if Opponent == 'A':
            self.Opponent = "Rock"
        elif Opponent == 'B':
            self.Opponent = "Paper"
        else:
            self.Opponent = "Scissors"

        if Response == 'X':
            self.Response = "Rock"
        elif Response == 'Y' :
            self.Response = "Paper"
        else:
            self.Response = "Scissors"
        pass

    def WinLossCheck(self):
        player = self.Response
        computer = self.Opponent

        LocalPoints = 0
        if player == "Rock" :
            LocalPoints += 1
        if player == "Paper":
            LocalPoints += 2
        if player == "Scissors":
            LocalPoints += 3


        if player == computer:
            print("Tie!")
            LocalPoints +=3
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
                LocalPoints += 6
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
                LocalPoints += 6
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
                LocalPoints += 6
        return LocalPoints

def GenerateScore(self):
    '''
    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
    In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

    :return:
    '''
    Score = 0



