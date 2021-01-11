from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from db_controller import DbController

controller = DbController()

class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["ID", "Name"])
        self.show_items(controller.get_all_tasks())
        self.horizontalHeader().setStretchLastSection(True)

    def show_items(self, tasks_list):
        if len(tasks_list) == 0:
            self.setRowCount(0)
        else:
            row = 0
            for entry in tasks_list:
                self.setRowCount(row+1)
                column = 0
                for item in entry:
                    self.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row += 1

    def get_id(self):
        return int(self.item(self.currentRow(), 0).text())