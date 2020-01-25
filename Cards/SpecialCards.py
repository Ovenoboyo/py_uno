""" Special cards should have numbers in -ve"""


class Reverse(object):
    def __init__(self, color):
        self.color = color
        self.type = "SPECIAL"
        self.name = "REVERSE"
        self.number = -1


class Skip(object):
    def __init__(self, color):
        self.color = color
        self.type = "SPECIAL"
        self.name = "SKIP"
        self.number = -2
