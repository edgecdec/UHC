import os
import zipfile

#Diameters of borders
baseSize = 128
smallSize = baseSize / 3

#TIMES ARE IN SECONDS
initialTimeBeforeStartShrinking = 30 * 60
initialTimeToShrinkOver = 60 * 60
defaultTimeToShrinkOver = 2 * 60
initialWorldBorderDiameter = 4000
timeBetweenShrinks = 1 * 60

#Center Coords
xCenter = 0
zCenter = 0

START_PATH = "uhc/data/uhc/functions/border/"
CALL_PATH = "uhc:border/"

#Add to tick function:
    #function uhc:border/border_helper

def buildCommands(xCenter, zCenter):
    line1 = f"worldborder set {baseSize}\n"
    line2 = f"worldborder center {xCenter} {zCenter}\n"
    line3 = f"worldborder set {smallSize} {defaultTimeToShrinkOver}\n"
    return f"{line1}{line2}{line3}"

def zipDir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))

def createBorderSegmentCode(startPath, name, xPlusMinus, yPlusMinus, isLast=False):
    with open(f"{startPath}border_segment_{name}.mcfunction", "w") as borderFile:
        newXCenter = xCenter + (smallSize * xPlusMinus)
        newZCenter = zCenter + (smallSize * yPlusMinus)
        borderFile.write(buildCommands(newXCenter, newZCenter))

        if isLast: # Repeat border shrinking
            borderFile.write(f"scoreboard players set borderTimer BorderTimer {timeToSetBackTo}\n")

#See each tick if we need to change border
with open(f"{START_PATH}border_helper.mcfunction", "w") as borderFile:
    startTime = initialTimeBeforeStartShrinking * 20
    borderFile.write(f"execute if score borderTimer BorderTimer matches {startTime} run function {CALL_PATH}start_border_shrink\n")
    startTime += initialTimeToShrinkOver * 20
    timeToSetBackTo = startTime - (defaultTimeToShrinkOver + timeBetweenShrinks) * 20

    segmentNames = ['one', 'two', 'three', 'four']

    for segmentName in segmentNames:
        borderFile.write(f"execute if score borderTimer BorderTimer matches {startTime} run function {CALL_PATH}border_segment_{segmentName}\n")
        startTime += (defaultTimeToShrinkOver + timeBetweenShrinks) * 20

    borderFile.write("scoreboard players add borderTimer BorderTimer 1\n")

#Create Initial Border
with open(f"{START_PATH}border_creator.mcfunction", "w") as borderFile:
    borderFile.write(f"worldborder set {initialWorldBorderDiameter}\n")
    borderFile.write(f"worldborder center {xCenter} {zCenter}\n")
    borderFile.write("scoreboard objectives add BorderTimer dummy \"Border Timer\"\n")
    borderFile.write("scoreboard players set borderTimer BorderTimer 0\n")

#Create Inital Shrink
with open(f"{START_PATH}start_border_shrink.mcfunction", "w") as borderFile:
    borderFile.write(f"worldborder set {baseSize} {initialTimeToShrinkOver}\n")

#Shrink border in segments
createBorderSegmentCode(START_PATH, 'one', 1, 1, False)
createBorderSegmentCode(START_PATH, 'two', -1, 1, False)
createBorderSegmentCode(START_PATH, 'three', -1, -1, False)
createBorderSegmentCode(START_PATH, 'four', 1, -1, True)

#Turn whole datapack into .zip file
zipf = zipfile.ZipFile('UHC.zip', 'w', zipfile.ZIP_DEFLATED)
zipDir('uhc/', zipf)
zipf.close()
