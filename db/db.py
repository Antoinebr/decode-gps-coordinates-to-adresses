import sqlite3

class DB:

    def __init__(self, dbName = "../db.db"):

        self.conn = sqlite3.connect(dbName)
        self.cur = self.conn.cursor()
        self.conn.commit()
        # REAL = FLOAT
        
        

    def createTable(self,sqlQuery):

        self.cur.execute(sqlQuery)
        self.conn.commit()
        


    # valuesToInsert : tupple
    def insert(self, sqlQuery, valuesToInsert):

        self.cur.execute(sqlQuery, valuesToInsert)
        self.conn.commit()
    

    def get(self, sqlQuery):
   
        self.cur.execute(sqlQuery)
        rows = self.cur.fetchall()
        return rows

