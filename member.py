import datetime
from movie import Movie

class Member:
    max_movies = 3
    max_date = 10
    fee_per_day = 1
    def __init__(self, list):
        self.name = str(list[0])
        self.last_name = str(list[1])
        self.id = str(list[2])
        self.fees = list[3]
        self.movies = list[4]
    def __str__(self):
        return self.name + ' ' + self.last_name + ' ' + self.id

    def convert(self):
        ret = [ self.name, '|', self.last_name, '|', self.id, '|', str(self.fees), '|' ]
        temp = []
        for movie, date in self.movies.items():
            datum = str(date.day) + '.' + str(date.month) + '.' + str(date.year)
            temp.append( movie.convert() + ':' + datum + '&' )
        spoji1 = ''.join(ret)
        spoji2 = ''.join(temp)
        return spoji1 + spoji2

    def return_movies(self):
        if len(self.movies) == 0:
            return "Nemate posudenih filmova"
        ret = []
        for key, value in self.movies.items():
            temp_string = str(key) + ' ' + str(value)
            ret.append(temp_string)
        return ''.join(ret)

    def add_movie(self, movie, date):
        if len(self.movies) >= self.max_movies:
            return "Već ste posudili {} filmova, vratite jedan od njih pa onda možete posuditi novi".format(self.max_movies)

        end_date = date + datetime.timedelta(days=self.max_date)
        self.movies[movie] = end_date
        return "Uspjesno ste posudili film {}".format(movie)

    def remove_movie(self, movie):
        end_date = self.movies[movie]
        end_date = datetime.date(end_date.year, end_date.month, end_date.day)
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)

        delta_date = end_date - now
        if delta_date.days > self.max_date:
            val = (delta_date.days - self.max_date) * self.fee_per_day
            self.fees += val

        del self.movies[movie]
        return "Uspjesno ste vratili film {}".format(movie)



'''
p = Movie(["The Matrix", 1997, 120])
mem = Member([ "Ivan", "Milinovic", 1])
print(mem.print_movies())
print(mem.add_movie(p, datetime.datetime.now()))
print(mem.print_movies())
print(mem.remove_movie(p))
print(mem.print_movies())
print(mem.fees)
'''
