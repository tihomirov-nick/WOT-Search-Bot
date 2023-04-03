import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('WOT.db')
    cur = base.cursor()


async def get_all_users():
    return cur.execute("SELECT * FROM users").fetchall()


async def get_stream_count():
    return cur.execute("SELECT counter FROM streams").fetchall()[0][0]


async def get_social_count():
    return cur.execute("SELECT counter FROM social").fetchall()[0][0]


async def add_streams():
    cur.execute("UPDATE streams SET counter = counter + 1")
    base.commit()


async def add_social():
    cur.execute("UPDATE social SET counter = counter + 1")
    base.commit()


async def add_user(user_id):
    cur.execute("INSERT INTO users(user_id) VALUES(?)", (user_id,))
    base.commit()


async def search_name(Nation, Level, Type):
    return cur.execute("SELECT * FROM tanks WHERE Nation == ? and Level == ? and Type == ?", (Nation, Level, Type,)).fetchall()

async def search_description(name):
    return cur.execute("SELECT Description FROM tanks WHERE name == ?", (name,)).fetchall()[0][0]

async def search_photo(name):
    return cur.execute("SELECT Photo FROM tanks WHERE name == ?", (name,)).fetchall()[0][0]

async def get_all_types(Nation, Level):
    return cur.execute("SELECT * FROM tanks WHERE Nation == ? and Level == ?", (Nation, Level,)).fetchall()
