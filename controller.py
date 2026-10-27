import sqlite as connector

class controller():
    def __init__(self) -> None:
        self.connector = connector.sql_handling("geek.db")
    
    def insert_student(self,p_name, p_class, p_section):
        
        if p_section != 'A' and p_section != 'B' and p_section != 'C':
            print("error message") 
        else:
            
            self.connector.insert_record("geek.db", [p_name, p_class, p_section])
            
if __name__ == "__main__":
    controller().insert_student("Richa", "15", 'A')