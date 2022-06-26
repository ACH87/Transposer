"""
Represent one bar in a tab
"""

class Bar:

    """
    Contructor takes in:
    time_sig (tuple): tuple represent time signature (3, 4) == 3/4
    bpm (int): beats per minute
    notes (2d_array): individual notes and chords
    """
    def __init__(self, time_sig = (4,4), bpm = 100, notes = [], ties = []):
        self.time_sig = time_sig
        self.bpm = bpm
        self.notes = notes
        self.ties = ties

    """
    mehtod to add notes
    """
    def add_note(self, notes):
        self.notes.append([notes])

    """
    method to add notes if was part of chord    
    """
    def add_chord(self, note):
        self.notes[len(self.notes) -1].append(note)

    """
    print notes
    """
    def print_notes(self):
        output = ''
        max = 16
        number_of_notes = len(self.notes)
        for i in range(number_of_notes):
            output += self.notes[i].name
            for j in range(int(max/self.notes[i].duration) -1):
                output += '-'

        for i in range(max - len(output)):
            output += '-'

        print(output)
        return output


"""
Represents beginning bar
"""
class Repeating_Bar(Bar):
    def __init__(self, time_sig, bpm, notes = []):
        super().__init__(time_sig, bpm, notes)
