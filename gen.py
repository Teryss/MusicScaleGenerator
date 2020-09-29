modes = ("ioanian","dorian","phrygian","lydian","mixolydian","aeolian","locrian")
sharpNotes = ("a", "b#", "b","c","c#","d","d#","e","f","f#","g","g#")
flatNotes = ("a", "bb", "b","c","db","d","eb","e","f","gb","g","ab")
majorScaleSpacing = (2,2,1,2,2,2,1)

enteredScale = input("Enter a scale to generate: ")
enteredScale = enteredScale.lower()

#getting rid of spaces and appending everything in dictionary
tempString = ""
scaleWithoutSpaces = []
for char in enteredScale:
    if (char == " " and tempString != ""):
        scaleWithoutSpaces.append(tempString)
        tempString = ""
    else:
        tempString += char
scaleWithoutSpaces.append(tempString)

#checking if the scale note enetered matches
for i in range(12):
    if sharpNotes[i] == scaleWithoutSpaces[0] or flatNotes[i] == scaleWithoutSpaces[0]:
        scaleRootIndex = i

#checking if the mode enteres matches
if(scaleWithoutSpaces[1] == "major"):
    modeIndex = 0
elif (scaleWithoutSpaces[1] == "minor"):
    modeIndex = 5
for i in range(7):
    if modes[i] == scaleWithoutSpaces[1]:
        modeIndex = i


#creating scale in dictionary
scaleNotes = []
scaleNotesIndex = []

for i in range(7):
    counter = i + modeIndex
    if (counter > 6):
        counter -= 7
    scaleNotes.append(sharpNotes[scaleRootIndex])
    scaleNotesIndex.append(scaleRootIndex)
    scaleRootIndex += majorScaleSpacing[counter]
    if (scaleRootIndex > 11):
        scaleRootIndex -= 12

#generating chord notes indexes
chord = []
chordsIndexes = []
for i in range(7):
    counter = i
    chord = []
    for n in range(4):
        chord.append(scaleNotesIndex[counter])
        counter += 2
        if counter > 6:
            counter -= 7
    chordsIndexes.append(chord)

#calculating spacing between notes
numberOfNotes = len(chordsIndexes[0])
chordsIndexes_copy = chordsIndexes
spacing = []

for i in range(7):
    singleChordSpacing = []
    counter = 0
    for x in range(numberOfNotes-1):
        singleSpacing = chordsIndexes_copy[i][counter+1] - chordsIndexes_copy[i][0]
        counter +=1
        if(singleSpacing < 0):
            singleSpacing+= 12
        singleChordSpacing.append(singleSpacing)
    spacing.append(singleChordSpacing)
    
#matching spacing to a chord
def matchChord(funcSpacing, counter, only3notechords):
    chordNotes = sharpNotes[chordsIndexes[counter][0]].upper() + " " + sharpNotes[chordsIndexes[counter][1]].upper() + " " + sharpNotes[chordsIndexes[counter][2]].upper() + " "
    if (funcSpacing[0] == 3):
        if (funcSpacing[1] == 6):
            chordType = "dim"
        elif (funcSpacing[1] == 7):
            chordType = "min"
        if(len(funcSpacing) == 3 and only3notechords == "false"):
            if(funcSpacing[2] == 10):
                chordType += "7"
            elif(funcSpacing[2] == 11):
                chordType += "(maj7)"

    if (funcSpacing[0] == 4):
        if (spacing[1] == 6):
            chordType = "b5"
        elif (funcSpacing[1] == 7):
            chordType = "maj "
        if(len(funcSpacing) == 3 and only3notechords == "false"):
            if(funcSpacing[2] == 10):
                chordType = "7"
            elif(funcSpacing[2] == 11):
                chordType = "maj7"
    chord = sharpNotes[chordsIndexes[counter][0]].upper() + " " + chordType + " - " + chordNotes
    return chord

print("Basic chords in " + enteredScale.upper() +": ")
for i in range(7):
    print(matchChord(spacing[i], i, "true"))

print("\n7th chords in " + enteredScale.upper() +": ")
for i in range(7):
    print(matchChord(spacing[i], i, "false"))
