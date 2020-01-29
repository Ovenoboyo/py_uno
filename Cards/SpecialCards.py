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


class Wildcard(object):
    def __init__(self, color):
        self.color = color
        self.type = "SPECIAL"
        self.name = "SKIP"
        self.number = -2
        self.is_draw_4 = False


class DrawCard:
    def __init__(self, color):
        self.color = color
        self.type = "SPECIAL"
        self.name = "SKIP"
        self.number = -2
        self.color = None

