
class RockPaperSissorsRound:
    def __init__(self,Opponent,EndGame):
        if Opponent == 'A':
            self.Opponent = "Rock"
        elif Opponent == 'B':
            self.Opponent = "Paper"
        else:
            self.Opponent = "Scissors"

        if EndGame == 'X':
            self.Response = "Lose"
        elif EndGame == 'Y' :
            self.Response = "Draw"
        else:
            self.Response = "Win"
        pass

    def WinLossCheck(self):
        player = self.Response
        computer = self.Opponent


        PlayerChoice = ""
        if self.Response == "Lose":
            if computer == "Paper":
                PlayerChoice = "Rock"
            if computer == "Rock":
                PlayerChoice = "Scissors"
            if computer == "Scissors":
                PlayerChoice = "Paper"

        if self.Response == "Win":
            if computer == "Paper":
                PlayerChoice = "Scissors"
            if computer == "Rock":
                PlayerChoice = "Paper"
            if computer == "Scissors":
                PlayerChoice = "Rock"

        if self.Response == "Draw":
            if computer == "Paper":
                PlayerChoice = "Paper"
            if computer == "Rock":
                PlayerChoice = "Rock"
            if computer == "Scissors":
                PlayerChoice = "Scissors"

        LocalPoints = 0
        if PlayerChoice == "Rock" :
            LocalPoints += 1
        if PlayerChoice == "Paper":
            LocalPoints += 2
        if PlayerChoice == "Scissors":
            LocalPoints += 3
        if player == "Win":
            LocalPoints+=6
        if player == "Draw":
            LocalPoints+=3
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



