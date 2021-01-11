from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QLineEdit, QLabel, QPushButton
from table_widget import *
from create_db import *

import sys
import os

from functions import *

class MainWindow(QWidget):
    def __init__(self):
        if not os.path.exists("tasks.db"):
            create_db()

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        table_widget = TableWidget()
        layout.addWidget(table_widget)

        label = QLabel("Type a task below:")
        layout.addWidget(label)

        line_edit = QLineEdit()
        layout.addWidget(line_edit)

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        add_btn = QPushButton("Add to list")
        add_btn.clicked.connect(add_task)
        button_layout.addWidget(add_btn)

        del_btn = QPushButton("Delete task")
        del_btn.clicked.connect(del_task)
        button_layout.addWidget(del_btn)

        setup(line_edit, table_widget)

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    appctxt.app.setStyle("Fusion")
    appctxt.app.setStyleSheet("QPushButton { padding: 10px; } QListWidget { margin-bottom: 15px; }")
    window = MainWindow()
    window.setWindowTitle("Tasks App")
    window.setFixedSize(600, 400)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)