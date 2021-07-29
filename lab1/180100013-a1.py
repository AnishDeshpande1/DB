import csv
#READ ALL DATA ON BOOTUP, STORE IN 'relations' dictionary
relations = {}

with open('csv-files/advisor.csv','r') as file:
	reader = csv.reader(file)
	table = []
	for row in reader:
		table.append(row)
	relations['advisor'] = table

with open('csv-files/classroom.csv','r') as file:
	reader = csv.reader(file)
	table = []
	for row in reader:
		table.append(row)
	relations['classroom'] = table

with open('csv-files/course.csv','r') as file:
	reader = csv.reader(file)
	table = []
	for row in reader:
		table.append(row)
	relations['course'] = table

with open('csv-files/department.csv','r') as file:
	reader = csv.reader(file)
	table = []
	for row in reader:
		table.append(row)
	relations['department'] = table

with open('csv-files/instructor.csv','r') as file:
	reader = csv.reader(file)
	table = []
	for row in reader:
		table.append(row)
	relations['instructor'] = table

with open('csv-files/prereq.csv','r') as file:
	reader = csv.reader(file)
	table = []
	for row in reader:
		table.append(row)
	relations['prereq'] = table

with open('csv-files/section.csv','r') as file:
	reader = csv.reader(file)
	table = []
	for row in reader:
		table.append(row)
	relations['section'] = table

with open('csv-files/student.csv','r') as file:
	reader = csv.reader(file)
	table = []
	for row in reader:
		table.append(row)
	relations['student'] = table

with open('csv-files/takes.csv','r') as file:
	reader = csv.reader(file)
	table = []
	for row in reader:
		table.append(row)
	relations['takes'] = table

with open('csv-files/teaches.csv','r') as file:
	reader = csv.reader(file)
	table = []
	for row in reader:
		table.append(row)
	relations['teaches'] = table

with open('csv-files/time_slot.csv','r') as file:
	reader = csv.reader(file)
	table = []
	for row in reader:
		table.append(row)
	relations['time_slot'] = table
###############################################################
#Now, we begin the query loop.

q_type = ""
while(True):
	q_type = input("Query Type? ").strip()
	n = q_type[0]

	if(n=='0'):
		print("exiting...")
		break

	elif(n=='1'):
		if(len(q_type)==1):
			print("specify further.")
			continue
		char = q_type[1]
		query = input("Enter your query: ")
		query = query.replace(";","").strip()
		if(char == 'a'):
			r_name = query.split("from")[1]
			r_name = r_name.strip()
			data = relations[r_name]
			for row in data[1:]:
				print(*row,sep=',')
		elif(char == 'b'):
			start = "from"
			end = "where"
			r_name = query[query.find(start)+len(start):query.rfind(end)].strip()
			start = "where"
			condn = query[query.find(start)+len(start):].strip()
			col,val = condn.split("=")
			col = col.strip()
			val = val.replace("'","").strip()
			data = relations[r_name]
			idx = data[0].index(col)
			for row in data[1:]:
				if(row[idx]==val):
					print(*row,sep=',')
		elif(char=='c'):
			start = "from "
			end = "where"
			r_name = query[query.find(start)+len(start):query.rfind(end)].strip()
			start = "where "
			condn = query[query.find(start)+len(start):]
			start = "select"
			end = "from"
			columns = query[query.find(start)+len(start):query.rfind(end)]
			columns = columns.replace(" ","").split(',')
			col,val = condn.split("=")
			col = col.strip()
			val = val.replace("'","").strip()
			data = relations[r_name]
			idx = data[0].index(col)
			indices = []
			for c in columns:
				indices.append(data[0].index(c))
			for row in data[1:]:
				if(row[idx]==val):
					out = [row[i] for i in indices]
					print(*out, sep =',')
		else:
			print("Invalid query type")


	elif(n=='2'):
		query = input("Enter your query: ").replace(";","").strip()
		start = "from"
		end = "where"
		rel1,rel2 = query[query.find(start)+len(start):query.rfind(end)].replace(" ","").split(",")
		start = "where"
		condns = query[query.find(start)+len(start):].split("=")
		if(condns[0].find(rel1) != -1):
			col1 = condns[0].split(".")[1].strip()
			col2 = condns[1].split(".")[1].strip()
		else:
			col1 = condns[1].split(".")[1].strip()
			col2 = condns[0].split(".")[1].strip()
		data1 = relations[rel1]
		data2 = relations[rel2]
		idx1 = data1[0].index(col1)
		idx2 = data2[0].index(col2)
		for row1 in data1[1:]:
			for row2 in data2[1:]:
				if(row1[idx1]==row2[idx2]):
					print(*(row1 + row2), sep = ",")

	elif(n=='3'):
		query = input("Enter your query: ").replace(";","").strip()
		start = "from"
		end = "where"
		r_name = query[query.find(start)+len(start):query.rfind(end)].strip()
		start = "where"
		condn = query[query.find(start)+len(start):]
		col,val = condn.split("=")
		col = col.strip()
		val = val.replace("'","").strip()
		data = relations[r_name]
		idx = data[0].index(col)
		count = 0
		for row in data[1:]:
			if(row[idx]==val):
				count+=1
		print(count)

	elif(n=='4'):
		char = q_type[1]
		query = input("Enter your query: ").replace(";","").strip()
		if(char=='a'):
			query1,query2 = query.split('intersect') 
		elif(char=='b'):
			query1,query2 = query.split('union')		
		else:
			print("Invalid query type")
			continue
		start = "("
		end = ")"
		query1 = query1[query1.find(start)+len(start):query1.rfind(end)].strip()
		query2 = query2[query2.find(start)+len(start):query2.rfind(end)].strip()

		start = "from"
		end = "where"
		rel1 = query1[query1.find(start)+len(start):query1.rfind(end)].strip()
		rel2 = query2[query2.find(start)+len(start):query2.rfind(end)].strip()

		start = "where"
		condn1 = query1[query1.find(start)+len(start):]
		condn2 = query2[query2.find(start)+len(start):]

		col1,val1 = condn1.split("=")
		col1 = col1.strip()
		val1 = val1.replace("'","").strip()
		data1 = relations[rel1]
		idx1 = data1[0].index(col1)
		col2,val2 = condn2.split("=")
		col2 = col2.strip()
		val2 = val2.replace("'","").strip()
		data2 = relations[rel2]
		idx2 = data2[0].index(col2)

		start = "select"
		end = "from"
		op_col1 = query1[query1.find(start)+len(start):query1.rfind(end)].strip()
		op_idx1 = data1[0].index(op_col1)
		op_col2 = query2[query2.find(start)+len(start):query2.rfind(end)].strip()
		op_idx2 = data2[0].index(op_col2)

		op1 = []
		for row in data1[1:]:
			if(row[idx1]==val1):
				if(row[op_idx1] not in op1):
					op1.append(row[op_idx1])
		op2 = []
		for row in data2[1:]:
			if(row[idx2]==val2):
				if(row[op_idx2] not in op2):
					op2.append(row[op_idx2])
		op = []
		if(char == 'a'):
			for item in op1:
				if(item in op2):
					op.append(item)
		else:
			op = op1
			for item in op2:
				if(item not in op):
					op.append(item)

		for elem in op:
			print(elem)

	else:
		print("Invalid Query")




