
import sqlite3 as sql

#Class - Not connect to particular database
class sql_handling():

    cursor = ""
    my_conn = ""
    
    #Construtor
    def __init__(self, database):  #Self parameter is ignored externally      
        
        #Create the connection object       
        with sql.connect(database) as self.my_conn:
        #printing the connection object   
            print(self.my_conn)  
            self.cursor = self.my_conn.cursor()     #Exectues scripts and quries
    
    #Preconditions: Takes two values a queery to run, vals to run
    #Changing data
    def sql_execute(self, query, vals):
        self.cursor.execute(query, vals)      
        self.my_conn.commit()   #Commit = change
    
    #Precondition: Takes one value a query to run
    #Postcondition: Returns x number of rows from a database
    def fetch_all(self, query):
        self.cursor.execute(query)    
        return self.cursor.fetchall()  #FetchAll = bring data from 


    #Preconditions: Takes two values a database name and a list of values to insert into the database
    #Postcondition: Inserts a record into the database
    def insert_record(self, database, values):
        
        vals = (values[0], values[1], values[2])
        self.cursor.execute(f"INSERT INTO student VALUES (?, ?, ?)", vals)    
        self.my_conn.commit()    


if __name__ == "__main__":
    connector = sql_handling("geek.db")
    rows = connector.fetch_all(f"SELECT * FROM student;")
    for row in rows:
        print(row)
        for field in row:
            print(field)