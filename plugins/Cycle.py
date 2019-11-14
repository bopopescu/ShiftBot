class Cycle:

    def __init__(self, list):
        self.i = 0
        self.list = list

    def next(self):
        self.i = (self.i + 1) % len(self.list)
        return self.list[self.i]

    def prev(self):
        self.i = (self.i - 1) % len(self.list)
        return self.list[self.i]

    def present(self):
        return self.list[self.i]

    def reset(self):
        self.i = 0
        return self.list[self.i]


if __name__ == '__main__':
    Cycle()
