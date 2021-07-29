import csv

output_file = 'ipl-data.sql'
filenames = ['team','venue','player','match','ball_by_ball','player_match']
relation = 'team'
relations = {}

sql1 = 'insert into '
sql2 = ' values ('
sql3 = ');\n'
sql4 = 'delete from '
sql5 = ';\n'
with open(output_file,'w') as opfile:
	for item in reversed(filenames):
		opfile.write(sql4+item+sql5)

	for relation in filenames:
		with open(relation+'.csv','r') as file:
			reader = csv.DictReader(file)
			for tupple in reader:
				q = ""
				for _,val in tupple.items():
					if(val=='NULL'):
						q+= 'null,'
					else:
						q+= "\'"+val+"\',"
				query = sql1 + relation + sql2 + q[:-1] + sql3
				opfile.write(query)




