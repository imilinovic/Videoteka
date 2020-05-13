import datetime
from movie import Movie

class Member:
    max_movies = 3
    max_date = 10
    fee_per_day = 1
    def __init__(self, list):
        self.name = list[0]
        self.last_name = list[1]
        self.id = list[2]
        self.fees = 0
        self.movies = {}

    def print_movies(self):
        if len(self.movies) == 0:
            return "Nemate posudenih filmova"
        ret = []
        for key, value in self.movies.items():
            temp_string = str(key) + ' ' + str(value)
            ret.append(temp_string)
        return ''.join(ret)

    def add_movie(self, movie, date):
        if len(self.movies) == self.max_movies:
            return "Već ste posudili {} filmova, vratite jedan od njih pa onda možete posuditi novi".format(max_movies)

        end_date = date + datetime.timedelta(days=self.max_date)
        self.movies[movie] = end_date
        return "Uspjesno ste posudili film {}".format(movie)

    def remove_movie(self, movie):
        end_date = self.movies[movie]
        delta_date = end_date - datetime.datetime.now()
        if delta_date.days > self.max_date:
            val = (delta_date.days - self.max_date) * self.fee_per_day
            self.fees += val

        del self.movies[movie]
        return "Uspjesno ste vratili film {}".format(movie)

class Database:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name) as f:
            self.file_lines = f.readlines()
    def print(self):
        for i in self.file_lines:
            print(i)


p = Movie(["The Matrix", 1997, 120])
mem = Member([ "Ivan", "Milinovic", 1])
print(mem.print_movies())
print(mem.add_movie(p, datetime.datetime.now()))
print(mem.print_movies())
print(mem.remove_movie(p))
print(mem.print_movies())
print(mem.fees)
