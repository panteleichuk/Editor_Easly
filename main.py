from app_editor import app
from widget_editor import*
from data import*
import os

window = My_Window()
window.setLayout(main_layout)
workdir = ""
list_image = list()

img_edit = ImageEditor(lbl_image)

def click_img():
    fl = list_file.currentItem().text()
    print(fl)
    img_edit.open(fl)
def filterr():
    global list_image
    filter_list = []
    ext = [".png",'.jpg','.bmp']
    for fl in list_image:
        for e in ext:
            if fl.endswith(e):
                filter_list.append(fl)
                break
    list_image = filter_list
    list_file.clear()
    list_file.addItems(list_image)

def choose_folder():
    global workdir,list_image
    lbl_image.hide()
    file_directory.show()
    if file_directory.exec_():
        wokrdir = file_directory.selectedFiles()[0]
        print(wokrdir)
        img_edit.DIR = wokrdir
        list_image = os.listdir(wokrdir)
        print(list_image)
        filterr()
        lbl_image.show()
        file_directory.hide()
    else:
        lbl_image.show()
        file_directory.hide()



btn_folder.clicked.connect(choose_folder)
list_file.itemClicked.connect(click_img)

window.show()
app.exec_()