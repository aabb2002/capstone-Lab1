import sqlite3

db = 'menuDB.db'

class MenuDB:
    

    def create_table():
        with sqlite3.connect(db) as conn:
            create_table_sql = 'CREATE TABLE IF NOT EXISTS juggling_record (Name text, Country text, Catches int)'
            conn.execute(create_table_sql)
        conn.close()

    def get_all_records():
        select_sql_statement = 'SELECT * FROM juggling_record'
        conn = sqlite3.connect(db)
        all_records = conn.execute(select_sql_statement)

        return all_records

    def make_new_record(name, country, catches):
        with sqlite3.connect(db) as conn:
            insert_sql_statement = 'INSERT INTO juggling_record (Name, Country, Catches) VALUES (?, ?, ?)'
            conn.execute(insert_sql_statement, (name, country, catches))
        conn.close()

    def edit_record(name, catches):
        update_sql_statement = 'UPDATE juggling_record SET  Catches = ? WHERE name = ?'

        with sqlite3.connect(db) as conn:
            conn.execute(update_sql_statement, (catches, name))
        conn.close()

    def delete_record(name):
        delete_sql_statement = 'DELETE FROM juggling_record WHERE name = ?'

        with sqlite3.connect(db) as conn:
            conn.execute(delete_sql_statement, name)
        conn.close()
