# <<<<<<< HEAD
# =======
# <<<<<<< develop
# import tkinter
#
# from app.gui.components import GuiComponent
#
#
#
# class MovieListFrame(tkinter.Frame, GuiComponent):
#     def __init__(self, parent, gui, *arg, **kwargs):
#         self.parent= parent
#         self.gui =gui
#         gui.register_listener(self)
#         super(MovieListFrame, self).__init__(parent)
#         self.createWidget()
#         self.grid()
#
#
#     def createWidget(self):
#         self.lblTitle= tkinter.Label(self, text="test")
#         self.lstFilm = tkinter.Listbox(self,width=100)
#         self.btnChange = tkinter.Button(self,text="Ouvrir",command=self.showMovieInfo)
#
#         self.lblTitle.grid()
#         self.lstFilm.grid()
#         self.btnChange.grid()
#
#     def updateWidget(self,data):
#         self.lstFilm.delete(0,tkinter.END)
#         self.lstObjFilm = []
#         for i in data:
#             self.lstFilm.insert(tkinter.END, i)
#             self.lstObjFilm.append(i)
#
#     def handleAction(self, name, data):
#         if name == 'list_result_search':
#             self.updateWidget(data)
#
#     def showMovieInfo(self):
#         idxFilmList = self.lstFilm.curselection() #idxFilmList  is the position of the film in the list of movies
#         film = self.lstObjFilm[int(idxFilmList[0])] # film is the object movie of the film selected
#         self.gui.dispatchAction("search_selected",film)
#
#
#     def requestAction(self, name):
#         pass
#
#
# =======
# >>>>>>> develop
# import tkinter
#
# from app.gui.components import GuiComponent
#
#
#
# class MovieListFrame(tkinter.Frame, GuiComponent):
#     def __init__(self, parent, gui, *arg, **kwargs):
#         self.parent= parent
#         self.gui =gui
#         gui.register_listener(self)
#         super(MovieListFrame, self).__init__(parent)
#         self.createWidget()
#         self.grid()
#
#
#     def createWidget(self):
#         self.lblTitle= tkinter.Label(self, text="test")
#         self.lstFilm = tkinter.Listbox(self,width=100)
#         self.btnChange = tkinter.Button(self,text="Ouvrir",command=self.showMovieInfo)
#
#         self.lblTitle.grid()
#         self.lstFilm.grid()
#         self.btnChange.grid()
#
#     def updateWidget(self,data):
#         self.lstFilm.delete(0,tkinter.END)
#         self.lstObjFilm = []
#         for i in data:
#             self.lstFilm.insert(tkinter.END, i)
#             self.lstObjFilm.append(i)
#
#     def handleAction(self, name, data):
#         if name == 'list_result_search':
#             self.updateWidget(data)
#
#     def showMovieInfo(self):
#         idxFilmList = self.lstFilm.curselection() #idxFilmList  is the position of the film in the list of movies
#         film = self.lstObjFilm[int(idxFilmList[0])] # film is the object movie of the film selected
#         self.gui.dispatchAction("search_selected",film)
#
#
#     def requestAction(self, name):
#         pass
#
#
# <<<<<<< HEAD
# =======
# >>>>>>> movie_frame -Change label value from french to english (réalisateur->director) -Display "-" if the movie attribut value is null MainFrame -change the name of the list of frame which was a bidon name Gui.py -comment lines which was used to debug
# >>>>>>> develop
