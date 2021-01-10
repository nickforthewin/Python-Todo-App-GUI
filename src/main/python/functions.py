from PyQt5.QtWidgets import QMessageBox
import pickle

def setup(list_widget_obj, line_edit_obj):
    global list_widget
    global line_edit
    list_widget = list_widget_obj
    line_edit = line_edit_obj

def create_msg_box(msg_text):
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Warning")
    msg_box.setText(msg_text)
    msg_box.exec()

def add_task():
    if line_edit.text() == "" or line_edit.text().isspace():
        create_msg_box("Please enter a task to be completed")
    else:
        list_widget.addItem(line_edit.text())
        line_edit.setText("")

def del_task():
    selected_items = list_widget.selectedItems()
    for task in selected_items:
        list_widget.takeItem(list_widget.row(task))

def save_tasks():
    tasks = []
    if not list_widget.count():
        create_msg_box("Please enter tasks before saving")
    else:
        for task in range(list_widget.count()):
            tasks.append(list_widget.item(task).text())
        pickle.dump(tasks, open("tasks.dat", "wb"))

def load_tasks():
    try:
        list_widget.clear()
        tasks = pickle.load(open("tasks.dat", "rb"))
        for task in tasks:
            list_widget.addItem(task)
    except:
        create_msg_box("No saved tasks (tasks.dat not found)")