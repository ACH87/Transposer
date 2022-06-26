import unittest

from src.Tab.Note import Note
from src.Guitar.String import String


class TestString(unittest.TestCase):

    def testGenerateStringE(self):
        string = String(Note('E', 1))
        exp_notes = ['E', 'F', 'F_SHARP', 'G', 'G_SHARP', 'A', 'A_SHARP', 'B', 'C', 'C_SHARP', 'D', 'D_SHARP', 'E',
               'F', 'F_SHARP', 'G', 'G_SHARP', 'A', 'A_SHARP', 'B', 'C', 'C_SHARP', 'D', 'D_SHARP', 'E']
        exp_octaves = [1,1,1,1,1,1,1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2,2,2,2,3]
        notes = []
        octaves = []
        for note in string.notes:
            notes.append(note.name)
            octaves.append(note.octave)

        self.assertEqual(exp_notes, notes, 'notes do not match')
        self.assertEqual(exp_octaves, octaves, 'octaves do not match')

    def testGenerateStringA(self):
        string = String(Note('A', 1))
        exp_notes = ['A', 'A_SHARP', 'B', 'C', 'C_SHARP', 'D', 'D_SHARP', 'E', 'F', 'F_SHARP', 'G', 'G_SHARP',
                     'A', 'A_SHARP', 'B', 'C', 'C_SHARP', 'D', 'D_SHARP', 'E', 'F', 'F_SHARP', 'G', 'G_SHARP', 'A']
        exp_octaves = [ 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
        notes = []
        octaves = []
        for note in string.notes:
            notes.append(note.name)
            octaves.append(note.octave)

        self.assertEqual(exp_notes, notes, 'notes do not match')
        self.assertEqual(exp_octaves, octaves, 'octaves do not match')

    def testGenerateStringD(self):
        string = String(Note('D', 1))
        exp_notes = ['D', 'D_SHARP', 'E', 'F', 'F_SHARP', 'G', 'G_SHARP',
                     'A', 'A_SHARP', 'B', 'C', 'C_SHARP', 'D', 'D_SHARP', 'E', 'F', 'F_SHARP', 'G', 'G_SHARP', 'A',
                     'A_SHARP', 'B', 'C', 'C_SHARP', 'D']
        exp_octaves = [ 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]
        notes = []
        octaves = []
        print(exp_notes[19], exp_octaves[19])
        for note in string.notes:
            notes.append(note.name)
            octaves.append(note.octave)

        self.assertEqual(exp_notes, notes, 'notes do not match')
        self.assertEqual(exp_octaves, octaves, 'octaves do not match')

    def testGenerateStringG(self):
        string = String(Note('G', 2))
        exp_notes = [ 'G', 'G_SHARP',
                     'A', 'A_SHARP', 'B', 'C', 'C_SHARP', 'D', 'D_SHARP', 'E', 'F', 'F_SHARP', 'G', 'G_SHARP', 'A',
                     'A_SHARP', 'B', 'C', 'C_SHARP', 'D', 'D_SHARP', 'E', 'F', 'F_SHARP', 'G']
        exp_octaves = [ 2, 2, 2, 2, 2, 2,2,2,2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4,4,4, 4 ]
        notes = []
        octaves = []
        print(exp_notes[19], exp_octaves[19])
        for note in string.notes:
            notes.append(note.name)
            octaves.append(note.octave)

        self.assertEqual(exp_notes, notes, 'notes do not match')
        self.assertEqual(exp_octaves, octaves, 'octaves do not match')
