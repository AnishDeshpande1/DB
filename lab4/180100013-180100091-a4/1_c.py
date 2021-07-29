import psycopg2, config
import time
def connect():
    """ returns connection to database """
    # TODO: use variables from config file as connection params
    conn = psycopg2.connect(dbname=config.name,user=config.user, password=config.pswd, host=config.host, port=config.port)
    #print("connected successfully")
    # conn = psycopg2.connect(....)
    return conn

def exec_query(conn, sql):
    """ Executes sql query and returns header and rows """
    # TODO: create cursor, get header from cursor.description, and execute query to fetch rows.
    cur = conn.cursor()
    #print("cursor made")
    #print(cur)
    try:
        cur.execute(sql)
        conn.commit()
        #print("successfully exectued and committed")
    except:
        print("Some execution error")
        conn.rollback()

if __name__ == "__main__":
	import config
	query_clean = '''delete from covid'''
	query_insert = '''copy covid FROM '/home/atothed/Desktop/DB/lab4/archive/data1.csv' 
				DELIMITER ',' CSV;'''
	try:
		conn = connect()
	except:
		print("Connection error")
	exec_query(conn,query_clean)
	start = time.time()
	exec_query(conn,query_insert)
	end = time.time()
	print(start,end,end-start)

