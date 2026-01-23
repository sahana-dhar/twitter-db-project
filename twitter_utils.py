"""
filename: twitter_utils.py

description: A collection of database utilities to make it easier
to implement a database application (specific for sqlite3 instead of MySQL)

Written by Anya
"""

import sqlite3
import pandas as pd

class DBUtils:

    def __init__(self, database):
        """ Connect to database file.
        """
        self.con = sqlite3.connect(database)

    def close(self):
        """ Close the connection """
        self.con.close()
        self.con = None

    def execute(self, query):
        """ Execute a select query and returns the result as a dataframe """

        # Step 1: Create cursor
        rs = self.con.cursor()

        # Step 2: Execute the query
        rs.execute(query)

        # Step 3: Get the resulting rows and column names
        rows = rs.fetchall()
        cols = [description[0] for description in rs.description] # change for sqlite3 (not column_names)

        # Step 4: Close the cursor
        rs.close()

        # Step 5: Return result
        return pd.DataFrame(rows, columns=cols)


    def insert_one(self, sql, val):
        """ Insert a single row """
        cursor = self.con.cursor()
        cursor.execute(sql, val)
        self.con.commit()


    def insert_many(self, sql, vals):
        """ Insert multiple rows """
        cursor = self.con.cursor()
        cursor.executemany(sql, vals)
        self.con.commit()



