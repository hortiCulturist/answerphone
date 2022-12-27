import sqlite3 as sqlt

db_name = 'users.db'


def start_db():
    base = sqlt.connect(db_name)
    base.execute('CREATE TABLE IF NOT EXISTS "users" ("id"	INTEGER NOT NULL UNIQUE,'
                 '"user"   INTEGER,'
                 'PRIMARY KEY("id" AUTOINCREMENT))')
    base.execute('CREATE TABLE IF NOT EXISTS "message" ("message_id"   INTEGER,'
                 '"chat_id"	    INTEGER)')
    base.commit()


def add_user_db(user_id):
    base = sqlt.connect(db_name)
    cur = base.cursor()
    user_id = int(user_id)
    cur.execute('INSERT INTO users VALUES (null, ?)', (user_id, ))
    base.commit()
    base.close()


def add_message(message_id, chat_id):
    base = sqlt.connect(db_name)
    cur = base.cursor()
    cur.execute('DELETE from message')
    cur.execute('INSERT INTO message VALUES (?, ?)', (message_id, chat_id))
    base.commit()
    base.close()


def select_message():
    base = sqlt.connect(db_name)
    cur = base.cursor()
    m = cur.execute('SELECT * from message').fetchone()
    message = list()
    print(m)
    for i in m:
        message.append(i)
    base.close()
    print(message)
    return message


def all_user():
    base = sqlt.connect(db_name)
    cur = base.cursor()
    all_user = cur.execute('SELECT * from users').fetchall()
    lst = list()
    for i in all_user:
        lst.append(int(i[1]))
    base.close()
    return lst