from pathlib import Path
import sqlite3
import pandas as pd

def create_db(db_name, filename, table_name):
    folder_data = 'data collection'
    file_path = Path(folder_data) / filename
    print(file_path)# create a path to the data file

    # folder_db = '../database'
    con = sqlite3.connect(db_name) # create a connection to the database
    cursor = con.cursor() # create a cursor

    data_titanic = pd.read_csv(file_path) # read in the data 
    # insert the data into the specified table 
    data_titanic.to_sql(table_name,con, index = False, if_exists='replace')

    # execute a select statement as f-string and print results to verify insertion
    executing_db = f"SELECT * FROM {table_name}"
    result = cursor.execute(executing_db).fetchall()
    print(result)
    # commit the changes to the database
    con.commit()
    # close the connection
    con.close()

if __name__=="__main__":
    db_name = "titanic.db"
    filename = "new_titanic.csv"
    table_name = "titanic_table"
    create_db(db_name, filename, table_name)
