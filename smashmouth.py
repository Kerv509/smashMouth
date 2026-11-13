class Players:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

class NFLTeam:
    def __init__(self, teamName, playerList):
        self.teamName = teamName
        self.playerList = playerList

    def displayTeam(self):
        print("Team:", self.teamName)
        for player in self.playerList:
            print(player.playerName, "-", player.playerPosition)

def main():
    player1 = Players("Joe Montana", "QB")
    player2 = Players("Barry Sanders", "RB")
    player3 = Players("Jerry Rice", "WR")
    player4 = Players("Graham Gano", "K")

    playerList = [player1, player2, player3, player4]

    team = NFLTeam("Smashmouth All stars", playerList)
    team.displayTeam()


main()