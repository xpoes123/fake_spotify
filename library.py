import os
class Library:
    SONG_PATH = "./songs/"
    def __init__(self):
        self.songs = []
        self.setup()

    def print_library(self):
        index = 0
        for song_name in self.songs:
            if song_name[0] != '.':
                print((str(index + 1) + " " + song_name[0:song_name.index(".")]).replace("_", " "))
                index += 1

    def reindex(self):
        for song_name in self.songs:
            if song_name[0] == '.':
                self.songs.remove(song_name)

    def setup(self):
        self.songs = os.listdir(self.SONG_PATH)
        self.reindex()

    