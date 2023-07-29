import library
import videoDownloader
from pydub import AudioSegment
from pydub.playback import play

SONG_PATH = "./songs/"

def main(): 
    print("Welcome to fake spotify")
    while(True):
        action = input("Type 1 to view your library, 2 to download a new song, 3 to play a song, 4 to exit")
        if action == "1":
            view_library()
        elif action == "2":
            download()
        elif action == "3":
            play_song()
        elif action == "4":
            exit()


def play_song():
    play_library = view_library()
    song_to_play = input("Which song do you want to play? (Number)")
    audio = AudioSegment.from_wav(str(SONG_PATH + play_library[int(song_to_play)-1]))
    play(audio)

def download():
    videoDownloader.download()

def view_library():
    library2 = library.Library()
    library2.print_library()
    return library2.songs

if __name__ == "__main__":
    main()

