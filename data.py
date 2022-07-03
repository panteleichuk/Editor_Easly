from PIL import Image, ImageFilter
import os
from PyQt5.QtWidgets import QWidget,QPushButton,QListWidget
from PyQt5.QtGui import QIcon,QPixmap,QImage
from PyQt5.QtCore import QSize,Qt
#from PyQt5.QtWidgets import QPushButton,QWidget
# from PyQt5.QtGui import QPixmap,QImage, QIcon,QLinearGradient,QPalette,QBrush
# from PyQt5.QtCore import Qt,QSize

#функція пошуку абсолютного шляху до файлу
def abs_path(name_file):
    p = os.path.abspath(__file__+"/..")
    p = os.path.join(p, name_file)
    return p


class My_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700,700)
        self.setWindowTitle("Easy Editor")
        self.move(100,100)
        self.setStyleSheet('QWidget{background-color: rgb(100,115,10);}')
        

class My_Button(QPushButton):
    def __init__(self,name_img):
        super().__init__()
        name_img = abs_path(name_img)
        icon = QIcon(name_img)
        self.setIcon(icon)
        self.setIconSize(QSize(50,50))
        self.setFixedSize(40,40)
        self.setStyleSheet('QPushButton{background-color: rgb(255,15,110);}')


class My_List(QListWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('QListWidget{background-color: rgb(150,135,110);}')















# class My_Window(QWidget):
#     def __init__(self, width, height, color,title,icon, main_line):
#         super().__init__()
#         self.resize(width,height)
#         self.setWindowTitle(title)
#         icon = QIcon(abs_path(icon))
#         self.setWindowIcon(icon)
        # p = QPalette()
        # gradient = QLinearGradient(0, 0, 0, 400)
        # gradient.setColorAt(0.0, QColor(240, 240, 240))
        # gradient.setColorAt(1.0, QColor(240, 160, 160))
        # p.setBrush(QPalette.Window, QBrush(gradient))
        #self.setPalette(p)
#         # self.setLayout(main_line)
# class My_Button(QPushButton):
#     def __init__(self,name_image):
#         super().__init__()
#         self.IMAGE = QIcon(abs_path(name_image))
#         self.setIcon(self.IMAGE)
#         self.setIconSize(QSize(50,50))
# #клас для обробки зображення
# Клас ImageEditor повинен володіти полями та методами для читання та обробки зображень.
class ImageEditor:
# Наповнення класу:
# 1) Конструктор, що заповнює поля: "ім'я файлу", "оригінал", "список змінених зображень".
    def __init__(self,lbl_image):
        self.NAME_FILE = None
        self.FILE = None
        self.PAXMAP_IMG = None
        self.ORIGINAL = None
        self.LIST_CHANGE = [None,None,None,None]
        self.DIR = None
        self.LBL_IMAGE = lbl_image

    def load_img(self): 
        try:
            self.PAXMAP_IMG = QPixmap(self.NAME_FILE)
            
            w,h = self.LBL_IMAGE.width(), self.LBL_IMAGE.height()
           
            self.PAXMAP_IMG = self.PAXMAP_IMG.scaled(w,h, Qt.KeepAspectRatio)
            
            self.LBL_IMAGE.setPixmap(self.PAXMAP_IMG)
            
        except:
            self.LBL_IMAGE.setText("Image can not open")
        
        
        
# 2) Метод open(), що зчитує зображення.
    def open(self,new_file):
        self.FILE = new_file
        self.NAME_FILE = os.path.join(self.DIR,new_file)
        try:
            
            self.ORIGINAL = Image.open(self.NAME_FILE)
            
        except:
            print("No file in directory!")
        self.load_img()

# 3) Метод save(), що зберігає зображення в окремій папці.
    def do_save(self,save_image,name, kind):
        name_file = name.split('.')
        name_file[0] = name_file[0]+"_"+kind
        name_file ='.'.join(name_file)
        abs_name_file = os.path.join(self.DIR, name_file)
        save_image.save(abs_name_file)
        return name_file

# 4) Методи обробки зображення - do_left() - 0
    def do_left(self):
        pic_bw = self.ORIGINAL.transpose(Image.ROTATE_90)
        self.LIST_CHANGE[0] = (pic_bw)
       
        pic_bw.save("left_image.jpg")

# Методи обробки зображення - do_rigth() - 1
    
# Методи обробки зображення - do_blured() -2
    def do_blured(self):
        pic_blur = self.ORIGINAL.filter(ImageFilter.BLUR)
        self.LIST_CHANGE[2] = (pic_blur)
       
        pic_blur.save("blur_image.jpg")
# Методи обробки зображення - do_bw() - 3
    def do_bw(self):
        pic_bw = self.ORIGINAL.convert("L")
        self.LIST_CHANGE[3] = (pic_bw)
        self.FILE = self.do_save(pic_bw,self.FILE,"bw")
        self.NAME_FILE = abs_path( self.FILE)

# Методи обробки зображення - do_mirror() - 4


# exemple_imp = ImageEditor("original.jpg")
# exemple_imp.open()
# exemple_imp.do_blured()


# 5) Методи обробки зображення та do_cropped().
        # 1) Визнач прямокутну частину box, що вирізається. Задай її як
        # box = (<ліво>, <верх>, <право>, <низ>).
        # Спробуй box = (100, 100, 400, 450).
        # Чи можна поліпшити фрагмент, що вирізується?

        # 2) Обріж фотографію вбудованим методом PIL:
        # cropped = self.original.crop(box) - "вирізати з оригіналу прямокутник і зберегти в cropped".

        # 3) Аналогічно минулим методам, додай нову картинку до списку змінених фотографій та збережи до папки проекту.

# А раптом ця програма використовуватиметься для обробки 10 фотографій? 100 фотографій? Щоб не вигадувати імена файлів самим, запрограмуємо автоматичний неймінг.

# Нехай оригінал фотографії називається original.jpg. Тоді дві оброблені картинки будуть називатися original1.jpg та original2.jpg.

# 1) Формування імені має відбуватися у методі-обробнику перед збереженням файлу в папку проекту.

# 2) Сформуй нове ім'я. Ім'я оригіналу лежить у полі filename.
# - Відокремили назву файлу від його розширення. Використовуй метод split().
# - Сформуй нове ім'я, наприклад, як (назва_оригіналу + число_змінених_фото + '.' + формат_файлу).

# Нове ім'я готове.