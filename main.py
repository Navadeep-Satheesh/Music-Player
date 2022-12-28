

from root import *
from settings import *
from sidebar import *
from home import *

class main_window(Home,Settings,SideBar):
    def __init__(self):
           
        self.minheight = 600
        self.minwidth = 1200
        self.sliderlength = 1000
        super().__init__()
        self.setWindowTitle("music player")
        self.setMinimumSize(self.minwidth , self.minheight)
        self.setStyleSheet(stylesheets["window"])

        self.createHome()
        self.createSettings()
        self.createSideBar()
        
        self.master_layout = widgets.QGridLayout()
        
        self.master_layout.addWidget(self.player_widget, 0 , 1)
        self.master_layout.addWidget(self.settings_scroll_area, 0 , 1)
        self.master_layout.addLayout(self.sidebar, 0 ,0)
        self.setLayout(self.master_layout)


if __name__ == "__main__":

    app = widgets.QApplication([])
    window = main_window()
    
    app.exec_()

