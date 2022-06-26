from src.Tab.Note import Note
from src.Tab.Scale import Scale


class String:

    def __init__(self, starting_note, frets=24, base_string = 'E'):
        self.notes = self.generateString(starting_note, frets, base_string)

    def generateString(self, starting_note, frets, base_string):
        res = []
        note_counter = Scale[starting_note.name].value
        octave_counter = starting_note.octave
        while frets >= 0:
            res.append(Note(Scale(note_counter).name, octave_counter))
            note_counter = note_counter + 1 if note_counter < 11 else 0
            if Scale(note_counter).name == base_string: octave_counter += 1
            frets -= 1

        return res

    def getNotes(self):
        return self.notes

    """
    Returns tuple
    """
    def getStringNotes(self):
        res = []
        for n in self.notes:
            res.append((n.name, n.octave))
        return res






    #     self.scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    #
    #     self.notes = self.generate_note(note, frets)
    #     print(self.notes)
    #     print(len(self.notes))
    #
    # def generate_note(self, note, frets ):
    #     idx = self.scale.index(note)
    #     counter = frets
    #     result = []
    #
    #     while(counter >= 12):
    #         result += self.scale[idx: 12] + self.scale[0: idx]
    #         counter -= 12
    #
    #     result += self.scale[idx: idx + counter]
    #     return result