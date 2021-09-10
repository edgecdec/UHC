from Team import Team

import csv

startPath = "uhc/data/uhc/functions/team_setup/"
callPath = "uhc:team_setup/"

TEAM_NAME_Q = "What is your team name?"
TIMESTAMP = "Timestamp"
SCHOOL = "What school is your team affiliated with? (if applicable)"
AUTO_PAIRED = "IF YOU ARE NOT REGISTERING A FULL TEAM OF 4, please indicate if you would like to be auto-paired with other small teams."
MINECRAFT_1 = "What is teammate #1's Minecraft username?"
DISCORD_1 = "What is teammate #1's Discord username?"
MINECRAFT_2 = "What is teammate #2's Minecraft username? (if applicable)"
DISCORD_2 = "What is teammate #2's Discord username? (if applicable)"
MINECRAFT_3 = "What is teammate #3's Minecraft username? (if applicable)"
DISCORD_3 = "What is teammate #3's Discord username? (if applicable)"
MINECRAFT_4 = "What is teammate #4's Minecraft username? (if applicable)"
DISCORD_4 = "What is teammate #4's Discord username? (if applicable)"

TEAM_COLORS = [
    "aqua",
    "blue",
    "dark_aqua",
    "dark_blue",
    "dark_gray",
    "dark_green",
    "dark_purple",
    "dark_red",
    "gold",
    "gray",
    "green",
    "light_purple",
    "red",
    "yellow",
    "black",
    "white"
    ]

resultsDict = csv.DictReader(open("IML UHC Team Signup.csv", encoding='utf-8'))

teams = []
for result in resultsDict:
    teamName = result[TEAM_NAME_Q]
    players = [result[MINECRAFT_1], result[MINECRAFT_2], result[MINECRAFT_3], result[MINECRAFT_4]]
    discords = [result[DISCORD_1], result[DISCORD_2], result[DISCORD_3], result[DISCORD_4]]
    teams.append(Team(len(teams) + 1, TEAM_COLORS[len(teams)], teamName, players, discords, result[SCHOOL], result[TIMESTAMP]))

for team in teams:
    print(team)

# Create Teams and add players to them
with open(startPath + "create_teams.mcfunction", "w") as outfile:
    for team in teams:
        curTeamNum = team.getNumber()
        outfile.write(f'#Create Team {curTeamNum} and add players\n')
        outfile.write(f'team add team{curTeamNum} "Team {curTeamNum}"\n')
        outfile.write(f'team modify team{curTeamNum} color {team.getTeamColorName()}\n')
        outfile.write(f'team modify team{curTeamNum} friendlyFire false\n')
        for player in team.players:
            if player == '':
                continue
            outfile.write(f'team join team{curTeamNum} {player}\n')
        outfile.write(f'\n')

#Create Whitelist Commands
with open("whitelist_commands.txt", "w") as outfile:
    for team in teams:
        for player in team.players:
            if player == '':
                continue
            outfile.write(f"execute as @p run whitelist add {player}\n")

