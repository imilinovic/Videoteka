from member import Member
from movie import Movie
from database_mov import Database_movie
import datetime

class Database_member:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name) as f:
            self.file_lines = f.read().splitlines()
        f.close()

        self.members = []
        for item in self.file_lines:
            temp = item.split('|')
            name = temp[0]
            last_name = temp[1]
            id = temp[2]
            fees = temp[3]
            movies = temp[4]
            movies = movies.split('&')
            dict = {}
            for i in movies:
                if len(i) == 0:
                    continue
                tmp = i.split(':')
                movie_list = tmp[0].split(';')
                date_list = tmp[1].split('.')
                temp_movie = Movie([movie_list[0], movie_list[1], movie_list[2], movie_list[3], movie_list[4]])
                temp_date = datetime.date( int(date_list[2]), int(date_list[1]), int(date_list[0]) )
                dict[temp_movie] = temp_date
            self.members.append(Member([name, last_name, id, fees, dict]))

    def update_file(self):
        open(self.file_name, "w").close()
        with open(self.file_name, 'w') as f:
            for item in self.file_lines:
                f.write(item + '\n')
        f.close()

    def find_by_id(self, id):
        lo = 0
        hi = len(self.members) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if self.members[mid].id < str(id):
                lo = mid + 1
            else:
                hi = mid
        return self.members[lo].id == id

    def find_bigger_id(self, id):
        lo = 0
        hi = len(self.members) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if self.members[mid].id < str(id):
                lo = mid + 1
            else:
                hi = mid
        return lo

    def add_to_index(self, index, member):
        self.file_lines.insert(index, member.convert())
        self.members.insert(index, member)
        self.update_file()

    def delete_index(self, index):
        del self.file_lines[index]
        del self.members[index]
        self.update_file()

test = Database_member("members.txt")
#test.delete_index(2)
#curr_date = datetime.datetime.now()
#mov1 = Movie(["The Matrix", 1992, 122, 2, 3])
#list = { mov1 : curr_date }
#tmp = Member(['Ivan', 'Milinovic', '321321321', 0, list])
#print(tmp.convert())
#print(tmp)
