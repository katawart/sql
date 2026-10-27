from sqlite import *
from insertrecord import *
connector = sql_handling("geek.db")

class controller():
    def __init__(self) -> None:
        pass
    
    def insert_student(self,p_name, p_class, p_section):
        
        if p_section != 'A' and p_section != 'B' and p_section != 'C':
            print("error message") 
        else:
            
            insert_record("geek.db", [p_name, p_class, p_section])
            
if __name__ == "__main__":
    controller().insert_student("Richa", "12", 'A')