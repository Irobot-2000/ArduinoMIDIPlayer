import mido
fileName = input("Enter file name  without .mid: ")
mid = mido.MidiFile("midi/" + fileName + ".mid")
notes = []
lastStartTime = 0
lastStopTime = 0
durations = []
time = 0
tempo = mid.ticks_per_beat * 4

#extract notes and durations 
count = 700
for msg in mid:
    time += msg.time
    if msg.is_meta: continue
    if msg.channel == 0:
        if count == 0: break
        count -= 1
        if msg.type == "note_on":
            notes.append( round(440 * 2 ** ((msg.note - 69) / 12)) )
            if lastStopTime != time:
                notes.append(-1)
                durations.append(time - lastStopTime )
            lastStartTime = time

        elif msg.type == "note_off":
            lastStopTime = time
            durations.append(time - lastStartTime)

#normalize durations
for i in range(len(durations)):
    durations[i] = round(durations[i] * tempo / 4)
print(durations)


def listToStringList(list):
    for i in range(len(list)):
        list[i] = str(list[i])

listToStringList(durations)
listToStringList(notes)

with open("notes.cpp","w") as notesFile:
    notesFile.write('#include "include.h"\n'
    + "short melody[] = {"
    + ",".join(notes) 
    + "}; \n"
    + "byte noteDurations[] = {"
    + ",".join(durations)
    + "};\n"
    + "int length = "
    + str( len(notes) )
    +";"
     )
print("done")
