"""
Utils
"""

import sqlite3

class NetworkData:
    """
    A class filled with static methods that interacts with the sqlite database.
    """

    @staticmethod
    def create_con():
        '''Create Database Connection'''
        return sqlite3.connect('signature.db')

    @staticmethod
    def setup_db():
        '''Create Sqlite3 DB with all required tables'''
        if exists('signature.db'):
            pass
        else:
            with open('signature.db', 'x', encoding='utf-8') as _:
                pass
            conn = sqlite3.connect('signature.db')
            # Create Signatures Table
            conn.execute('''CREATE TABLE "signatures" (
	        "id"	INTEGER NOT NULL UNIQUE,
            "tcp"	TEXT,
	        "port"	TEXT NOT NULL,
            "address"  TEXT NOT NULL,
	        PRIMARY KEY("id" AUTOINCREMENT)
            );''')
            conn.close()
        return True