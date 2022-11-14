from mido import Message, MidiFile, MidiTrack
from pitch import Pitch
from tempo import Tempo
from velocity import Velocity
from note_recognition import fromFileToNote


mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)


bpm, notes = fromFileToNote("example.txt")
tempo = Tempo(bpm)

track.append(Message('program_change', program=12, time=0))

i=0
notes[i]

#primeira nota
track.append(Message('note_on', note = notes[i].pitch, velocity = notes[i].velocity, time=0))
track.append(Message('note_off', note = notes[i].pitch, velocity = notes[i].velocity, time=0))
i+=1

#todas as outras
for i in range(1,len(notes)):

    track.append(Message('note_on', note = notes[i].pitch, velocity = notes[i].velocity, time=tempo.Time(notes[i-1].duration)))
    #observe que olhamos para a duração da última nota pra sabermos quando tocar a próxima, daí o notes[i-1].duration
    track.append(Message('note_off', note = notes[i].pitch, velocity = notes[i].velocity, time=0))



mid.save('yourMidi.mid')