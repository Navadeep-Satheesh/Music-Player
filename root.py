

import PyQt5.QtWidgets as widgets 
import PyQt5.QtCore as core
import PyQt5.QtGui as gui
import pickle
import random 

import pygame.mixer as mixer
import os
from mutagen.mp3 import MP3
from mutagen.wave import WAVE



mixer.init()


music_types = [".mp3",".wav"]

music_mapping = {}

musics = []
shuffled_music = []

current_music = ""
current_music_index = 0
current_music_duration = 0
current_position = 0
divisions = 0


playing = False


musics_original = []

repeat = 0 
shuffle = False



mainFont = "Sans Serif"
mainFontSize = 10

playButtonSize =  core.QSize(80 , 80) 
controlButtonSize =  core.QSize(50 , 50) 
controlButtonSize2 = core.QSize(30 , 30)  



stylesheets = {
    "buttons":"height:100px ; max-width : 100px; border: transparent;",
    "window":"background-color: rgb(10, 10 , 10); color:white;",
    "button":"background-color : rgb(20 , 20 , 20); ",
    "scroll":"border: transparent;"
}

paths = {
    "settings":"res\\icons\\settings.svg",
    "play":"res\\icons\\play2.svg",
    "pause":"res\\icons\\pause2.svg",
    "next":"res\\icons\\next3.svg",
    "previous":"res\\icons\\previous3.svg",
    "shuffle-on":"res\\icons\\shuffle-on.svg",
    "shuffle-off":"res\\icons\\shuffle-off.svg",
    "repeat-0":"res\\icons\\repeat-0.svg",
    "repeat-1":"res\\icons\\repeat-1.svg",
    "repeat-infinite":"res\\icons\\repeat-infinite.svg",

}


if "playlists.pickle" in os.listdir("files"):
    playlists = pickle.load(open("files/playlists.pickle","rb"))
else:
    pickle.dump({"favorites":[]} , open("files/playlists.pickle",  "wb"))
    playlists = pickle.load(open("files/playlists.pickle","rb"))


if "folders.pickle" in os.listdir("files"):
    folders = pickle.load(open("files/folders.pickle","rb"))
else:
    pickle.dump([],open("files/folders.pickle","wb"))
    folders = pickle.load(open("files/folders.pickle","rb"))
    


