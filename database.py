import time
import random
import sqlite3
from config import *

def start_database():
	with sqlite3.connect("./data/DB/Database.db") as conn:
		cursor = conn.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS users (
		    name TEXT,
		    id INT,
		    money BIGINT,
		    inventory TEXT,
		    desc TEXT,
		    lvl INT,
		    xp INT
		)""")
		cursor.execute("""CREATE TABLE IF NOT EXISTS premium_guild (
		    id_guild INT,
		    premium BOOL,
		    date INT
		)""")
		cursor.execute("""CREATE TABLE IF NOT EXISTS commands (
		    am BOOL,
		    commands_numbers BIGINT
		)""")
		cursor.execute("""CREATE TABLE IF NOT EXISTS premium_user (
			id INT,
			premium INT
		)""")
	conn.close()

def commands():
	with sqlite3.connect("./data/DB/Database.db") as conn:
		cursor = conn.cursor()
		if cursor.execute(f"SELECT am FROM commands WHERE am = True").fetchone() is None:
			cursor.execute(f"INSERT INTO commands VALUES (?, ?)", (True, 0))
		else:
			for row in cursor.execute(f"SELECT commands_numbers FROM commands WHERE am = True"):
				cursor.execute("UPDATE commands SET commands_numbers = ? WHERE am = ?", (row[0] + 1, True))
	conn.close()

def premium(id, author):
	if author == id_owner:
		with sqlite3.connect("./data/DB/Database.db") as conn:
			cursor = conn.cursor()
			for row in cursor.execute(f"SELECT premium, date FROM premium_guild WHERE id_guild = {id}"):
				cursor.execute("UPDATE premium_guild SET premium = ?, date = ? WHERE id_guild = ?", (True, time.time(), id))
		conn.close()

def economy(id):
	with sqlite3.connect("./data/DB/Database.db") as conn:
		cursor = conn.cursor()
		for row in cursor.execute(f"SELECT lvl,xp,money FROM users WHERE id = {id}"):
			cursor.execute("UPDATE users SET xp = ? WHERE id = ?", (row[1]+random.randint(15, 25), id))
			if row[1] > (5*row[0]**2+50*row[0]+100):
				cursor.execute("UPDATE users SET lvl = ?, xp = ?, money = ? WHERE id = ?", (row[0]+1, 0, row[2]+500*row[0], id))
	conn.close()

def proverka(id, author, author_name):
	with sqlite3.connect("./data/DB/Database.db") as conn:
		cursor = conn.cursor()
		if cursor.execute(f"SELECT id FROM users WHERE id = {author}").fetchone() is None:
			cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)", (author_name, author, 500, '{}', ' ', 1, 0))
		if cursor.execute(f"SELECT id_guild FROM premium_guild WHERE id_guild = {id}").fetchone() is None:
			cursor.execute("INSERT INTO premium_guild VALUES (?, ?, ?)", (id, False, time.time()))
	conn.close()

def desc(id, arg):
	with sqlite3.connect("./data/DB/database.db") as conn:
		cursor = conn.cursor()
		cursor.execute("UPDATE users SET desc = ? WHERE id = ?", (arg, id))
	conn.close()