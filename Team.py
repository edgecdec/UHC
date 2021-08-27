class Team:
    def __init__(self, number, color, teamName, players, discords, school="None", timeCreated="N/A"):
        self.number = number
        self.teamColor = color
        self.teamName = teamName
        self.players = self.checkPlayers(players)
        self.discords = self.checkDiscords(discords)
        self.timeCreated = timeCreated

        if school == "":
            school = "None"
        self.school = school

    def __str__(self):
        output = f"TEAM {self.number}: {self.teamName} ({self.teamColor}):\n"
        for player in self.players:
            output += f"\t{player}\n"
        return output + "\n"

    def checkPlayers(self, players):
        for player in players:
            if player == "":
                players.remove(player)
        if len(players) > 4:
            print("TOO MANY PLAYERS")
        return players[:min(4, len(players))]

    def checkDiscords(self, discords):
        for discord in discords:
            if discord == "":
                discords.remove(discord)
        if len(discords) > 4:
            print("TOO MANY DISCORDS")
        return discords[:min(4, len(discords))]

    def getTeamColorName(self):
        return self.teamColor

    def getNumber(self):
        return self.number
