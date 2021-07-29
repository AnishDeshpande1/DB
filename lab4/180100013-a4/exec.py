import psycopg2, config

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
    #print(cur.description)
    
    if( cur is None):
        rows = []
        header = []
    else:
        rows = [row for row in cur]
        header = [desc[0] for desc in cur.description]
    return (header, rows)

    pass

if __name__ == "__main__":
    from sys import argv
    import config

    query = argv[1]
    try:
        conn = connect()
        #print(conn)
        (header, rows) = exec_query(conn, query)
        print(",".join([str(i) for i in header]))
        for r in rows:
            print(",".join([str(i) for i in r]))
        conn.close()
    except Exception as err:
        print("ERROR %%%%%%%%%%%%%%%% \n", err)
