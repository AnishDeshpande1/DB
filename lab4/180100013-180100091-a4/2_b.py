import psycopg2, config, time
import matplotlib.pyplot as plt 
import numpy as np
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
    from sys import argv
    import config, random
    
    try:
        conn = connect()
        cursor = conn.cursor(name="large")
        sql = "select * from covid"
        cursor.execute(sql)
        row = 0
        limit = 100
        ite = 1
        x = [] 
        y = []
        glob_time = time.time()
        while ite<1000:
            
            tim = time.time()
             
            rows = cursor.fetchmany(limit)
            if not rows:
                break
            tim = time.time() - tim
            x.append(ite)
            y.append(tim)
            row+=limit
            ite+=1
        glob_time = time.time() - glob_time
        print(glob_time)
        plt.figure(figsize=(5,5))
        plt.plot(x, y) 
        plt.yticks(np.arange(float('%.3f'%min(y)), float('%.3f'%(max(y)+0.01)), 0.005))
        y = [str('%.3f'%t)+"s" for t in y]
          
        # naming the x axis 
        plt.xlabel('query') 
        # naming the y axis 
        plt.ylabel('time') 

        plt.title('Execution time!') 

        plt.savefig("2b.png")
        conn.close()
    except Exception as err:
        print("ERROR %%%%%%%%%%%%%%%% \n", err)