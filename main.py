import sys
import os
import sqlite3
import pathlib

from random import shuffle
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QLabel, QMessageBox
from PIL import Image

filename = '/Users/HP/Desktop/проект Яндекс Лицей/music.mp3'
space_x, space_y = 101, 101
final_field = ['1.png', '2.png', '3.png', '4.png',
               '5.png', '6.png', '7.png', '8.png',
               '9.png', '10.png', '11.png', '12.png',
               '13.png', '14.png', '15.png', '16.png']
active_picture = 'images/animals/dog.png'

class Menu(QMainWindow):

    def __init__(self):
        self.background_image = 'images/background_image_menu.jpg'
        self.SIZE = [800, 800]
        self.names_of_buttons = ['НОВАЯ ИГРА', 'ОБ ИГРЕ', 'ВЫХОД']
        self.list_of_buttons = {}
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 40, *self.SIZE)
        self.setFixedSize(*self.SIZE)
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setWindowTitle('PUZZLE MANIA')
        self.build_surface()

    def build_surface(self):
        self.picture = QPixmap(self.background_image)
        self.bg = QLabel(self)
        self.bg.move(0, 0)
        self.bg.resize(*self.SIZE)
        self.bg.setPixmap(self.picture)

        x_button, y_button = 280, 410
        for i in range(3):
            self.button_start = QPushButton(self.names_of_buttons[i], self)
            self.button_start.move(x_button, y_button)
            self.button_start.resize(230, 60)
            self.button_start.setStyleSheet('background-color: red; border-style: outset; border-width: '
                                        '2px;border-radius: 200px; border-color: beige; font: bold 14px; min-width: '
                                        '10em;padding: 6px; border-radius: 20px')

            self.button_start.clicked.connect(self.open_second_form)
            self.list_of_buttons[self.names_of_buttons[i]] = self.button_start
            y_button += 111

    def open_second_form(self):
        if self.sender().text() == self.names_of_buttons[0]:
            self.second_form = GameField()
            self.second_form.show()

        elif self.sender().text() == self.names_of_buttons[1]:
            self.second_form = AboutGame()
            self.second_form.show()

        elif self.sender().text() == self.names_of_buttons[2]:
            EXIT()

class GameField(Menu):

    def __init__(self):
        self.background_image2 = 'images/background_image_choice_menu.jpg'
        super().__init__()
        self.initUI()
        self.setWindowTitle('CATEGORY SELECTION')

    def build(self):
        self.picture = QPixmap(self.background_image2)
        self.bg = QLabel(self)
        self.bg.move(0, 0)
        self.bg.resize(*self.SIZE)
        self.bg.setPixmap(self.picture)

    def create_images(self):
        self.pushButton_1.setStyleSheet('background-image: url(images/second_city_icon.jpg)')
        self.pushButton_2.setStyleSheet('background-image: url(images/animal_icon.jpg)')
        self.pushButton_3.setStyleSheet('background-image: url(images/landscapes_icon.jpg)')
        self.pushButton_4.setStyleSheet('background-image: url(images/user.jpg)')
        self.pushButton_1.clicked.connect(self.open_second_form)
        self.pushButton_2.clicked.connect(self.open_second_form)
        self.pushButton_3.clicked.connect(self.open_second_form)
        self.pushButton_4.clicked.connect(self.open_second_form)

    def open_second_form(self):
        if self.sender() == self.pushButton_1:
            self.third_form = City()
        elif self.sender() == self.pushButton_2:
            self.third_form = Animals()
        elif self.sender() == self.pushButton_3:
            self.third_form = Landscapes()
        elif self.sender() == self.pushButton_3:
            self.third_form = Landscapes()
        elif self.sender() == self.pushButton_4:
            self.third_form = UserPictures()
        self.third_form.show()

    def initUI(self):
        self.build()
        self.setGeometry(820, 40, *self.SIZE)
        self.setFixedSize(*self.SIZE)
        uic.loadUi('choice_menu.ui', self)
        self.create_images()
        self.setWindowIcon(QIcon('images/icon.png'))

