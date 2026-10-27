import sqlite3

def insert_record(database, values):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    vals = (values[0], values[1], values[2])
    cursor.execute(f"INSERT INTO student VALUES (?, ?, ?)", vals)    
    conn.commit()
    
if __name__ == "__main__":
    database = "geek.db"
    values = ("Test Name", "Test Class", "B")

    insert_record(database, values)

