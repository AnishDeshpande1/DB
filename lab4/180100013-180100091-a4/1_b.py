import csv
sql_files = ['insert_data1','insert_data2','insert_data3','insert_data4','insert_data5']
input_csvs = ['data1','data2','data3','data4','data5']

sql_files2 = ['insert_data6','insert_data7','insert_data8','insert_data9','insert_data10']
input_csvs2 = ['data6','data7','data8','data9','data10']


for i in range(5):
	with open(sql_files[i] + '.sql', 'w') as o_file:
		with open(input_csvs[i] + '.csv', 'r') as i_file:
			file = csv.DictReader(i_file)
			query = "insert into covid values ("
			for row in file:
				q = query
				for _,val in row.items():
					if(val == 'NULL'):
						q = q + 'null,'
					else:
						q = q + '\'' + val + '\','
				q = q[:len(q)-1] + ');'
				print(q,file = o_file)



