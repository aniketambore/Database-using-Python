import sqlite3
from datetime import datetime as dt


def create_table():
    conn=sqlite3.connect("piece.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS piece (id INTEGER PRIMARY KEY, datetime integer, name text, colour text, count integer, status text)")
    conn.commit()
    conn.close()

def insert(datetime,name,colour,count,status):
    conn=sqlite3.connect("piece.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO piece VALUES (NULL,?,?,?,?,?)",(datetime,name,colour,count,status))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("piece.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM piece")
    row=cur.fetchall()
    conn.close()
    return row

def search(datetime="",name="",colour="",count="",status=""):
    conn=sqlite3.connect("piece.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM piece WHERE datetime=? OR name=? OR colour=? OR count=? OR status=?",(datetime,name,colour,count,status))
    row=cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn=sqlite3.connect("piece.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM piece WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,datetime,name,colour,count,status):
    conn=sqlite3.connect("piece.db")
    cur=conn.cursor()
    cur.execute("UPDATE piece SET datetime=?, name=?, colour=?, count=?, status=? WHERE id=?",(datetime,name,colour,count,status,id))
    conn.commit()
    conn.close()


create_table()
#insert(dt.now(),'maa','blue',3,'Hemming')
##search(name='Ani')
#print(view())
#delete(2)
#update(1, '2019-07-04 12:15:56.245735', 'Aniket', 'pink', 9, 'Hemming')
