from src.Tab.Note import Note
from src.Guitar.String import String


class Guitar():

    def __init__(self, tuning = [('E', 1), ('A',1), ('D', 1), ('G',2), ('B',2), ('E', 3)], frets = 24):
        self.strings = []
        for string in tuning:
            self.strings.append(String(Note(string[0], string[1]), frets, tuning[0][0]))

    def getStringNotes(self, num):
        return self.strings[num].getStringNotes()

    def getNote(self, value_note):
        #TODO change to numpy
        listOfMatchingFrets = []
        stringCounter = 0
        for string in self.strings:
            fret_counter = 0
            for fret in string.getNotes():
                if fret.name == value_note.name and fret.octave == value_note.octave:
                    listOfMatchingFrets.append((stringCounter, fret_counter))
                    break
                fret_counter += 1
            stringCounter += 1

        return listOfMatchingFrets