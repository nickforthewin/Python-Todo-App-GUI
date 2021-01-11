from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import pickle
from db_controller import DbController

controller = DbController()

def setup(line_edit_obj, table_widget_obj):
    global line_edit
    global table_widget
    line_edit = line_edit_obj
    table_widget = table_widget_obj

def create_msg_box(msg_text):
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Warning")
    msg_box.setText(msg_text)
    msg_box.exec()

def add_task():
    if line_edit.text() == "" or line_edit.text().isspace():
        create_msg_box("Please enter a task to be completed")
    else:
        controller.add_task(line_edit.text())
        table_widget.show_items(controller.get_all_tasks())
        line_edit.setText("")

def del_task():
    task_id = table_widget.get_id()
    controller.delete_task(task_id)
    table_widget.show_items(controller.get_all_tasks())
