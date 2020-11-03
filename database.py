import time
import random
import config
import pymysql

conn = pymysql.connect(
	host = "localhost",
	user = "root",
	password = "amthebot127",
	db = "forbot"
)

def start_database():
	with conn.cursor() as cursor:
		cursor.execute("""CREATE TABLE IF NOT EXISTS users (
			name TEXT NOT NULL ,
			id BIGINT NOT NULL,
			money BIGINT,
			inventory MEDIUMTEXT,
			description TEXT,
			lvl SMALLINT UNSIGNED NOT NULL,
			xp INT UNSIGNED
		)""")
	conn.commit()

	with conn.cursor() as cursor:
		cursor.execute("""CREATE TABLE IF NOT EXISTS commands (
			am BOOL,
			commands_numbers BIGINT UNSIGNED
		)""")
	conn.commit()

def commands_view():
	with conn.cursor() as cursor:
		cursor.execute("SELECT commands_numbers FROM commands")
		return cursor.fetchone()[0]

def commands():
	with conn.cursor() as cursor:
		if cursor.execute("SELECT 1 FROM commands WHERE am = True") == 0:
			cursor.execute("INSERT INTO commands (am, commands_numbers) VALUES (True, 1)")
		else:
			cursor.execute("UPDATE commands SET commands_numbers = {} WHERE am = True".format(commands_view() + 1))
	conn.commit()

def economy(id):
	with sqlite3.connect("./data/DB/Database.db") as conn:
		cursor = conn.cursor()
		for row in cursor.execute(f"SELECT lvl,xp,money FROM users WHERE id = {id}"):
			cursor.execute("UPDATE users SET xp = ? WHERE id = ?", (row[1]+random.randint(15, 25), id))
			if row[1] > (5*row[0]**2+50*row[0]+100):
				cursor.execute("UPDATE users SET lvl = ?, xp = ?, money = ? WHERE id = ?", (row[0]+1, 0, row[2]+500*row[0], id))
	conn.close()

def proverka(id, author_name):
	with conn.cursor() as cursor:
		try:
			if cursor.execute("SELECT 1 FROM users WHERE id = {}".format(id)) == 0:
				cursor.execute("INSERT INTO users (name, id, money, inventory, description, lvl, xp) VALUES ('{}', {}, {}, '{}', '{}', {}, {})".format(author_name, id, 500, "[]", " ", 1, 0))
		except pymysql.err.DataError:
			pass
		finally:
			conn.commit()

def desc(id, arg):
	if len(arg) < 1001:
		with conn.cursor() as cursor:
			cursor.execute("UPDATE users SET description = '{}' WHERE id = {}".format(arg, id))
		conn.commit()

def stat(id):
	with sqlite3.connect("./data/DB/database.db") as conn:
		conn.row_factory = lambda cursor, row: row[0]
		data = {}
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM users")
		for i in [description[0] for description in cursor.description]:
			data.update({i:cursor.execute("SELECT {} FROM users WHERE id = {}".format(i, id)).fetchone()})
		return data
	conn.close()

def azino(id, sum, vin):
	with sqlite3.connect("./data/DB/database.db") as conn:
		cursor = conn.cursor()
		for row in cursor.execute(f"SELECT money FROM users WHERE id = {id}"):
			if vin == 1:
				cursor.execute("UPDATE users SET money = ? WHERE id = ?", (row[0] + sum * 2, id))
			else:
				cursor.execute("UPDATE users SET money = ? WHERE id = ?", (row[0] - sum, id))
	conn.close()

def pays(id, id_2, num):
	with sqlite3.connect("./data/DB/database.db") as conn:
		cursor = conn.cursor()
		for row in cursor.execute(f"SELECT money FROM users WHERE id = {id}"):
			cursor.execute("UPDATE users SET money = ? WHERE id = ?", (row[0] - num, id))
		for row in cursor.execute(f"SELECT money FROM users WHERE id = {id_2}"):
			cursor.execute("UPDATE users SET money = ? WHERE id = ?", (row[0] + num, id_2))
	conn.close()

def up(id, num):
	with sqlite3.connect("./data/DB/database.db") as conn:
		cursor = conn.cursor()
		for row in cursor.execute(f"SELECT money FROM users WHERE id = {id}"):
			cursor.execute("UPDATE users SET money = ? WHERE id = ?", (row[0] + num, id))
	conn.close()
