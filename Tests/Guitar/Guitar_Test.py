import unittest

from src.Guitar.Guitar import Guitar
from src.Tab.Note import Note


class TestString(unittest.TestCase):

    def testGenerateGuitarStringE(self):
        guitar = Guitar()
        exp_notes = ['E', 'F', 'F_SHARP', 'G', 'G_SHARP', 'A', 'A_SHARP', 'B', 'C', 'C_SHARP', 'D', 'D_SHARP', 'E',
               'F', 'F_SHARP', 'G', 'G_SHARP', 'A', 'A_SHARP', 'B', 'C', 'C_SHARP', 'D', 'D_SHARP', 'E']
        exp_octaves = [1,1,1,1,1,1,1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2,2,2,2,3]
        notes = []
        octaves = []
        for note in guitar.getStringNotes(0):
            notes.append(note[0])
            octaves.append(note[1])

        self.assertEqual(exp_notes, notes, 'notes do not match')
        self.assertEqual(exp_octaves, octaves, 'octaves do not match')

    def testGenerateGuitarStringA(self):
        guitar = Guitar()
        exp_notes = ['A', 'A_SHARP', 'B', 'C', 'C_SHARP', 'D', 'D_SHARP', 'E', 'F', 'F_SHARP', 'G', 'G_SHARP',
                     'A', 'A_SHARP', 'B', 'C', 'C_SHARP', 'D', 'D_SHARP', 'E', 'F', 'F_SHARP', 'G', 'G_SHARP', 'A']
        exp_octaves = [ 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
        notes = []
        octaves = []
        for note in guitar.getStringNotes(1):
            notes.append(note[0])
            octaves.append(note[1])

        self.assertEqual(exp_notes, notes, 'notes do not match')
        self.assertEqual(exp_octaves, octaves, 'octaves do not match')

    def testGetd1(self):
        guitar = Guitar()
        res = guitar.getNote(Note('D', 1))
        self.assertEqual([(0, 10), (1, 5), (2, 0)], res )