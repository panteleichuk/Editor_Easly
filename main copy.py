#створи тут фоторедактор Easy Editor!
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os
from app_editor import app
from interfase import*
from data import*
window = My_Window(700,700,"grey","Easy Editor",'btn\icon.png', main_layout)
# window = QWidget()
# window.resize(700,700)
# window.setWindowTitle("Easy Editor")
# window.setLayout(main_layout)
file_list = list()
file_dir = ""
list_images = list()
image_process = ImageEditor()
def my_filter(file_dir):
    file_list = os.listdir(file_dir)
    filter_list = []
    print(file_list)
    find_file = [".png",'.jpg']
    for f in file_list:
        for end in find_file:
            if f.endswith(end):
                filter_list.append(f)
    print(filter_list)
    list_image.clear()
    list_image.addItems(filter_list)
    
def click_folder():
    global workdir, file_dir
    workdir.show()
    image.hide()
    if workdir.exec_():
        file_dir = workdir.selectedFiles()[0]
        print(file_dir)
        image.show()
        my_filter(file_dir)
def click_image():
    img = list_image.currentItem().text()
    image_process.load_img(img,file_dir,image)
    list_images.append(image_process)
    


btn_folder.clicked.connect(click_folder)    
list_image.itemClicked.connect(click_image)
window.show()
app.exec_()