class UserPictures(QMainWindow):

    def __init__(self):

        self.background_image2 = 'images/background_image.jpg'
        self.SIZE = [800, 800]
        self.window = Window()
        super().__init__()
        self.initUI()
        self.setWindowTitle('MY PICTURES')

    def build(self):
        self.picture = QPixmap(self.background_image2)
        self.bg = QLabel(self)
        self.bg.move(0, 0)
        self.bg.resize(*self.SIZE)
        self.bg.setPixmap(self.picture)

    def initUI(self):
        self.build()
        uic.loadUi('user_choice_menu.ui', self)
        self.setFixedSize(*self.SIZE)
        self.setGeometry(820, 40, *self.SIZE)
        self.setWindowIcon(QIcon('images/icon.png'))
        self.work_with_base()
        self.show_in_label()
        self.slovar_user_pictures = [self.pushButton_1, self.pushButton_2, self.pushButton_3,
                                     self.pushButton_4, self.pushButton_5, self.pushButton_6,
                                     self.pushButton_7, self.pushButton_8]
        self.names_of_files = ['background-image: url(images/user_pictures/icons/1.png)', 'background-image: url(images/user_pictures/icons/2.png)',
                               'background-image: url(images/user_pictures/icons/3.png)', 'background-image: url(images/user_pictures/icons/4.png)',
                               'background-image: url(images/user_pictures/icons/5.png)', 'background-image: url(images/user_pictures/icons/6.png)',
                               'background-image: url(images/user_pictures/icons/7.png)', 'background-image: url(images/user_pictures/icons/8.png)']
        self.nm_of_files = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png']
        self.pushButton.setStyleSheet('background-color: red; border-style: outset; border-width: '
                                        '2px;border-radius: 200px; border-color: beige; font: bold 14px; min-width: '
                                        '15em;padding: 6px; border-radius: 20px')
        self.pushButton.clicked.connect(self.download_new_picture)
        self.create_images()

    def show_in_label(self):
        con = sqlite3.connect('number_of_pictures.db')
        cur = con.cursor()
        result = cur.execute("""SELECT number FROM num""").fetchall()
        if int(result[0][0]) != 8:
            self.label.setText('Кол-во картинок - ' + str(result[0][0]))
        else:
            self.label.setText('Кол-во картинок - ' + str(result[0][0]) + 'Макс')
            self.pushButton.setEnabled(False)


    def work_with_base(self):
        con = sqlite3.connect('number_of_pictures.db')
        cur = con.cursor()
        name1 = pathlib.Path().absolute()
        name2 = pathlib.Path('/images/user_pictures')
        name3 = name1 / name2.relative_to(name2.anchor)
        col_files = next(os.walk(name3))[2]
        new_item = len(col_files)
        cur.execute('UPDATE num SET number =?', (str(new_item)))
        con.commit()
        self.show_in_label()


    def download_new_picture(self):
        name1 = pathlib.Path().absolute()
        name2 = pathlib.Path('/images/user_pictures')
        name3 = name1 / name2.relative_to(name2.anchor)
        col_files = next(os.walk(name3))[2]
        new_item = len(col_files)
        new_picture = QFileDialog.getOpenFileName(self, 'Выбор картинки', '')[0]
        im = Image.open(new_picture)
        resized_img = im.resize((600, 600), Image.ANTIALIAS)
        resized2_img = im.resize((375, 300), Image.ANTIALIAS)
        name1 = pathlib.Path().absolute()
        name2 = pathlib.Path('/images/user_pictures')
        name4 = pathlib.Path('/images/user_pictures/icons')
        name3 = name1 / name2.relative_to(name2.anchor)
        name5 = name1 / name4.relative_to(name4.anchor)
        gr = os.path.join(name3, self.nm_of_files[new_item])
        gr2 = os.path.join(name5, self.nm_of_files[new_item])
        resized_img.save(gr)
        resized2_img.save(gr2)
        self.work_with_base()
        self.create_images()

    def create_images(self):
        name1 = pathlib.Path().absolute()
        name2 = pathlib.Path('/images/user_pictures')
        name3 = name1 / name2.relative_to(name2.anchor)
        col_files = next(os.walk(name3))[2]
        new_item = len(col_files)
        for i in range(new_item):
            self.slovar_user_pictures[i].setStyleSheet(self.names_of_files[i])
            self.slovar_user_pictures[i].clicked.connect(self.open_user_form)

    def open_user_form(self):
        global active_picture
        if self.sender() == self.pushButton_1:
            active_picture = 'images/user_pictures/1.png'
        elif self.sender() == self.pushButton_2:
            active_picture = 'images/user_pictures/2.png'
        elif self.sender() == self.pushButton_3:
            active_picture = 'images/user_pictures/3.png'
        elif self.sender() == self.pushButton_4:
            active_picture = 'images/user_pictures/4.png'
        elif self.sender() == self.pushButton_5:
            active_picture = 'images/user_pictures/5.png'
        elif self.sender() == self.pushButton_6:
            active_picture = 'images/user_pictures/6.png'
        elif self.sender() == self.pushButton_7:
            active_picture = 'images/user_pictures/7.png'
        elif self.sender() == self.pushButton_8:
            active_picture = 'images/user_pictures/8.png'
        self.window.initUI()
        self.window.show()


