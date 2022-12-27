import sqlite3 as sqlt

db_name = 'users.db'


def start_db():
    with sqlt.connect(db_name) as base:
        base.execute('CREATE TABLE IF NOT EXISTS "users" ("id"	INTEGER NOT NULL UNIQUE,'
                     '"user"   INTEGER,'
                     'PRIMARY KEY("id" AUTOINCREMENT))')
        base.execute('CREATE TABLE IF NOT EXISTS "message" ("message_id"   INTEGER,'
                     '"chat_id"	    INTEGER)')
        base.commit()


def add_user_db(user_id):
    with sqlt.connect(db_name) as base:
        cur = base.cursor()
        user_id = int(user_id)
        cur.execute('INSERT INTO users VALUES (null, ?)', (user_id, ))
        base.commit()



def add_message(message_id, chat_id):
    with sqlt.connect(db_name) as base:
        cur = base.cursor()
        cur.execute('DELETE from message')
        cur.execute('INSERT INTO message VALUES (?, ?)', (message_id, chat_id))
        base.commit()


def select_message():
    with sqlt.connect(db_name) as base:
        cur = base.cursor()
        m = cur.execute('SELECT * from message').fetchone()
        message = list()
        for i in m:
            message.append(i)
        return message


def all_user():
    with sqlt.connect(db_name) as base:
        cur = base.cursor()
        all_user = cur.execute('SELECT * from users').fetchall()
        lst = list()
        for i in all_user:
            lst.append(int(i[1]))
        return lst