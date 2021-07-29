import psycopg2, config, time
import matplotlib.pyplot as plt 
import csv

def connect():
    """ returns connection to database """
    # TODO: use variables from config file as connection params
    # conn = psycopg2.connect(....)
    # return conn
    conn = psycopg2.connect(
    host=config.host,
    database=config.name,
    user=config.user,
    password=config.pswd,
    port=config.port)
    return conn





if __name__ == "__main__":

	for i in range(1,6):
		filename = "data"+str(i)+".csv"
		conn = connect()
		cursor = conn.cursor()

		sql = "insert into covid values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
		with open(filename,'r') as csv_file:
			file = csv.DictReader(csv_file)
			query = "insert into covid values ("
			tim = time.time()
			for row in file:
				q = query
				for _,val in row.items():
					if(val == 'NULL'):
						q = q + 'null,'
					else:
						q = q + '\'' + val + '\','
				q = q[:len(q)-1] + ');'
				cursor.execute(q)
			tim = time.time() - tim
			print(tim)
	conn.close()
	
	
    