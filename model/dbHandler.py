import sqlite3 as SQL


def match_exact(word: str) -> list:
    """
    This method will:
    1. Accept a string
    2. Search the dictionary for an exact match
    3. If success return the definition
    4. If not return an empty list
    """

    db = SQL.connect("data/dictionary.db")
    sql_query = "SELECT * FROM entries where word = ?"
    match = db.execute(sql_query, (word,)).fetchall()
    db.close()
    return match

    # TODO: Establish connection to the dictionary database

    # TODO: Query the database for exact matches

    # TODO: Clone the connection to the database
    


def match_like(word: str) -> list:
    """
    This method will:
    1. Accept a string
    2. Search the dictionary for approximate matches
    3. If success return the definition as a list
    4. If not return an empty list
    """

    db = SQL.connect("data/dictionary.db")
    sql_query = "SELECT * FROM entries WHERE word LIKE ?"
    match = db.execute(sql_query, ("%" + word + "%",)).fetchall()
    db.close()
    return match

    # TODO: Establish connection to the dictionary database
    
    # TODO: Query the database for exact matches
    
    # TODO: Clone the connection to the database
    

