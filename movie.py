class Movie:
    def __init__(self, list):
        self.name = str(list[0])
        self.year = str(list[1])
        self.length = str(list[2])
        self.id = str(list[3])
        self.owner  = str(list[4])
    def __str__(self):
        return "{} iz {}. godine u trajanju od {} minuta".format(self.name, self.year, self.length)
    def convert(self):
        return str(self.name) + ';' + str(self.year) + ';' + str(self.length) + ';' + str(self.id) + ';' + str(self.owner)
