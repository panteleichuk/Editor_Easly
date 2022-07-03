from PyQt5.QtWidgets import(QWidget, QListWidget, QPushButton, QLabel, 
                            QHBoxLayout, QVBoxLayout, QFileDialog)

btn_folder = QPushButton('folder')
list_file = QListWidget()

lbl_img = QLabel('Image')
file_dialog = QFileDialog()
file_dialog.setFileMode(QFileDialog.DirectoryOnly)

btn_left = QPushButton("left")
btn_right = QPushButton("right")
btn_bw = QPushButton("b/w")
btn_blur = QPushButton("blur")
btn_mirror = QPushButton("mirror")

main_layout = QHBoxLayout()

lv1 = QVBoxLayout()
lv2 = QVBoxLayout()
lh = QHBoxLayout()

lv1.addWidget(btn_folder)
lv1.addWidget(list_file)

lh.addWidget(btn_left)
lh.addWidget(btn_right)
lh.addWidget(btn_bw)
lh.addWidget(btn_blur)
lh.addWidget(btn_mirror)

lv2.addWidget(lbl_img)
lv2.addWidget(file_dialog)

file_dialog.hide()
lv2.addLayout(lh)

main_layout.addLayout(lv1)
main_layout.addLayout(lv2)