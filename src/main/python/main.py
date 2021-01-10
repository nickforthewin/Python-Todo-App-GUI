from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QListWidget, QLineEdit, QLabel, QPushButton

import sys

from functions import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        list_widget = QListWidget()
        layout.addWidget(list_widget)

        label = QLabel("Type a task below:")
        layout.addWidget(label)

        line_edit = QLineEdit()
        layout.addWidget(line_edit)

        add_btn = QPushButton("Add to list")
        add_btn.clicked.connect(add_task)
        layout.addWidget(add_btn)

        del_btn = QPushButton("Delete task")
        del_btn.clicked.connect(del_task)
        layout.addWidget(del_btn)

        save_btn = QPushButton("Save tasks")
        save_btn.clicked.connect(save_tasks)
        layout.addWidget(save_btn)

        load_btn = QPushButton("Load saved tasks")
        load_btn.clicked.connect(load_tasks)
        layout.addWidget(load_btn)

        setup(list_widget, line_edit)

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    appctxt.app.setStyle("Fusion")
    appctxt.app.setStyleSheet("QPushButton { padding: 10px; } QListWidget { margin-bottom: 15px; }")
    window = MainWindow()
    window.setWindowTitle("Tasks App")
    window.setFixedSize(300, 500)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)