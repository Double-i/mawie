
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QGridLayout,QListWidget,QListWidgetItem
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtCore import QRect
from app.gui.components import GuiComponent
from app.models.Movie import Movie
from urllib import request

class ResearchListFrame(QWidget,GuiComponent):
    def __init__(self,parent=None,gui=None):
        super().__init__(parent)
        self.gui = gui
        self.gui.register_listener(self)
        self.initFrame()

    def initFrame(self):
        self.createWidgets()
        self.show()
    def createWidgets(self):
        grid = QGridLayout()

        self.listWidgets = QListWidget(self)
        self.listWidgets.setMinimumSize(670,700)
        self.updateWidgets(Movie.query())
        # for film in Movie.query():
        #     item = QListWidgetItem(self.listWidgets)
        #     itemW= ResultRow(self,film,self.gui)
        #     item.setSizeHint(itemW.sizeHint())
        #     self.listWidgets.setItemWidget(item, itemW)

        self.setLayout(grid)
    def updateWidgets(self,data):
        self.listWidgets.clear()
        for film in data:
            try:
                itemW= ResultRow(self.listWidgets,film,self.gui)
                self.listWidgets.addItem(itemW)
            except Exception as e:
                print(e)
    def handleAction(self,name,data):
        if name == "search-results":
            self.updateWidgets(data)
            print("*********************")
    def requestAction(self,name):
        pass

class ResultRow(QListWidgetItem,GuiComponent):
    def __init__(self,parent,data,gui):
        super().__init__(parent)
        self.gui = gui
        self.gui.register_listener(self)
        self.initRow(data)
        #self.setGeometry(QRect(0,0,700,160))
        #self.setMinimumSize(650,160)
        #self.setSizePolicy(650,160)

    def initRow(self,data):
        self.createWidgets(data)
        #self.show()

    def createWidgets(self,data):
        grid = QGridLayout()

        lblImg = QLabel(self)
        if data.poster is not None:
            poster = self.importPosterFilm(data.poster)
        else :
            poster = self.importPosterFilm()
        lblImg.setPixmap(poster)

        if data.name is not None:
            if data.release is not None:
                lblProducer = QLabel("Title: "+data.name, self)
            else:
                lblProducer = QLabel("Title: "+data.name, self)

        else:
            lblProducer = QLabel("Title: -", self)
        if data.actors is not None:
            lblActors = QLabel("Actor(s): "+data.actors,self)
        else:
            lblActors = QLabel("Actors(s): -",self)
        if data.directors is not None:
            lblRating = QLabel("IMDb Rating: "+data.rate,self)
        else:
            lblRating = QLabel("IMDb Rating: -", self)
        btnSee = QPushButton("See info",self)

        lblActors.setFixedWidth(400)
        lblProducer.setFixedWidth(400)
        lblRating.setFixedWidth(400)

        lblActors.setWordWrap(True)
        lblProducer.setWordWrap(True)
        lblRating.setWordWrap(True)

        lblImg.setFixedSize(100,160)
        lblImg.setScaledContents(True)  # fit image to label

        grid.addWidget(lblImg,0,0,3,2)


        grid.addWidget(lblImg,0,0,3,2)
        grid.addWidget(lblProducer,0,2)
        grid.addWidget(lblRating, 1, 2)
        grid.addWidget(lblActors, 2, 2)
        grid.addWidget(btnSee, 0, 3,3,2)

        btnSee.clicked.connect(lambda : self.test(data))

        self.setLayout(grid)
    def test(self,film):
        self.gui.dispatchAction("search_selected",film)


    def importPosterFilm(self,path=''):
        image = QImage()
        pixMap = QPixmap("noPoster.jpg")
        if path is "":
            return pixMap
        try:
            html = request.urlopen(path)
            data = html.read()
            flag = False
            image.loadFromData(data)
            pixMap = QPixmap(image)
        except request.URLError: #in case there isn't the internet or the url gives 404 error or bad url
            print("a problem with the connection or the url has occurred")
        return pixMap

    def handleAction(self, name, data):
        pass

    def requestAction(self, name):
        pass

