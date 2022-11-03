from mido import Message, MidiFile, MidiTrack
from note import Note
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)


track.append(Message('program_change', program=12, time=0))


track.append(Message('note_on', note= Note.C4, velocity=64, time=0))

track.append(Message('note_on', note= Note.E4, velocity=64, time=0))

track.append(Message('note_on', note=Note.G4, velocity=64, time=0))


track.append(Message('note_off', note=Note.C4, velocity=127, time=1000))
track.append(Message('note_off', note=Note.E4, velocity=127, time=0))
track.append(Message('note_off', note=Note.G4, velocity=127, time=0))

track.append(Message('note_on', note=Note.Ab4, velocity=64, time=0))
track.append(Message('note_off', note=Note.Ab4, velocity=64, time=0))

mid.save('c_major.mid')