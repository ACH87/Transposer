class Note:
    def __init__(self, note, x, y):
        self.note = note
        self.x = x
        self.y = y

    def print_vals(self):
        print(self.note + ' ' + str(self.x) + ' ' + str(self.y))