from PySide2 import QtWidgets
from movie import Movie

class App(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cine Club")  
        self.setup_ui()
        self.show_movie()
        self.setup_connection()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.LineEdit = QtWidgets.QLineEdit()
        self.btn_add = QtWidgets.QPushButton("Add a movie")
        self.btn_remove = QtWidgets.QPushButton("Remove a movie")
        self.list_movie = QtWidgets.QListWidget()
        self.list_movie.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_remove = QtWidgets.QPushButton("Remove a movie")


        self.layout.addWidget(self.LineEdit)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.list_movie)
        self.layout.addWidget(self.btn_remove)

    def show_movie(self):
        movies = Movie.get_movies()
        for movie in movies:
            self.list_movie.addItem(movie.title)

    def setup_connection(self):
        self.btn_add.clicked.connect(self.add_movie)
        self.btn_remove.clicked.connect(self.remove_movie)
        self.LineEdit.returnPressed.connect(self.add_movie)
    
    def add_movie(self):
        title = self.LineEdit.text()
        Movie(title).add_to_movies()
        self.list_movie.addItem(title)    
        self.LineEdit.clear()
        print("Adding a movie") 
    
    def remove_movie(self):
        list = Movie._get_movies()
        for i, item in enumerate(self.list_movie.selectedItems()):
            for index, j in enumerate(list):
                if item.text() == j:
                    print(item.text())
                    self.list_movie.takeItem(index)
                    Movie.remove_from_movies(item.text())
                    print("Deleting movie(s)")

app = QtWidgets.QApplication([])

win = App()
win.show()

app.exec_()