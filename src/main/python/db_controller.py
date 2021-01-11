import sqlite3

class DbController():
    def __init__(self):
        self.db_name = "tasks.db" 

    def query(self, sql, data):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute(sql, data)
            db.commit()

    def select_query(self, sql):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
        return results

    def add_task(self, task):
        self.query("INSERT INTO Tasks (Description) VALUES (?)", (task,))

    def get_all_tasks(self):
        results = self.select_query("SELECT * FROM Tasks")
        return results

    def delete_task(self, task_id):
        self.query("DELETE FROM Tasks WHERE TaskID = ?", (task_id,))