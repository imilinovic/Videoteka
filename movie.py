class Movie:
    def __init__(self, list):
        self.name = list[0]
        self.year = list[1]
        self.length = list[2]
        self.owner  = 1
    def __str__(self):
        return "{} iz {}. godine u trajanju od {} minuta".format(self.name, self.year, self.length)
