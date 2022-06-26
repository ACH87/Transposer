from src.Guitar.Guitar import Guitar


class Convertor:

    def __init__(self, tuning = None, frets = None):

        if tuning is None and frets is None:
            self.guitar = Guitar()
        elif tuning is None and frets is not None:
            self.guitar = Guitar(frets=frets)
        elif tuning is not None and frets is None:
            self.guitar = Guitar(tuning=tuning)
        else:
            self.guitar = Guitar(tuning, frets)

    def convertNotes(self, notes):
        temp = []

        for note in notes:
            temp.append(self.guitar.getNote(note))

        res = []

        for value in temp:
            if len(res) == 0:
                res.append(value[0])

            # else:
            # TODO calculate the nearest note based on euclidean distance
            #     for fret in value:
