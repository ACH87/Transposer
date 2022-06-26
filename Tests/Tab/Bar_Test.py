from src.Tab.Bar import Bar
from src.Tab.Note import Note
from src.Tab.Ties import Ties


def print_bar():
    tie = Ties(1, 2)
    e0 = Note('E', 0)
    a1 = Note('A', 0)
    d1 = Note('D', 0)

    bar = Bar((4,4), 100, [e0, a1, d1], tie)
    bar.print_notes()

print_bar()