class Landscapes(QMainWindow):

    def __init__(self):
        self.background_image2 = 'images/background_image.jpg'
        self.SIZE = [800, 800]
        self.window = Window()
        super().__init__()
        self.initUI()
        self.setWindowTitle('LANDSCAPES')

    def build(self):
        self.picture = QPixmap(self.background_image2)
        self.bg = QLabel(self)
        self.bg.move(0, 0)
        self.bg.resize(*self.SIZE)
        self.bg.setPixmap(self.picture)

    def open_landscapes_form(self):
        global active_picture
        if self.sender() == self.pushButton_1:
            active_picture = 'images/landscapes/1.jpg'
        elif self.sender() == self.pushButton_2:
            active_picture = 'images/landscapes/2.jpg'
        elif self.sender() == self.pushButton_3:
            active_picture = 'images/landscapes/3.jpg'
        elif self.sender() == self.pushButton_4:
            active_picture = 'images/landscapes/4.jpg'
        elif self.sender() == self.pushButton_5:
            active_picture = 'images/landscapes/5.jpg'
        elif self.sender() == self.pushButton_6:
            active_picture = 'images/landscapes/6.jpg'
        elif self.sender() == self.pushButton_7:
            active_picture = 'images/landscapes/7.jpg'
        elif self.sender() == self.pushButton_8:
            active_picture = 'images/landscapes/8.jpg'
        self.window.initUI()
        self.window.show()

    def initUI(self):
        self.build()
        uic.loadUi('categories_choice_menu.ui', self)
        self.setFixedSize(*self.SIZE)
        self.setGeometry(820, 40, *self.SIZE)
        self.setWindowIcon(QIcon('images/icon.png'))
        self.pushButton_1.setStyleSheet('background-image: url(images/landscapes/icons/1.jpg)')
        self.pushButton_2.setStyleSheet('background-image: url(images/landscapes/icons/2.jpg)')
        self.pushButton_3.setStyleSheet('background-image: url(images/landscapes/icons/3.jpg)')
        self.pushButton_4.setStyleSheet('background-image: url(images/landscapes/icons/4.jpg)')
        self.pushButton_5.setStyleSheet('background-image: url(images/landscapes/icons/5.jpg)')
        self.pushButton_6.setStyleSheet('background-image: url(images/landscapes/icons/6.jpg)')
        self.pushButton_7.setStyleSheet('background-image: url(images/landscapes/icons/7.jpg)')
        self.pushButton_8.setStyleSheet('background-image: url(images/landscapes/icons/8.jpg)')
        self.pushButton_1.clicked.connect(self.open_landscapes_form)
        self.pushButton_2.clicked.connect(self.open_landscapes_form)
        self.pushButton_3.clicked.connect(self.open_landscapes_form)
        self.pushButton_4.clicked.connect(self.open_landscapes_form)
        self.pushButton_5.clicked.connect(self.open_landscapes_form)
        self.pushButton_6.clicked.connect(self.open_landscapes_form)
        self.pushButton_7.clicked.connect(self.open_landscapes_form)
        self.pushButton_8.clicked.connect(self.open_landscapes_form)

