from PIL import Image, ImageFilter
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt
import os
#функція пошуку абсолютного шляху до файлу
def abs_path(name_file):
        p = os.path.abspath(__file__+"/..")
        p = os.path.join(p, name_file)
        return p
#клас для обробки зображення

class My_Window (QWidget):
        def __init__(self):
                super().__init__()
                self.resize(700, 700)
                self.setWindowTitle('Easy Editor')
                self.move(0,0)
                self.setStyleSheet('QWidget{background-color: rgb(102,201,128);}')

#Клас ImageEditor повинен володіти полями та методами для читання та обробки зображень.
class ImageEditor:
        def __init__(self,lbl_img):
                self.DIR = None#
                self.DIR_CHANGE = '/Change'#
                self.NAME_IMG = None#
                self.IMAGE = None#
                self.PIX_IMG = None#
                self.LBL_IMG = lbl_img#
                
# Наповнення класу:
# 1) Конструктор, що заповнює поля: "ім'я файлу", "оригінал", "список змінених зображень".

# 2) Метод open(), що зчитує зображення.
        def open(self, new_file):
                self.NAME_IMG = new_file
                try:
                        #self.Name_file = abs_path(self.Name_file)
                        path = os.path.join(self.DIR,self.NAME_IMG)
                        self.IMAGE = Image.open(path)
                        self.load_img(path)
                except:
                        print("No file found")
                        self.LBL_IMG.setText("Can not open image")

        def load_img(self,path):
                self.LBL_IMG.hide()
                self.PIX_IMG = QPixmap(path)
                w,h = self.LBL_IMG.width(), self.LBL_IMG.height()
                self.PIX_IMG = self.PIX_IMG.scaled(w,h, Qt.KeepAspectRatio)
                self.LBL_IMG.setPixmap(self.PIX_IMG)
                self.LBL_IMG.show()

# 3) Метод save(), що зберігає зображення в окремій папці.
        def do_save(self, save_image):
                pass

# 4) Методи обробки зображення - do_left() 0 
        def do_left(self):
                pic_left = self.Original.transpose(Image.ROTATE_90)
                self.List_change[0].append(pic_left)
                pic_left.show()
                pic_left.save("left_image.jpg")
# Методи обробки зображення - do_rigth() 1
        def do_right(self):
                pic_right = self.Original.transpose(Image.ROTATE_270)
                self.List_change[1].append(pic_right)
                pic_right.show()
                pic_right.save("right_image.jpg")
# Методи обробки зображення - do_blured() 2
        def do_blured(self):
                pic_blur = self.Original.filter(ImageFilter.BLUR)
                self.List_change[2].append(pic_blur)
                pic_blur.show()
                pic_blur.save("blur_image.jpg")
# Методи обробки зображення - do_bw() 3
        def do_bw(self):
                pic_bw = self.IMAGE.convert('L')
                path = os.path.join(self.DIR,self.DIR_CHANGE)
                if not( os.path.exists(path) or os.path.isdir(path) ):
                        os.mkdir(path)
                path = os.path.join(path,"bw_"+self.NAME_IMG+".png")
                pic_bw.save(path)
                self.load_img(path)
#example_imp = ImageEditor("original.jpg")
#example_imp.open()

# Методи обробки зображення - do_mirror() 4





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