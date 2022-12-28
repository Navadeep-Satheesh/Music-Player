
from random import randrange
import pygame
from root import *

class Home(widgets.QWidget):
     
        def createHome(self):
            
            #layouts
            
            self.currentPlaylist = "all songs"

            self.player_widget =  widgets.QWidget()

            self.player_layout = widgets.QVBoxLayout(self.player_widget)
            self.length_layout = widgets.QHBoxLayout()

            self.controls = widgets.QHBoxLayout()
            self.controls.setAlignment(core.Qt.AlignCenter)
            self.controls2 = widgets.QHBoxLayout()
       

            #widgets
            self.timer = core.QTimer()
            self.timer.timeout.connect(self.updatetiming)
            
            #creating music list 
           
            self.music_list_scroll  = widgets.QScrollArea()
            self.music_list_scroll.setStyleSheet("border : transparent;")
            self.music_list_scroll.setWidgetResizable(True)
            self.music_widget = widgets.QWidget()
            self.music_list_scroll.setWidget(self.music_widget)
            self.music_list = widgets.QVBoxLayout(self.music_widget)
            self.music_list.setAlignment(core.Qt.AlignTop)
            

            self.playlist_songs_scroll = widgets.QScrollArea()
            self.playlist_songs_scroll.setStyleSheet(stylesheets["scroll"])
            self.playlist_songs_scroll.setWidgetResizable(True)
            
            self.playlist_songs_widget = widgets.QWidget()
            self.playlist_songs_scroll.setWidget(self.playlist_songs_widget)
            self.playlist_songs = widgets.QVBoxLayout(self.playlist_songs_widget)
            self.playlist_songs.setAlignment(core.Qt.AlignTop)

            self.loadMusic()

            self.playlist_songs_scroll.hide()
            # self.music_list_scroll.hide()
   
            self.playButton = widgets.QPushButton()
            self.playButton.setIcon(gui.QIcon(paths["play"]))
            self.playButton.setIconSize( playButtonSize)
            self.playButton.clicked.connect(self.play_pause)
            self.playButton.setStyleSheet(stylesheets["buttons"])
            
            self.nextButton = widgets.QPushButton()
            self.nextButton.clicked.connect(lambda: self.changeMusic(0))
            self.nextButton.setIcon(gui.QIcon(paths["next"]))
            self.nextButton.setIconSize( controlButtonSize)
            self.nextButton.setStyleSheet(stylesheets["buttons"])

            self.backButton = widgets.QPushButton()
            self.backButton.clicked.connect(lambda: self.changeMusic(1))
            self.backButton.setIcon(gui.QIcon(paths["previous"]))
            self.backButton.setIconSize( controlButtonSize)
            self.backButton.setStyleSheet(stylesheets["buttons"])


            def toggle_shuffle():
                global shuffle
                global current_music
                if shuffle is True:
                    self.shuffle_button.setIcon(gui.QIcon(paths["shuffle-off"]))
                    shuffle=False
                    
                else:
                    self.shuffle_button.setIcon(gui.QIcon(paths["shuffle-on"]))
                    shuffle=True     
                    x = self.musics.copy()

                    
             
                    
                    if current_music == "":
                        start_music = random.choice(self.musics)
                    else:
                        start_music = current_music

                    print("the current music is", start_music)
                    x.remove( start_music)
                    self.musics_shuffled.append(start_music)
                    while x != []:
                        song = random.choice(x)
                        x.remove(song)
                        self.musics_shuffled.append(song)
                
                   

            def toggle_repeat():
                global repeat
                if repeat == 0:
                    repeat = 2
                    self.repeat_button.setIcon(gui.QIcon(paths["repeat-infinite"]))
                elif repeat ==2 :
                    repeat = 1
                    self.repeat_button.setIcon(gui.QIcon(paths["repeat-1"]))
                elif repeat ==1:
                    repeat = 0
                    self.repeat_button.setIcon(gui.QIcon(paths["repeat-0"]))
            def changeVolume():
                volume = self.volume_control.value()
                mixer.music.set_volume(volume/100)




            #==================search layout============
            self.searchWidget = widgets.QWidget()
           
            self.searchLayout = widgets.QHBoxLayout()
            self.searchWidget.setLayout(self.searchLayout)
            self.searchWidget.setStyleSheet("margin-right: 50%; padding: 5px;")
            self.searchLayout.setAlignment(core.Qt.AlignRight)

            self.searchBar = widgets.QLineEdit()
            self.searchBar.setStyleSheet("""
                                    max-width: 200%; 
                                    background-color: rgb(30, 30 , 30);
                                    padding: 5px;
                                    border: 1px rgb(15,15,15);
                                   
                                    """)
            self.searchBar.hide()
            self.searchBar.setFont(gui.QFont(mainFont , mainFontSize))           
            self.searchBar.setPlaceholderText("search")
            

            self.searchButton = widgets.QPushButton()
            self.searchButton.setIcon(gui.QIcon("res\\icons\\search.svg"))
            self.searchButton.clicked.connect(self.search)
            self.searchButton.setStyleSheet("max-width: 50%;;")

            self.closeButton = widgets.QPushButton("x")
            self.closeButton.setStyleSheet("background-color: rbg(10,10,10); border: transparent;max-width:20%;")
            self.closeButton.clicked.connect(self.closeSearch)
            self.closeButton.hide()
            
            self.searchLayout.addWidget(self.searchButton)
            self.searchLayout.addWidget(self.searchBar)
            self.searchLayout.addWidget(self.closeButton)
            

            #=========================================================


            self.shuffle_button = widgets.QPushButton()
            self.shuffle_button.setIcon(gui.QIcon(paths["shuffle-off"]))
            self.shuffle_button.clicked.connect(toggle_shuffle )
            self.shuffle_button.setStyleSheet(stylesheets["buttons"])
            self.shuffle_button.setIconSize(controlButtonSize2)

            self.repeat_button = widgets.QPushButton()
            self.repeat_button.clicked.connect(toggle_repeat)
            self.repeat_button.setIcon(gui.QIcon(paths["repeat-0"]))
            self.shuffle_button.setStyleSheet(stylesheets["buttons"])
            self.repeat_button.setIconSize(controlButtonSize2)
            
            mixer.music.set_volume(1)
            self.volume_control = widgets.QSlider()
            self.volume_control.setOrientation(core.Qt.Horizontal)
            self.volume_control.setRange(0,100)
            self.volume_control.valueChanged.connect(changeVolume)
            self.volume_control.setStyleSheet("max-width: 100px; max-height: 10px; ")
            self.volume_control.setValue(100)
            
            
            self.titlelabel = widgets.QLabel(text = "")
            self.titlelabel.setStyleSheet(r"padding: 10% 20%")
            self.titlelabel.setFont(gui.QFont(mainFont , 10))


            self.currentTimeLabel = widgets.QLabel(text = "00")
            
            self.actualTimeLabel = widgets.QLabel(text = "00")

            self.timingbar = widgets.QSlider()
            self.timingbar.setOrientation(core.Qt.Horizontal)
            self.timingbar.valueChanged.connect(self.setsongpos)
            
            
            self.timingbar.setPageStep(1)      
        
            self.controls.addWidget(self.shuffle_button)  
            self.controls.addWidget(self.backButton)
            self.controls.addWidget(self.playButton)
            self.controls.addWidget(self.nextButton)  
            self.controls.addWidget(self.repeat_button)  
            


            #addig items to length layout
            
            self.length_layout.addWidget(self.currentTimeLabel)
            self.length_layout.addWidget(self.timingbar)
            self.length_layout.addWidget(self.actualTimeLabel)

            #adding itemsm to player playout
            self.searchresultsscroll =  widgets.QScrollArea()
            self.searchresultsscroll.setWidgetResizable(True)
            self.searchresultsscroll.setStyleSheet(stylesheets["scroll"])
            self.searchresultswidget = widgets.QWidget()

            self.searchresultsscroll.setWidget(self.searchresultswidget)
            self.searchresults  = widgets.QVBoxLayout(self.searchresultswidget)

            self.player_layout.addWidget(self.searchWidget)
            self.player_layout.addWidget(self.music_list_scroll)
            self.player_layout.addWidget(self.playlist_songs_scroll)
            self.player_layout.addWidget(self.searchresultsscroll)
            self.player_layout.addWidget(self.titlelabel)
            self.player_layout.addLayout(self.length_layout)
            self.player_layout.addLayout(self.controls2)
            self.player_layout.addLayout(self.controls)
            self.player_layout.addWidget(self.volume_control)

            self.searchresultsscroll.hide()
            
        def playMusic(self,music):
            global current_music
            global current_music_duration
            global current_music_index
            global current_position
            global playing

            current_music = music

            current_position = 0

            self.timingbar.setValue(0)
            

            song = mixer.music.load(music_mapping[current_music])   
            current_music_duration  = self.currentMusicDuration()
            self.titlelabel.setText(music)
            length = current_music_duration
            minutes = length//60
            if len(str(minutes))<2:
                minutes = "0"+str(minutes)
            seconds = length%60 
            if len(str(seconds))<2:
                seconds = "0"+str(minutes)

            self.actualTimeLabel.setText(f"{minutes}:{seconds}")


            playing = True
            self.timer.start(1000)
            mixer.music.play() 
            
            self.playButton.setIcon(gui.QIcon(paths["pause"]))

        def loadMusic(self):
           
            global music_mapping
         
            index = 0       
            self.musics = []
            self.musics_shuffled = []
            folders  = pickle.load(open("files/folders.pickle","rb"))
            for folder in folders:
                for music in os.listdir(folder):
                    if any(item in music for item in music_types):
                        full_music_path = folder + "/"+ music
                        self.musics.append(music)
                        music_mapping[music] = full_music_path
                        
                        self.create_single_item(music, index , self.music_list)
                        self.create_single_item(music , index , self.playlist_songs , Type = "playlist")
                        index+=1
            self.musics = self.musics
            self.musics_original = self.musics.copy()

        def search(self):
            if not  self.searchBar.isVisible() :
                self.closeButton.show()
                self.searchBar.show()
            elif self.searchBar.text() == "":
                print("here")
                self.searchBar.hide()
                self.closeButton.hide()
                self.searchresultswidget.hide()
                self.music_list_scroll.show()
            else:
                item = self.searchBar.text().lower()
                itemWords = item.split(" ")
                songs_with_similarity = []
                similarities = []
                index = 0
                for music in self.musics:
                    musicWords  =  music.lower().split(" ")
                    similarity = 0
                    for word in musicWords:
                        if word in itemWords:
                            similarity+=1
                    
                    if similarity>0:
                        songs_with_similarity.append(index)
                        similarities.append(similarity)
                        print(music , similarity)
                    index+=1
                self.music_list_scroll.hide()
                self.searchresultsscroll.show()
                for i in range(self.searchresults.count()):
                    self.searchresults.itemAt(i).layout().deleteLater()
                print(similarities)
                print(songs_with_similarity)
                while songs_with_similarity != []:
                    max_sim = max(similarities)
                    index1 = similarities.index(max_sim)
                    index2 = songs_with_similarity[index1]
                    print(index)
                    item = self.music_list.itemAt(index2).widget()
                    self.searchresults.addWidget(item)

                    similarities.pop(index1)
                    songs_with_similarity.pop(index1)
                print("done")
                self.music_list_scroll.hide()
                self.searchresultsscroll.show()
            
        def closeSearch(self):
            if self.searchBar.text() == "":
                self.searchBar.hide()
                self.closeButton.hide()
            self.searchresultsscroll.hide()
            self.music_list_scroll.show()
            self.searchBar.setText("")
            
        def create_single_item(self ,  music, index , layout , Type  =""):
            global music_mapping
            single_music_widget = widgets.QWidget()
            single_music_widget.setStyleSheet("padding :10px")
            

            single_music_item = widgets.QGridLayout(single_music_widget)

            index_label = widgets.QLabel(text = str(index+1))
            index_label.setStyleSheet("max-width:30%; padding-left: 20%;")

              
            title = widgets.QPushButton(text = music)
            title.setStyleSheet(stylesheets["button"])
            title.clicked.connect(self.setCurrentSong)
                
            self.music_menu =  widgets.QMenu()

            addToPlaylist = self.music_menu.addMenu("add to playlist")
            
            
            if Type == "playlist":
                remove = self.music_menu.addAction("remove from playlist")
                remove.triggered.connect(lambda: self.respond_to_menu(3))
                remove.id = index
                
            else :
                i = 0
                for item in playlists:
                    # print(item)
                    x = addToPlaylist.addAction(item)
                    x.triggered.connect(lambda: self.respond_to_menu(0))
                    x.id = index
                    i+=1  
                addToPlaylist.code = 0
            


            addToQueue = self.music_menu.addAction("add to queue")
            addToQueue.triggered.connect(lambda: self.respond_to_menu(2))
            addToQueue.id = index
            addToQueue.code = 1

            
            rename = self.music_menu.addAction("rename")
            rename.triggered.connect(lambda: self.respond_to_menu(2))
            rename.id = index
              

            options = widgets.QPushButton(text = "...")
            options.setStyleSheet("max-width: 50%;")      
            options.setMenu(self.music_menu)

            single_music_item.addWidget(index_label,0,0)
            single_music_item.addWidget(title,0,1)
            single_music_item.addWidget(options,0,2)
            
       
            layout.addWidget(single_music_widget , alignment=core.Qt.AlignTop)
         
        def respond_to_menu(self, code ):
            global currentPlaylist
            action =  self.sender()         

            if code == 0:
                playlist = action.text()
                print(self.musics_original)
                print(action.id )
                song = self.musics_original[action.id]
                if song   not in playlists[playlist]:
                    playlists[playlist].append(song)
                    pickle.dump(playlists, open("files\\playlists.pickle","wb"))

            elif code == 1:
                print(action.id)
                song = self.musics[action.id]
                self.musics.remove(song)
                self.musics.insert(0, song)
            elif code == 2:
                old_name = self.musics_original[action.id]
                dialog = widgets.QInputDialog()
                new_name , x = dialog.getText(self , "rename" , "enter new name")
                if x:
                    path = music_mapping[old_name]
                    path_split = path.split("/")
                    path_split.pop(-1)
                    path_split.append(new_name)
                    new_path = "/".join(path_split)

                    extension = path.split(".")[-1]

                    print(path ,new_path+"."+extension)
                    os.rename(path ,  new_path+"."+extension)
                    for playlist in playlists:
                        if old_name in playlists[playlist]:
                            playlists[playlist].remove(old_name)
                            playlists[playlist].append(new_name)
                
                required_layout = self.music_list.itemAt(action.id).widget().layout()
                required_button = required_layout.itemAt(1).widget()
                required_button.setText(new_name)
                # print(required_button)
            elif code == 3:
                
                playlists[self.currentPlaylist].remove(self.musics_original[action.id])
          
                self.playlist_songs.itemAt(action.id).widget().hide()
                pickle.dump(playlists , open("files//playlists.pickle", "wb"))
                print(self.musics)
                for i in range( self.musics.index(self.musics_original[action.id]) , self.playlist_songs.coutn()):
                    print("hi")
     
        def setCurrentSong(self):
        
            global current_music
            global playing
            global current_music_duration
            
            music = self.sender().text()     
            self.playMusic(music)

        def play_pause(self):
            global playing 
            global current_music
            global current_music_duration
            
            if current_music == "":
                print("starting....")
                
                if shuffle:
                    
                    current_music =  self.musics_shuffled[0]
                else:
                    current_music =  self.musics[0]
                print("the current music is" , current_music)
                self.playMusic(current_music)

            elif playing is True:
                print("pausing")
                mixer.music.pause()
                
                self.playButton.setIcon(gui.QIcon(paths["play"]))
                playing = False
            elif playing is False:
                print("playing")
                mixer.music.unpause()
                self.playButton.setIcon(gui.QIcon(paths["pause"]))
                playing = True 

        def changeMusic(self, direction):
            global current_music
            global current_music_index
            global playing
            global current_music_duration
            global repeat

            if shuffle:
                current_music_list = self.musics_shuffled
            else:
                current_music_list = self.musics

            if repeat == 0:
                if direction == 0:
                    if current_music_index == len(current_music_list)-1:
                        current_music_index = 0
                    else:
                        current_music_index = current_music_index+1               

                elif direction ==1:
                    if current_music_index == 0:
                        current_music_index = len(current_music_list)-1
                    else:
                        current_music_index = current_music_index-1

                current_music = current_music_list[current_music_index]
                
            elif repeat == 1:
                repeat = 0

            self.playMusic(current_music)
        
        def updatetiming(self):

            global current_position
            # current_time = mixer.music.get_pos()
            # print("got time is ", current_time)
            if playing:
        
        
                current_position = current_position+1

                if current_position == current_music_duration:
                    
                    self.changeMusic(0)
                                
                else:
                    # print(length , end = " ")
                    self.timingbar.setValue(current_position)
                    # print(self.timingbar.value())
                    minutes = current_position//60
                    if len(str(minutes))<2:
                        minutes  = "0" + str(minutes)
                    seconds = current_position%60
                    if len(str(seconds)) <2:
                        seconds  = "0" + str(seconds)

                    self.currentTimeLabel.setText(f"{minutes}:{seconds}")
        
        def currentMusicDuration(self):
            music  = current_music
            if ".mp3" in current_music:
                audio = MP3(music_mapping[current_music])
            elif ".wav" in current_music:
                audio  =  WAVE(music_mapping[current_music])
            length = int(audio.info.length)
            print("the song is", length,"s")
            self.timingbar.setRange(0, length)
            
            return length
        
        def setsongpos(self):
            global current_position

            value = self.timingbar.value()
            
            if value  != current_position:

                mixer.music.set_pos(int(current_position) )        
        
                current_position = value
       
       
       
