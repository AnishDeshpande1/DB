import psycopg2, config
import random
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
    
def fetch_value(conn,n):
    cur = conn.cursor()
    query1 = "SELECT hex_string FROM oracle WHERE int_col = %s;"
    #query2 = "SELECT count(*) FROM oracle WHERE intcol = "+str(n)+";"
    try:
        cur.execute(query1,[n])
        conn.commit()
    except:
        print("some query execution/commit error while fetching output")
        conn.rollback()
    ans = cur.fetchall()
    for row in ans:
        s = row[0]
        break
    return s
    
def generate_string():
    stri = ""
    for i in range(64):
        stri = stri + random.sample(set('0123456789abcdef'), 1)[0]
    return stri

hexset = set([])
def populate_table(conn,n):
    cur = conn.cursor()
    query = """INSERT INTO oracle VALUES (%s,%s);"""
    s = generate_string()
    while(s in hexset):
        s = generate_string()
    hexset.add(s)
    cur.execute(query,[n,s])
    conn.commit()
        #print(query)




if __name__ == "__main__":
    import config

    try:
        conn = connect()
    except:
        print("Connection error")
    q = """DROP TABLE IF EXISTS oracle;"""
    exec_query(conn,q)
    create_table_query = """
            CREATE TABLE IF NOT EXISTS oracle(
                int_col INT not null,
                hex_string varchar(257),
                PRIMARY KEY (int_col));
             """
    exec_query(conn,create_table_query)
    #print("table created")
    
    numset = set([])
    
    while(True):
        print("Query:")
        try:
            n = int(input())
        except:
            print("Error in input, try again")
        if(n==-1):
            print("exiting...")
            break
        else:
            if(n not in numset):
                numset.add(n)
                populate_table(conn,n)
                #print("successfully populated with ",n)
            s = fetch_value(conn,n)
            print(s)
    conn.close()