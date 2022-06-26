"""
Class to represent tab object
"""

class Tab:

    def __init__(self):
        self.tab = []

    """
    Add a bar to the tab
    """
    def add_bar(self, bar):
        self.tab.append(bar)
