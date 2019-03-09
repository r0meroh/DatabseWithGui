import sqlite3
# creates database and establishes connection
def connect():
    conn=sqlite3.connect('Games.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS game(id INTEGER PRIMARY KEY, title text, year integer, company text)')
    conn.commit()
    conn.close()

# create the insert function to add entries to database
def insert(title, year, company):
    conn=sqlite3.connect('Games.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO game Values(NULL, ?,?,?)',(title,year,company))
    conn.commit()
    conn.close()

# create view function to view the database entries
def view():
    conn=sqlite3.connect('Games.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM game')
    rows=cur.fetchall()
    conn.close()
    return rows


# create the search function to search for entry in database copy and paste from view
def search(title='', year='', company=''):
    conn=sqlite3.connect('Games.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM game WHERE title=? OR year=? OR company=?',(title,year,company))
    rows=cur.fetchall()
    conn.close()
    return rows


#create delete function copy and paste from insert
def delete(id):
    conn=sqlite3.connect('Games.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM game WHERE  id=?',(id,))
    conn.commit()
    conn.close()


# create update function cpy and paste from delete
def update(id,title,year,company):
    conn = sqlite3.connect('Games.db')
    cur = conn.cursor()
    cur.execute('UPDATE game SET title=?, year=?,company=? WHERE id=?',(title,year,company,id))
    conn.commit()
    conn.close()

connect()
# test the database and its functions
# insert('sonic the hedgehog', 1989, 'sony')
# delete(2)
# update(3,'sonic mans',1990,'microsoft')
# print(view())
# print(search(title='sonic the hedgehog'))