from PyQt5.QtWidgets import QWidget,QApplication, QPushButton,QLabel,QListWidget,QVBoxLayout, QHBoxLayout,  QFileDialog
from app_editor import app
from data import*

btn_folder = QPushButton("folder")
list_image = QListWidget()

image = QLabel("Image")
image.resize(400,400)

# btn_bw = QPushButton("B/W")
# btn_mirror = QPushButton("Mirror")
# btn_blur = QPushButton("Blur")
# btn_left = QPushButton("Left")
# btn_rigth = QPushButton("Rigth")
btn_bw = My_Button("btn/bw.png")
btn_mirror = My_Button("btn/mir.png")
btn_blur = My_Button("btn/blur.png")
btn_left = My_Button("btn/left.png")
btn_rigth = My_Button("btn/right.png")

workdir = QFileDialog()
workdir.setFileMode(QFileDialog.DirectoryOnly)

main_layout = QHBoxLayout()

line_V1 = QVBoxLayout()
line_V2 = QVBoxLayout()

line_H1 = QHBoxLayout()

line_V1.addWidget(btn_folder)
line_V1.addWidget(list_image)

line_H1.addWidget(btn_left)
line_H1.addWidget(btn_rigth)
line_H1.addWidget(btn_blur)
line_H1.addWidget(btn_bw)
line_H1.addWidget(btn_mirror)

line_V2.addWidget(image)
line_V2.addWidget(workdir)
workdir.hide()
line_V2.addLayout(line_H1)
main_layout.addLayout(line_V1)
main_layout.addLayout(line_V2)

def click_folder():
    workdir.show()
    image.hide()
    if workdir.exec_():
        workdir = fl_dialog.selectedFiles()[0]
        print(fl_dialog.selectedFiles()[0])