class City(QMainWindow):

    def __init__(self):
        self.background_image2 = 'images/background_image.jpg'
        self.SIZE = [800, 800]
        self.window = Window()
        super().__init__()
        self.initUI()
        self.setWindowTitle('CITY')

    def build(self):
        self.picture = QPixmap(self.background_image2)
        self.bg = QLabel(self)
        self.bg.move(0, 0)
        self.bg.resize(*self.SIZE)
        self.bg.setPixmap(self.picture)

    def open_city_form(self):
        global active_picture
        if self.sender() == self.pushButton_1:
            active_picture = 'images/cities/1.jpg'
        elif self.sender() == self.pushButton_2:
            active_picture = 'images/cities/2.jpg'
        elif self.sender() == self.pushButton_3:
            active_picture = 'images/cities/3.jpg'
        elif self.sender() == self.pushButton_4:
            active_picture = 'images/cities/4.jpg'
        elif self.sender() == self.pushButton_5:
            active_picture = 'images/cities/5.jpg'
        elif self.sender() == self.pushButton_6:
            active_picture = 'images/cities/6.jpg'
        elif self.sender() == self.pushButton_7:
            active_picture = 'images/cities/7.jpg'
        elif self.sender() == self.pushButton_8:
            active_picture = 'images/cities/8.jpg'
        self.window.initUI()
        self.window.show()

    def initUI(self):
        self.build()
        uic.loadUi('categories_choice_menu.ui', self)
        self.setFixedSize(*self.SIZE)
        self.setGeometry(820, 40, *self.SIZE)
        self.setWindowIcon(QIcon('images/icon.png'))
        self.pushButton_1.setStyleSheet('background-image: url(images/cities/icons/1.jpg)')
        self.pushButton_2.setStyleSheet('background-image: url(images/cities/icons/2.jpg)')
        self.pushButton_3.setStyleSheet('background-image: url(images/cities/icons/3.jpg)')
        self.pushButton_4.setStyleSheet('background-image: url(images/cities/icons/4.jpg)')
        self.pushButton_5.setStyleSheet('background-image: url(images/cities/icons/5.jpg)')
        self.pushButton_6.setStyleSheet('background-image: url(images/cities/icons/6.jpg)')
        self.pushButton_7.setStyleSheet('background-image: url(images/cities/icons/7.jpg)')
        self.pushButton_8.setStyleSheet('background-image: url(images/cities/icons/8.jpg)')
        self.pushButton_1.clicked.connect(self.open_city_form)
        self.pushButton_2.clicked.connect(self.open_city_form)
        self.pushButton_3.clicked.connect(self.open_city_form)
        self.pushButton_4.clicked.connect(self.open_city_form)
        self.pushButton_5.clicked.connect(self.open_city_form)
        self.pushButton_6.clicked.connect(self.open_city_form)
        self.pushButton_7.clicked.connect(self.open_city_form)
        self.pushButton_8.clicked.connect(self.open_city_form)


class Animals(QMainWindow):

    def __init__(self):
        self.background_image2 = 'images/background_image.jpg'
        self.SIZE = [800, 800]
        self.window = Window()
        super().__init__()
        self.initUI()
        self.setWindowTitle('ANIMALS')

    def build(self):
        self.picture = QPixmap(self.background_image2)
        self.bg = QLabel(self)
        self.bg.move(0, 0)
        self.bg.resize(*self.SIZE)
        self.bg.setPixmap(self.picture)

    def open_animal_form(self):
        global active_picture
        if self.sender() == self.pushButton_1:
            active_picture = 'images/animals/dog.png'
        elif self.sender() == self.pushButton_2:
            active_picture = 'images/animals/fox.png'
        elif self.sender() == self.pushButton_3:
            active_picture = 'images/animals/giraff.png'
        elif self.sender() == self.pushButton_4:
            active_picture = 'images/animals/Hedgehog.jpeg'
        elif self.sender() == self.pushButton_5:
            active_picture = 'images/animals/lion.jpg'
        elif self.sender() == self.pushButton_6:
            active_picture = 'images/animals/monkey.jpg'
        elif self.sender() == self.pushButton_7:
            active_picture = 'images/animals/tiger.jpg'
        elif self.sender() == self.pushButton_8:
            active_picture = 'images/animals/panda.jpg'
        self.window.initUI()
        self.window.show()

    def initUI(self):
        self.build()
        uic.loadUi('categories_choice_menu.ui', self)
        self.setFixedSize(*self.SIZE)
        self.setGeometry(820, 40, *self.SIZE)
        self.setWindowIcon(QIcon('images/icon.png'))
        self.pushButton_1.setStyleSheet('background-image: url(images/animals/icons/dog.jpg)')
        self.pushButton_2.setStyleSheet('background-image: url(images/animals/icons/fox.png)')
        self.pushButton_3.setStyleSheet('background-image: url(images/animals/icons/giraff.png)')
        self.pushButton_4.setStyleSheet('background-image: url(images/animals/icons/Hedgehog.jpeg)')
        self.pushButton_5.setStyleSheet('background-image: url(images/animals/icons/lion.jpg)')
        self.pushButton_6.setStyleSheet('background-image: url(images/animals/icons/monkey.jpg)')
        self.pushButton_7.setStyleSheet('background-image: url(images/animals/icons/tiger.jpg)')
        self.pushButton_8.setStyleSheet('background-image: url(images/animals/icons/panda.jpg)')
        self.pushButton_1.clicked.connect(self.open_animal_form)
        self.pushButton_2.clicked.connect(self.open_animal_form)
        self.pushButton_3.clicked.connect(self.open_animal_form)
        self.pushButton_4.clicked.connect(self.open_animal_form)
        self.pushButton_5.clicked.connect(self.open_animal_form)
        self.pushButton_6.clicked.connect(self.open_animal_form)
        self.pushButton_7.clicked.connect(self.open_animal_form)
        self.pushButton_8.clicked.connect(self.open_animal_form)


