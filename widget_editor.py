from PyQt5.QtWidgets import(QWidget,QListWidget,
                            QPushButton,QLabel,
                            QFileDialog,QHBoxLayout,
                            QVBoxLayout)
from data import*

btn_folder = QPushButton("Folder")
list_file = My_List()

lbl_image = QLabel("IMAGE")
file_directory = QFileDialog()
file_directory.setFileMode(QFileDialog.DirectoryOnly)

# btn_left = QPushButton("Left")
# btn_rigth = QPushButton("Right")
# btn_bw = QPushButton("B/W")
# btn_blur = QPushButton("Blur")
# btn_mirror = QPushButton("Mirror")

btn_left = My_Button('btn/left.png')
btn_rigth = QPushButton("Right")
btn_bw = QPushButton("B/W")
btn_blur = QPushButton("Blur")
btn_mirror = QPushButton("Mirror")

main_layout = QHBoxLayout()

line_V1 = QVBoxLayout()
line_V2 = QVBoxLayout()
line_H = QHBoxLayout()

line_V1.addWidget(btn_folder)
line_V1.addWidget(list_file)

line_H.addWidget(btn_left)
line_H.addWidget(btn_rigth)
line_H.addWidget(btn_bw)
line_H.addWidget(btn_blur)
line_H.addWidget(btn_mirror)

line_V2.addWidget(lbl_image)
line_V2.addWidget(file_directory)
file_directory.hide()
line_V2.addLayout(line_H)

main_layout.addLayout(line_V1)
main_layout.addLayout(line_V2)

