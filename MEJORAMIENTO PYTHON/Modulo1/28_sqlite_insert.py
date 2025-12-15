import sqlite3
c=sqlite3.connect("bd.db"); cur=c.cursor(); cur.execute("INSERT INTO t VALUES (1)"); c.commit(); c.close()