class AboutGame(Menu):

    def __init__(self):
        self.background_image2 = 'images/background_image.jpg'
        super().__init__()
        self.initUI()
        self.setWindowTitle('ABOUT GAME')

    def build(self):
        self.picture = QPixmap(self.background_image2)
        self.bg = QLabel(self)
        self.bg.move(0, 0)
        self.bg.resize(*self.SIZE)
        self.bg.setPixmap(self.picture)

    def initUI(self):
        self.build()
        self.setGeometry(0, 40, *self.SIZE)
        self.setFixedSize(*self.SIZE)
        uic.loadUi('about_game.ui', self)
        self.setWindowIcon(QIcon('images/icon.png'))


def EXIT():
    sys.exit(app.exec())

class CropAndRandom:

    def __init__(self, img):
        self.image = img
        self.pieces_of_image = []
        self.side_size = 0


    def transform_difficult(self):
        k = 1
        im = Image.open(self.image)
        x_size, y_size = im.size
        x, y, x2, y2 = 0, 0, x_size // 4, y_size // 4
        for i in range(4): #y
            l_of_im = []
            for j in range(4): #x
                im_new = im.crop((x, y, x2, y2))
                l_of_im.append(str(k) + '.png')
                im_new.save(str(k) + '.png')
                x = x2
                x2 += x_size // 4
                k += 1
            self.pieces_of_image.append(l_of_im)
            y = y2
            y2 += y_size // 4
            x = 0
            x2 = x_size // 4
        return self.pieces_of_image

