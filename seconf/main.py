from app_Editor import app
from widget import*
from data import*
import os

win = My_Window()
win.setLayout(main_layout)
workdir = ''
list_image = list()
img_editor = ImageEditor(lbl_img)
def filter_file():
    global list_image
    expansion = [".png",".jpg",".webp",".svg",".gif",'.bmp']
    filter_list = list()
    for fl in list_image:
        '''"fl="1.png", fl = "home.doc"'''
        for ex in expansion:
            fl = fl.lower()
            if fl.endswith(ex):
                filter_list.append(fl)
    print("Filter",filter_list)
    list_image = filter_list
    list_file.clear()
    list_file.addItems(list_image)

def click_image():
    img_editor.DIR = workdir
    click_file = list_file.currentItem().text()
    img_editor.open(click_file)

def Choose_folder():
    global workdir,list_image
    lbl_img.hide()
    file_dialog.show()
    if file_dialog.exec_():
        workdir = file_dialog.selectedFiles()[0]
        print(workdir)
        list_image = os.listdir(workdir)
        print(list_image)
        filter_file()

        lbl_img.show()
        file_dialog.hide()
    else:
        lbl_img.show()
        file_dialog.hide()


btn_folder.clicked.connect(Choose_folder)
list_file.itemClicked.connect(click_image)
btn_bw.clicked.connect(img_editor.do_bw)
win.show()
app.exec_()