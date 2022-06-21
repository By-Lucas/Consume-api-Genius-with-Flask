import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    conn.execute('CREATE TABLE IF NOT EXISTS Artistas (id_transaction TEXT, artist TEXT, songs TEXT)')
    print ("Table created successfully")
    #conn.close()
    return conn

def add_data(id_transaction, artist, hits):  
    try:
        con = get_db_connection()
        c =  con.cursor() 
        c.execute("INSERT INTO Artistas (id_transaction, artist, songs) VALUES (?, ?, ?)", (id_transaction, artist, hits))
        con.commit() 
    except:
        print("Erro ao inserir dados na tabela")