class Window(QMainWindow):
    def __init__(self):
        self.background_image = 'images/background_image.jpg'
        self.first_x, self.first_y, self.second_x, self.second_y = 0, 0, 0, 0
        self.coords_labels_slov = {'1_1': [0, 0, 150, 150], '1_2': [150, 0, 300, 150], '1_3': [300, 0, 450, 150], '1_4': [450, 0, 600, 150],
                                    '2_1': [0, 150, 150, 300], '2_2': [150, 150, 300, 300], '2_3': [300, 150, 450, 300], '2_4': [450, 150, 600, 300],
                                   '3_1': [0, 300, 150, 450], '3_2': [150, 300, 300, 450], '3_3': [300, 300, 450, 450], '3_4': [450, 300, 600, 450],
                                   '4_1': [0, 450, 150, 600], '4_2': [150, 450, 300, 600], '4_3': [300, 450, 450, 600], '4_4': [450, 450, 600, 600]}
        self.SIZE = [800, 800]
        super().__init__()
        self.initUI()

    def do_class(self, picture):
        expl = CropAndRandom(picture)
        return expl.transform_difficult()

    def create_images_field(self, pieces):
        [shuffle(i) for i in pieces]
        shuffle(pieces)
        self.pixmap = [[pieces[0][0], pieces[0][1], pieces[0][2], pieces[0][3]],
                       [pieces[1][0], pieces[1][1], pieces[1][2], pieces[1][3]],
                       [pieces[2][0], pieces[2][1], pieces[2][2], pieces[2][3]],
                       [pieces[3][0], pieces[3][1], pieces[3][2], pieces[3][3]]]
        self.label1_1.setPixmap(QPixmap(self.pixmap[0][0]))
        self.label1_2.setPixmap(QPixmap(self.pixmap[0][1]))
        self.label1_3.setPixmap(QPixmap(self.pixmap[0][2]))
        self.label1_4.setPixmap(QPixmap(self.pixmap[0][3]))
        self.label2_1.setPixmap(QPixmap(self.pixmap[1][0]))
        self.label2_2.setPixmap(QPixmap(self.pixmap[1][1]))
        self.label2_3.setPixmap(QPixmap(self.pixmap[1][2]))
        self.label2_4.setPixmap(QPixmap(self.pixmap[1][3]))
        self.label3_1.setPixmap(QPixmap(self.pixmap[2][0]))
        self.label3_2.setPixmap(QPixmap(self.pixmap[2][1]))
        self.label3_3.setPixmap(QPixmap(self.pixmap[2][2]))
        self.label3_4.setPixmap(QPixmap(self.pixmap[2][3]))
        self.label4_1.setPixmap(QPixmap(self.pixmap[3][0]))
        self.label4_2.setPixmap(QPixmap(self.pixmap[3][1]))
        self.label4_3.setPixmap(QPixmap(self.pixmap[3][2]))
        self.label4_4.setPixmap(QPixmap(self.pixmap[3][3]))

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        if (90 < x < 688) and (100 < y < 700):
            self.first_x = x
            self.first_y = y

    def mouseReleaseEvent(self, event):
        x = event.x()
        y = event.y()
        if (90 < x < 688 and self.first_x != 0) and (100 < y < 700 and self.first_y != 0) and (self.first_x != x or self.first_y != y):
            self.second_x = x
            self.second_y = y
            self.exchange_images()

    def exchange_images(self):
        word_key_1 = ''
        word_key_2 = ''
        for key in self.coords_labels_slov:
            slov = self.coords_labels_slov
            if int(slov[key][0]) + space_x <= self.first_x <= int(slov[key][2]) + space_x and int(slov[key][1]) + space_y <= self.first_y <= int(slov[key][3]) + space_y:
                word_key_1 = key
            if int(slov[key][0]) + space_x <= self.second_x <= int(slov[key][2]) + space_x and int(slov[key][1]) + space_y <= self.second_y <= int(slov[key][3]) + space_y:
                word_key_2 = key
        self.transform(word_key_1, word_key_2)

    def transform(self, statement_1, statement_2):
        self.sl[statement_1][0].setPixmap(QPixmap(self.sl[statement_2][1]))
        self.sl[statement_2][0].setPixmap(QPixmap(self.sl[statement_1][1]))
        self.sl[statement_2][1], self.sl[statement_1][1] = self.sl[statement_1][1], self.sl[statement_2][1]
        self.result()

    def result(self):
        rend = []
        for i in self.sl:
            rend.append(self.sl[i][1])
        if rend == final_field:
            self.label.show()

    def closeEvent(self, event):
        close = QMessageBox.question(self, "Совет", "Вы уверены, что хотите завершить сборку?",
                                               QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def build(self):
        self.picture = QPixmap(self.background_image)
        self.bg = QLabel(self)
        self.bg.move(0, 0)
        self.bg.resize(*self.SIZE)
        self.bg.setPixmap(self.picture)

    def initUI(self):
        global active_picture
        self.build()
        uic.loadUi('image_field.ui', self)
        self.setGeometry(0, 40, *self.SIZE)
        self.setFixedSize(*self.SIZE)
        self.setWindowTitle('PUZZLE MANIA')
        self.setWindowIcon(QIcon('images/icon.png'))
        self.label.hide()
        list_of_pieces = self.do_class(active_picture)
        self.create_images_field(list_of_pieces)
        self.sl = {'1_1': [self.label1_1, self.pixmap[0][0]],
                    '1_2': [self.label1_2, self.pixmap[0][1]],
                    '1_3': [self.label1_3, self.pixmap[0][2]],
                    '1_4': [self.label1_4, self.pixmap[0][3]],
                    '2_1': [self.label2_1, self.pixmap[1][0]],
                    '2_2': [self.label2_2, self.pixmap[1][1]],
                    '2_3': [self.label2_3, self.pixmap[1][2]],
                    '2_4': [self.label2_4, self.pixmap[1][3]],
                    '3_1': [self.label3_1, self.pixmap[2][0]],
                    '3_2': [self.label3_2, self.pixmap[2][1]],
                    '3_3': [self.label3_3, self.pixmap[2][2]],
                    '3_4': [self.label3_4, self.pixmap[2][3]],
                    '4_1': [self.label4_1, self.pixmap[3][0]],
                    '4_2': [self.label4_2, self.pixmap[3][1]],
                    '4_3': [self.label4_3, self.pixmap[3][2]],
                    '4_4': [self.label4_4, self.pixmap[3][3]]}


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())