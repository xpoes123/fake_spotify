import tkinter
import customtkinter
import videoDownloader
import main
import os
from pydub import AudioSegment
from pydub.playback import play
from pygame import mixer

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("dark-blue")

def refresh():
    a.destroy()
    os.popen("python3 GUI.py") 

class App(customtkinter.CTk):
    frames = {"frame1": None, "frame2": None}

    def frame1_selector(self):
        App.frames["frame2"].pack_forget()
        App.frames["frame1"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def frame2_selector(self):
        App.frames["frame1"].pack_forget()
        App.frames["frame2"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def quit(self):
        exit()

    def play(self, number, song_list):
        song_to_play = number
        print(song_to_play)
        mixer.init()
  
        # Loading the song
        print(song_list[int(song_to_play)])
        mixer.music.load(str("./songs/" + song_list[int(song_to_play)]))

        # Setting the volume
        mixer.music.set_volume(0.7)
        
        # Start playing the song
        mixer.music.play()

    def download(self, url, name):
        videoDownloader.download(url, name)
        refresh()

    def pause(self, val):
        if val == 0:
            mixer.music.pause()
        else:
            mixer.music.unpause()

    def __init__(self):
        super().__init__()
        # self.state('withdraw')
        self.title("Change Frames")

        self.geometry("{0}x{0}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        # contains everything
        main_container = customtkinter.CTkFrame(self)
        main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        left_side_panel = customtkinter.CTkFrame(main_container, width=150)
        left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=10, pady=10)

        # buttons to select the frames
        bt_frame1 = customtkinter.CTkButton(left_side_panel, text = "View Library", command = self.frame1_selector, fg_color = ["green", "green"], font = ("Roboto", 32), width = 300, height = 50)
        bt_frame1.grid(row=0, column=0, padx=20, pady=10)

        bt_frame2 = customtkinter.CTkButton(left_side_panel, text = "Download New Music", command = self.frame2_selector, fg_color = ["green", "green"], font = ("Roboto", 32), width = 300, height = 50)
        bt_frame2.grid(row=1, column=0, padx=20, pady=10)

        bt_frame3 = customtkinter.CTkButton(left_side_panel, text = "Quit", command = self.quit, fg_color = ["green", "green"], font = ("Roboto", 32), width = 300, height = 50)
        bt_frame3.grid(row=3, column=0, padx=20, pady=10)

        # right side panel -> to show the frame1 or frame 2
        self.right_side_panel = customtkinter.CTkFrame(main_container)
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        self.right_side_container = customtkinter.CTkFrame(self.right_side_panel,fg_color="#000811")
        self.right_side_container.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        App.frames['frame1'] = customtkinter.CTkFrame(main_container,fg_color="gray26")
        song_list = main.view_library()
        bts = []
        print(song_list)
        for i in range(len(song_list)):
            bts.append(customtkinter.CTkButton(App.frames['frame1'], text = str(str(i+1) + " " +  (song_list[i][0:song_list[i].index(".")]).replace("_", " ")), command = lambda a = i: self.play(a, song_list)))
        for i in range(len(bts)):
            bts[i].grid(pady = 12, padx = 10)
        pause_music = customtkinter.CTkButton(App.frames['frame1'], text="Pause Music", command= lambda: self.pause(0))
        pause_music.place(relx = 0.4, rely = 0.9,relwidth = 0.2, relheight = 0.05)

        unpause_music = customtkinter.CTkButton(App.frames['frame1'], text="Unpause Music", command= lambda: self.pause(1))
        unpause_music.place(relx = 0.6, rely = 0.9, relwidth = 0.2, relheight = 0.05)

        App.frames['frame2'] = customtkinter.CTkFrame(main_container,fg_color="gray26")
        URL_textbox = customtkinter.CTkEntry(App.frames['frame2'], placeholder_text = "Youtube URL")
        name_textbox = customtkinter.CTkEntry(App.frames['frame2'], placeholder_text = "Name of Song")
        submit_new_song = customtkinter.CTkButton(App.frames['frame2'], text="Submit New Song", command= lambda: self.download(URL_textbox.get(), name_textbox.get()))
        submit_new_song.place(relx = 0.3, rely = 0.4, relwidth = 0.4)
        URL_textbox.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER, relwidth = 0.4)
        name_textbox.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER, relwidth = 0.4)

a = App()
a.mainloop()