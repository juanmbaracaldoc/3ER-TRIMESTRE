import sqlite3
c=sqlite3.connect("bd.db"); cur=c.cursor(); cur.execute("CREATE TABLE IF NOT EXISTS t(a)"); c.commit(); c.close()