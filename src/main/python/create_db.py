import sqlite3

def create_db():
    with sqlite3.connect("tasks.db") as db:
        cursor = db.cursor()

        cursor.execute("""CREATE TABLE Tasks(
            TaskID integer,
            Description text,
            PRIMARY KEY(TaskID)
        )""")

        db.commit()