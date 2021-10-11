import sqlite3


class Model:

    def __init__(self, class_controller):
        self.connection = sqlite3.connect('Note_v2.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Notes_DB
                            (note_id int primary key, title text, content text, date text)
                        """)
        self.connection.commit()
        self.Controller = class_controller

    def Save_note_DB(self, note):
        print(f'************* saving data to DB *************')
        temp = (note.my_id, note.full_title, note.full_text, note.my_date)
        temp2 = []
        temp2.append(temp)
        print(f"list for saving @{temp2}")
        self.cursor.executemany("INSERT INTO Notes_DB VALUES (?,?,?,?)", temp2)
        self.connection.commit()

    def Delete_note_DB(self, note_id):
        print(f'************* deleting data to DB *************')
        sql = "DELETE FROM Notes_DB WHERE note_id = ?"
        self.cursor.execute(sql, (str(note_id),))
        self.connection.commit()

    def Update_note_DB(self, note):
        print(f'************* updating data to DB *************')
        temp = (note.full_title, note.full_text, note.my_date, note.my_id)
        print(temp)
        sql = """
        UPDATE Notes_DB
        SET title = ?, content = ?, date = ?
        WHERE note_id = ? 
        """
        self.cursor.execute(sql, temp)
        self.connection.commit()

    def Get_data_DB(self):
        print("************** get data from DB **************")
        sql = "SELECT * from Notes_DB"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print("Всего строк:  ", len(data))
        print("Вывод каждой строки")
        return data
