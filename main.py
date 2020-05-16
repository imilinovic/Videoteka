from movie import Movie
from member import Member
from database_mov import Database_movie
from database_mem import Database_member
from tkinter import *
from random import randint
import datetime

def random_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


class Videoteka:
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('400x200')
        self.movies = Database_movie("movies.txt")
        self.members = Database_member("members.txt")

    def create_id(self):
        id = random_with_n_digits(9)
        while self.members.find_by_id(id):
            id = random_with_n_digits(9)
        return id

    def create_account(self, window, entries):
        for entry in entries:
            if not entry.get():
                fail = Label(window, text="Niste upisali sve podatke", font="Calibri 15")
                fail.place(relx=0.5, rely=0.8, anchor=CENTER)
                return

        member_info = [ entries[0].get(), entries[1].get(), self.create_id(), 0, {} ]
        new_member = Member(member_info)
        self.members.add_to_index( self.members.find_bigger_id(new_member.id), new_member )
        show_id = Button(window, text="Vaš id je " + str(new_member.id), font="Calibri 20", command = lambda:window.destroy())
        show_id.pack()

    def register(self):
        window = Toplevel(self.root)
        window.geometry('400x300')

        text = ["Ime:", "Prezime:"]
        entries = []
        for txt in text:
            tmp1 = Label( window, text=txt, font="Calibri 20" )
            tmp2 = Entry( window, text=txt, font="Calibri 20")
            tmp1.pack()
            tmp2.pack()
            entries.append(tmp2)

        done = Button( window, text="Napravi ID", font="Calibri 20", command = lambda : self.create_account(window, entries))
        done.pack()

    def get_movie(self, window, options, movie, id_pos):
        options.destroy()
        new_window = Toplevel(window)
        new_window.geometry('700x700')
        txt = self.members.members[id_pos].add_movie(movie, datetime.datetime.now())
        if "vratite" not in txt:
            temp_member = self.members.members[id_pos]
            self.members.delete_index(id_pos)
            self.members.add_to_index(id_pos, temp_member)

        new_button = Button(new_window, height = 700, width = 700, text=txt, font="Calibri 13",
                            command = lambda:new_window.destroy())
        new_button.pack()


    def get_movies(self, window, options, entry, id_pos):
        movie_name = entry.get()
        movies = self.movies.get_movies(movie_name)

        cnt = 0
        for movie in movies:
            button = Button(options, text=movie.name, font="Calibri 20", command=lambda window = window, options = options, movie = movie, id_pos = id_pos :self.get_movie(window, options, movie, id_pos))
            button.place(relx=0.5, rely=0.4 + cnt * 0.15, anchor=CENTER)
            cnt += 1

    def borrow_movie(self, window, id, id_pos):
        options = Toplevel(window)
        options.geometry('400x400')
        label = Label(options, text="Unesite ime filma", font="Calibri 20")
        label.pack()
        entry = Entry(options, font="Calibri 20")
        entry.pack()
        search = Button(options, text="Pretrazi", font="Calibri 20", command=lambda:self.get_movies(window, options, entry, id_pos))
        search.pack()

    def return_movie(self, window, options, movie, id_pos):
        self.members.members[id_pos].remove_movie(movie)
        temp_member = self.members.members[id_pos]
        self.members.delete_index(id_pos)
        self.members.add_to_index(id_pos, temp_member)
        options.destroy()

        money = Toplevel(window)
        money.geometry('400x400')
        txt = "Vaša zakasnina iznosi {} kn".format(self.members.members[id_pos].fees)
        button = Button(money, text=txt, font="Calibri 20", height=400, width=400, command=lambda:money.destroy())
        button.pack()

    def return_movies(self, window, id, id_pos):
        options = Toplevel(window)
        options.geometry('400x400')
        label = Label(options, text="Koji film želite vratiti?", font="Calibri 20")
        label.pack()

        movies = self.members.members[id_pos].movies
        for movie, date in movies.items():
            button = Button(options, text=movie.name, font="Calibri 20", command=lambda window=window, options=options,movie=movie, id_pos = id_pos : self.return_movie(window, options, movie, id_pos))
            button.pack()

    def create_id_movie(self):
        id = random_with_n_digits(9)
        while self.movies.exists(id):
            id = random_with_n_digits(9)
        return id

    def add_movie(self, window, entries, new_window):
        for entry in entries:
            if not entry.get():
                return None

        data = []
        for entry in entries:
            data.append(entry.get())
        data.append(self.create_id_movie())
        data.append("admin")
        new_movie = Movie(data)
        pos = self.movies.get_movies(new_movie.name, True)
        self.movies.add_to_index(pos, new_movie)
        new_window.geometry('600x600')
        done = Button(new_window, text="Uspjesno ste dodali film\n" + new_movie.__str__(), font="Calibri 13", height=600, width=600, command=lambda:new_window.destroy())
        done.place(relx=0.5, rely=0.5, anchor=CENTER)

    def add_movies(self, window):
        new_window = Toplevel(window)
        new_window.geometry('400x400')
        text = ["Ime:", "Godina izdavanja:", "Dužina u minutama:"]
        entries = []
        for txt in text:
            label = Label(new_window, text=txt, font="Calibri 20")
            label.pack()
            entry = Entry(new_window, font="Calibri 20")
            entry.pack()
            entries.append(entry)
        button = Button(new_window, text="Dodaj", font="Calibri 20", command=lambda:self.add_movie(window, entries, new_window))
        button.pack()

    def zakasnina(self, window, id, id_pos):
        new_window = Toplevel(window)
        new_window.geometry('400x400')
        button = Button(new_window, text="Vaša zakasnina iznosi\n" + str(self.members.members[id_pos].fees) + "kn", font="Calibri 18",
                        command=lambda:new_window.destroy(), width=400, height=400)
        button.pack()

    def login(self, entry):
        id = entry.get()
        if not self.members.find_by_id(id):
            window = Toplevel(self.root)
            window.geometry('200x200')
            button = Button(window, text="Nepostojeci ID", font="Calibri 20", height=200, width=200, command = lambda:window.destroy())
            button.pack()
            return None

        id_pos = self.members.find_bigger_id(id)
        #print(id_pos)
        window = Toplevel(self.root)
        window.geometry('300x400')

        button1 = Button(window, text="Posudi film", font="Calibri 20", command=lambda:self.borrow_movie(window, id, id_pos))
        button1.pack()
        button2 = Button(window, text="Vrati film", font="Calibri 20", command=lambda:self.return_movies(window, id, id_pos))
        button2.pack()
        button3 = Button(window, text="Dodaj film", font="Calibri 20", command=lambda:self.add_movies(window))
        button3.pack()
        button4 = Button(window, text="Zakasnina", font="Calibri 20", command=lambda:self.zakasnina(window, id, id_pos))
        button4.pack()

    def display_login(self):
        welcome_message = Label( self.root, text="Dobrodošli u videoteku", font="Calibri 25")
        welcome_message.pack()

        entry_text = Label( self.root, text="Ovdje upišite svoj ID", font="Calibri 15")
        entry_text.pack()
        entry = Entry( self.root )
        entry.pack()
        login_id = Button( self.root, text="Login", font="Calibri 15",
                            command = lambda : self.login(entry))
        login_id.place(relx=0.5, rely=0.60, anchor=CENTER)
        register_id = Button( self.root, text="Nemam svoj ID", font="Calibri 15",
                              command = lambda : self.register() )
        register_id.place(relx=0.5, rely=0.85, anchor=CENTER)


main = Videoteka("Videoteka")
main.display_login()
main.root.mainloop()
