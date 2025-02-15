from movie import Movie

class Database_movie:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name) as f:
            self.file_lines = f.read().splitlines()
        f.close()

        self.movies = []
        for item in self.file_lines:
            temp = item.split(';')
            self.movies.append(Movie([temp[0], temp[1], temp[2], temp[3], temp[4]]))

    def update_file(self):
        open(self.file_name, "w").close()
        with open(self.file_name, 'w') as f:
            for item in self.file_lines:
                f.write(item + '\n')
        f.close()

    def print(self):
        print(self.file_lines)

    def add_to_index(self, index, movie):
        self.file_lines.insert(index, movie.convert())
        self.movies.insert(index, movie)
        self.update_file()

    def delete_index(self, index):
        del self.file_lines[index]
        del self.movies[index]
        self.update_file()

    def get_movies(self, name, flag=False):
        ret = []
        lo = 0
        hi = len(self.movies) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if self.movies[mid].name < str(name):
                lo = mid + 1
            else:
                hi = mid
        if flag:
            return lo

        for i in range (lo + 3):
            if i >= len(self.movies):
                break
            if name in self.movies[i].name:
                ret.append(self.movies[i])
        return ret

    def exists(self, id):
        for movie in self.movies:
            if movie.id == str(id):
                return True
        return False

#tmp = Database_movie("data.txt")
#mov = Movie([ "The Matrix", "1999", 122, 1, "admin"])
#tmp.delete_index(0)
#tmp.add_to_index(5, mov)
#tmp.print()
