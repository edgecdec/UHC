import os
import zipfile

#Diameters of borders
baseSize = 48
smallSize = baseSize / 3

#TIMES ARE IN SECONDS
initialTimeBeforeStartShrinking = 0
initialTimeToShrinkOver = 20
defaultTimeToShrinkOver = 5
initialWorldBorderDiameter = 480
timeBetweenShrinks = 10

#Center Coords
xCenter = 0
zCenter = 0

startPath = "uhc/data/uhc/functions/border/"
callPath = "uhc:border/"

#Add to tick function:
    #function uhc:border/border_helper

def buildCommands(xCenter, zCenter):
    line1 = f"worldborder set {baseSize}\n"
    line2 = f"worldborder center {xCenter} {zCenter}\n"
    line3 = f"worldborder set {smallSize} {defaultTimeToShrinkOver}\n"
    return f"{line1}{line2}{line3}"

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))

#See each tick if we need to change border
with open(f"{startPath}border_helper.mcfunction", "w") as borderFile:
    startTime = initialTimeBeforeStartShrinking * 20
    borderFile.write(f"execute if score borderTimer BorderTimer matches {startTime} run function {callPath}start_border_shrink\n")
    startTime += initialTimeToShrinkOver * 20
    timeToSetBackTo = startTime - (defaultTimeToShrinkOver + timeBetweenShrinks) * 20
    borderFile.write(f"execute if score borderTimer BorderTimer matches {startTime} run function {callPath}border_segment_one\n")
    startTime += (defaultTimeToShrinkOver + timeBetweenShrinks) * 20
    borderFile.write(f"execute if score borderTimer BorderTimer matches {startTime} run function {callPath}border_segment_two\n")
    startTime += (defaultTimeToShrinkOver + timeBetweenShrinks) * 20
    borderFile.write(f"execute if score borderTimer BorderTimer matches {startTime} run function {callPath}border_segment_three\n")
    startTime += (defaultTimeToShrinkOver + timeBetweenShrinks) * 20
    borderFile.write(f"execute if score borderTimer BorderTimer matches {startTime} run function {callPath}border_segment_four\n")
    borderFile.write("scoreboard players add borderTimer BorderTimer 1\n")

#Create Initial Border
with open(f"{startPath}border_creator.mcfunction", "w") as borderFile:
    borderFile.write(f"worldborder set {initialWorldBorderDiameter}\n")
    borderFile.write(f"worldborder center {xCenter} {zCenter}\n")
    borderFile.write("scoreboard objectives add BorderTimer dummy \"Border Timer\"\n")
    borderFile.write("scoreboard players set borderTimer BorderTimer 0\n")

#Create Inital Shrink
with open(f"{startPath}start_border_shrink.mcfunction", "w") as borderFile:
    borderFile.write(f"worldborder set {baseSize} {initialTimeToShrinkOver}\n")

#Shrink border to first segment
with open(f"{startPath}border_segment_one.mcfunction", "w") as borderFile:
    newXCenter = xCenter + smallSize
    newZCenter = zCenter + smallSize
    borderFile.write(buildCommands(newXCenter, newZCenter))

#Shrink border to second segment
with open(f"{startPath}border_segment_two.mcfunction", "w") as borderFile:
    newXCenter = xCenter - smallSize
    newZCenter = zCenter + smallSize
    borderFile.write(buildCommands(newXCenter, newZCenter))

#Shrink border to third segment
with open(f"{startPath}border_segment_three.mcfunction", "w") as borderFile:
    newXCenter = xCenter - smallSize
    newZCenter = zCenter - smallSize
    borderFile.write(buildCommands(newXCenter, newZCenter))

#Shrink border to foruth segment & start repeart
with open(f"{startPath}border_segment_four.mcfunction", "w") as borderFile:
    newXCenter = xCenter + smallSize
    newZCenter = zCenter - smallSize
    borderFile.write(buildCommands(newXCenter, newZCenter))
    #Repeat border shrinking
    borderFile.write(f"scoreboard players set borderTimer BorderTimer {timeToSetBackTo}\n")

#Turn whole datapack into .zip file
zipf = zipfile.ZipFile('UHC.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('uhc/', zipf)
zipf.close()
