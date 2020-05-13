from member import Member
from movie import Movie

class Database_member:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name) as self.file:
            self.file_lines = self.file.readlines()
    def print(self):
        for i in self.file_lines:
            print(i)
    def add_to_index(self, index, member):
        self.file_lines.insert(index, movie)
        self.file.write(self.file_lines)
    def finish(self):
        self.file.close()
    # ime prezime id fees movies

tmp = Database_movie("data.txt")
mem = Member([ "Ivan", "Milinovic", 1])
tmp.add_to_index(1, )
print(tmp.file_lines)
