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
    if char == " " and tempString != "":
        scaleWithoutSpaces.append(tempString)
        tempString = ""
    else:
        tempString += char
scaleWithoutSpaces.append(tempString)
print(scaleWithoutSpaces)

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

print (scaleNotes)
print (scaleNotesIndex)

#generating chord notes indexes
chord = []
chordsIndexes = []
for i in range(7):
    counter = i
    chord = []
    for n in range(3):
        chord.append(scaleNotesIndex[counter])
        counter += 2
        if counter > 6:
            counter -= 7
    chordsIndexes.append(chord)

print(chordsIndexes)

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

print(spacing)

#matching spacing to a chord
def matchChord(funcSpacing):
    chordType = ""
    if (funcSpacing[0] == 3):
        if (funcSpacing[1] == 6):
            chordType = "dim"
        elif (funcSpacing[1] == 7):
            chordType = "min"
    if (funcSpacing[0] == 4):
        if (spacing[1] == 6):
            chordType = "b5"
        elif (funcSpacing[1] == 7):
            chordType = "maj "
    return chordType

for i in range(7):
    print(scaleNotes[i], matchChord(spacing[i]))
