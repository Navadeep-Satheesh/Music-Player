
from root import *

class SideBar(widgets.QWidget):

    def createSideBar(self):
        self.sidebar = widgets.QVBoxLayout()


        button_style_sheet = stylesheets["button"] +"min-height : 40%; margin : 10% ; max-width: 150%"
        self.home = widgets.QPushButton(text = "all songs")
        self.home.clicked.connect(self.show_home)
        self.home.setStyleSheet(button_style_sheet)

        self.favourites = widgets.QPushButton(text = "favorites")
        self.favourites.clicked.connect(self.show_playlist)
        self.favourites.setStyleSheet(button_style_sheet)
        

        self.playlist_scroll = widgets.QScrollArea()
        
        self.playlist_widget = widgets.QWidget()
        self.playlist_widget.setStyleSheet("background-color: rgb(13, 13 ,13);")

        self.playlist_scroll.setWidget(self.playlist_widget)
        self.playlist_scroll.setWidgetResizable(True)
        self.playlist = widgets.QVBoxLayout(self.playlist_widget)
        self.playlist.setAlignment(core.Qt.AlignTop)
      

        self.playlist_scroll.setStyleSheet(stylesheets["scroll"]+"max-width: 200%; ")
     
        for i in range(1, len(playlists)):
            self.single_playlist_item(list(playlists.keys())[i] , i )
            
            
        #=========================

        self.addPlaylistButton = widgets.QPushButton(text = "create")
        self.addPlaylistButton.clicked.connect(self.addPlaylist)
        self.addPlaylistButton.setStyleSheet(r" background-color : rgb(15,15,15);")


        self.settings = widgets.QPushButton()
        self.settings.setIcon(gui.QIcon(paths["settings"]))
        self.settings.clicked.connect(self.show_settings)
        self.settings.setStyleSheet("border:transparent;")


        self.sidebar.addWidget(self.home)
        self.sidebar.addWidget(self.favourites)
        self.sidebar.addWidget(self.playlist_scroll)      
        self.sidebar.addWidget(self.addPlaylistButton)
        self.sidebar.addWidget(self.settings)
              
        
        self.show()
    def single_playlist_item(self, item, index):
            container_widget = widgets.QWidget()
            container = widgets.QHBoxLayout(container_widget)
            container_widget.setStyleSheet(r"min-height: 40%; margin: 20% 0%")
            

            playlist = widgets.QPushButton(text = item )
         
            playlist.setStyleSheet(stylesheets["button"] + "min-width: 60% ;")
           
            options =  widgets.QPushButton(text = "")
            options.setStyleSheet(" width : 30%;")
            
            optionsMenu = widgets.QMenu()
          
            #==================options==========

            delete = optionsMenu.addAction("delete")
            delete.playlist = item
            delete.triggered.connect(lambda: self.respond_to_playlist_menu(0))

            rename = optionsMenu.addAction("rename")
            rename.playlist = item
            rename.triggered.connect(lambda: self.respond_to_playlist_menu(1))

            options.setMenu(optionsMenu)

            playlist.clicked.connect(self.show_playlist)
            

            container.addWidget(playlist)
            container.addWidget(options)

            self.playlist.addWidget( container_widget , alignment= core.Qt.AlignTop)

    def respond_to_playlist_menu(self , code):
        global playlists
        action = self.sender()
        print(list(playlists.keys()))
        if code == 0:
            playlist = action.playlist 
            print(playlist)
            widget = self.playlist.itemAt(list(playlists.keys()).index(playlist)+1).widget()
            widget.setParent(None)
            playlists.pop(playlist)
            pickle.dump(playlists,open("files\\playlists.pickle","wb"))
            self.show_home()

        elif code == 1:
            playlist = action.playlist
            dialog = widgets.QInputDialog()
            new_name , got = dialog.getText(self , "rename" , "enter the new name")
            if got:        
               
                widget = self.playlist.itemAt(list(playlists.keys()).index(playlist)+1).widget()
                button = widget.layout().itemAt(0).widget()
              
                button.setText(new_name)
                playlists[new_name] = playlists[playlist]
                
                del playlists[playlist]
                pickle.dump(playlists,open("files\\playlists.pickle","wb"))
    def show_home(self):
        self.closeSearch()
        # self.
        # self.searchBar.hide()
        # self.searchButton.hide()
        self.player_widget.show()
        self.settings_scroll_area.hide()
        self.music_list_scroll.show()
        self.playlist_songs_scroll.hide()      

    def show_settings(self):      
        self.player_widget.hide()
        self.settings_scroll_area.show()       
    def show_playlist(self):
        print(playlists)
        index = 1
        # self.closeSearch()
        # self.searchBar.hide()
        # self.searchButton.hide()
        self.settings_scroll_area.hide()
        self.music_list_scroll.hide()
        self.playlist_songs_scroll.show()


        playlist_name = self.sender().text()

        
        playlist = playlists[self.sender().text()]
        print("the playlist is" , playlist)
        self.musics.clear()

        for i in range(self.playlist_songs.count()):
            
            item = self.playlist_songs.itemAt(i).widget()
         
            song_name = item.layout().itemAt(1).widget().text()
            
            if song_name in playlist:
                
                self.musics.append(song_name)
                item.layout().itemAt(0).widget().setText(str(index))
                index+=1
                item.show()
            else:
                item.hide()

        print(self.playlist)
        
        self.currentPlaylist = playlist_name
        

    def addPlaylist(self):
        dialog = widgets.QInputDialog()
        name , done = dialog.getText(self,"create playlist", "enter name of playlist")
        if done:
            playlists[name]=[]
            pickle.dump(playlists, open("files\\playlists.pickle","wb"))
            self.single_playlist_item(name, self.playlist.count())