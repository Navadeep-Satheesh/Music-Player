import py_compile
from root import * 
import json

    

class Settings(widgets.QWidget):
    def createSettings(self):
        
        
        

        
        self.settings_scroll_area = widgets.QScrollArea()
        
        self.settings_scroll_area.setWidgetResizable(True)
        
        

        self.settings_widget = widgets.QWidget()
        self.settings_scroll_area.setWidget(self.settings_widget)


        
       
        self.settingslayout = widgets.QVBoxLayout(self.settings_widget)
        self.settingslayout.setAlignment(core.Qt.AlignTop)

        
        
        


        #add remove folders

        def addFolder():
            folder = str(widgets.QFileDialog.getExistingDirectory())
            folders.append(folder)
            pickle.dump(folders , open("files/folders.pickle","wb"))
            self.folder_list.addItem(folder)
            print(folder)
            self.loadMusic()
        def removeFolder():
            
            folder = self.folder_list.currentRow()
            print(folder)
            folders.pop(folder)
            pickle.dump(folders , open("files/folders.pickle","wb"))
            self.folder_list.takeItem(folder)
            self.loadMusic()


        self.folder_list = widgets.QListWidget()

        self.add = widgets.QPushButton(text = "+")
        self.add.clicked.connect(addFolder)

        self.remove = widgets.QPushButton(text = "-")
        self.remove.clicked.connect(removeFolder)

        self.folder_list.addItems(folders)

        self.folder_list.setMaximumHeight(100)

        self.add_remove_layout = widgets.QHBoxLayout()



        self.add_remove_layout.addWidget(self.add)
        self.add_remove_layout.addWidget(self.remove)

        self.settingslayout.addWidget(self.folder_list)
        self.settingslayout.addLayout(self.add_remove_layout)



        #=============

        self.settings_scroll_area.hide()

        

        


        


    


    
