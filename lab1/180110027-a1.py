import csv

'''
with open('csv-files/student.csv', newline='') as csvfile:
    stud = csv.DictReader(csvfile)
    for row in stud:
        strr = ""
        print(row)
        for key, value in row.items(): 
            strr = strr + value + ","
        print(strr[:-1])
'''

# +
#a = "How r u ?"
#a.split(' ')[-1]

# +
#qu1c("select ID, dept_name from student where dept_name = 'Physics';")

# +
#qu2('select * from student, instructor where student.dept_name = instructor.dept_name;')
# -





def qu1a(qu):
    #relat = qu.split(' ')[-1][:-1]
    relat = qu.split()[-1][:-1]
    with open('csv-files/' + relat + '.csv', newline='') as csvfile:
        stud = csv.DictReader(csvfile)
        for row in stud:
            strr = ""
            #print(row)
            for key, value in row.items(): 
                strr = strr + value + ","
            print(strr[:-1])


# +
#qu1b("select * from student where dept_name = 'Comp. Sci.';")
# -

def qu1b(qu):
    relat = qu.split()[3]
    
    after_eq = qu.split('=')[1]
    col = after_eq.strip()[:-1]
    #print(col)
    #return
    #col = qu.split()[-1][:-1]
    
    if(col[0] =="\'"):
        col = col[1:-1]
    col = col.strip()
    #print(col)
    
    col_nm = qu.split('=')[0].split()[-1].strip()
    #print(col_nm)
    
    with open('csv-files/' + relat + '.csv', newline='') as csvfile:
        stud = csv.DictReader(csvfile)
        for row in stud:
            strr = ""
            if(row[col_nm] == col):
                for key, value in row.items(): 
                    strr = strr + value + ","
                print(strr[:-1])


# +
#a = "select from a where c = 'dfg h'"
#a.split()
# -

'''
qu = "select dept_name,   title     ,credits from course where dept_name = 'Biology'"
fro = qu.lower().rfind("from")
to = qu.lower().find("select") + 6

cols = qu[to:fro]
col_list = cols.split(',')
for i in range(len(col_list)):
        if(col_list[i][-1] == ','):
            col_list[i] = col_list[i][:-1]
        col_list[i] = col_list[i].strip()

print(col_list)
'''



# +
def qu1c(qu):
    from_ind = qu.split().index('from')
    relat = qu.split()[from_ind+1]
    
    '''
    col = qu.split()[-1][:-1]
    if(col[0] =="\'"):
        col = col[1:-1]
    '''
    
    after_eq = qu.split('=')[1]
    col = after_eq.strip()[:-1]
    #print(col)
    #return
    #col = qu.split()[-1][:-1]
    
    if(col[0] =="\'"):
        col = col[1:-1]
    col = col.strip()
    
    #col_nm = qu.split()[-3]
    col_nm = qu.split('=')[0].split()[-1].strip()
    
    #col_list = qu.split(' ')[1: from_ind]
    #print(col_list)
    
    fro = qu.lower().rfind("from")
    to = qu.lower().find("select") + 6

    cols = qu[to:fro]
    col_list = cols.split(',')
    
    for i in range(len(col_list)):
        if(col_list[i][-1] == ','):
            col_list[i] = col_list[i][:-1]
        col_list[i] = col_list[i].strip()
            
    #print(col_list)
    
    with open('csv-files/' + relat + '.csv', newline='') as csvfile:
        stud = csv.DictReader(csvfile)
        for row in stud:
            strr = ""
            if(row[col_nm] == col):
                for i in col_list:
                    strr = strr + row[i] + ","
                    
                print(strr[:-1])
            
    
    
# -


def qu2(qu):
    rel_col1 = qu.split()[-3]
    rel_col2 = qu.split()[-1][:-1]
    rel1 = rel_col1.split('.')[0]
    rel2 = rel_col2.split('.')[0]
    col1 = rel_col1.split('.')[1]
    col2 = rel_col2.split('.')[1]


    with open('csv-files/' + rel1 + '.csv', newline='') as csvfile1:
        stud1 = csv.DictReader(csvfile1)

        for row1 in stud1:
            #print("A")
            with open('csv-files/' + rel2 + '.csv', newline='') as csvfile2:
                stud2 = csv.DictReader(csvfile2)
                
                for row2 in stud2: 
                    strr = ""
                        
                    if(row1[col1] == row2[col2]):
                        #print("HI")
                        for key, value in row1.items(): 
                            strr = strr + value + ","
                        for key, value in row2.items(): 
                            strr = strr + value + ","
                            
                        print(strr[:-1])



# +
#qu2('select * from student, instructor where student.dept_name = instructor.dept_name;')
# -

def qu3(qu):
    relat = qu.split()[3]
    
    '''
    col = qu.split()[-1][:-1]
    if(col[0] =="\'"):
        col = col[1:-1]
    col_nm = qu.split()[-3]
    '''
    after_eq = qu.split('=')[1]
    col = after_eq.strip()[:-1]
    #print(col)
    #return
    #col = qu.split()[-1][:-1]
    
    if(col[0] =="\'"):
        col = col[1:-1]
    col = col.strip()
    #print(col)
    
    col_nm = qu.split('=')[0].split()[-1].strip()
    #print(col_nm)
    
    
    count = 0
    
    with open('csv-files/' + relat + '.csv', newline='') as csvfile:
        stud = csv.DictReader(csvfile)
        for row in stud:
            #strr = ""
            if(row[col_nm] == col):
                count = count + 1
                #print(strr[:-1])
        print(count)


def qu4_help(qu):
    '''
    relat = qu.split()[-5]
    col = qu.split()[-1]
    if(col[0] =="\'"):
        col = col[1:-1]
    col_nm = qu.split()[-3]
    '''
    relat = qu.split()[3]
    
    after_eq = qu.split('=')[1]
    col = after_eq.strip()
    #print(col)
    #return
    #col = qu.split()[-1][:-1]
    
    if(col[0] =="\'"):
        col = col[1:-1]
    col = col.strip()
    #print(col)
    
    col_nm = qu.split('=')[0].split()[-1].strip()
    #print(col_nm)
    
    col_tak = qu.split()[1]
        
    #print(col_list)
    
    with open('csv-files/' + relat + '.csv', newline='') as csvfile:
        stud = csv.DictReader(csvfile)
        l = []
        for row in stud:
            if(row[col_nm] == col):
                if(row[col_tak] not in l):
                    l.append(row[col_tak])
                    
    
    return l


def qu4a(qu):
    qu1 = qu.split('intersect')[0][1:]
    qu1 = qu1.strip()
    qu1 = qu1[:-1]
    qu1 = qu1.strip()
    
    qu2 = qu.split('intersect')[1][:-2]
    qu2 = qu2.strip()
    qu2 = qu2[1:]
    qu2 = qu2.strip()
    
    l1 = qu4_help(qu1)
    l2 = qu4_help(qu2)
    
    #print(qu1)
    #print(qu2)
    
    for i in l1:
        if i in l2:
            print(i)



# +
#qu4a("(select course_id from section where semester = 'Fall'   )    intersect    (   select course_id from section where year = 2009);")
# -

def qu4b(qu):
    #qu1 = qu.split(') union (')[0][1:]
    #qu2 = qu.split(') union (')[1][:-2]
    qu1 = qu.split('union')[0][1:]
    qu1 = qu1.strip()
    qu1 = qu1[:-1]
    qu1 = qu1.strip()
    
    qu2 = qu.split('union')[1][:-2]
    qu2 = qu2.strip()
    qu2 = qu2[1:]
    qu2 = qu2.strip()
    
    l1 = qu4_help(qu1)
    l2 = qu4_help(qu2)
    
    #print(l1)
    #print(l2)
    #print(qu1)
    #print(qu2)
    
    l = []
    
    for i in l1:
        print(i)
    
    for i in l2:
        if i not in l1:
            print(i)


a = "I  am gawd  "
a = a[:-1]
#a.strip()
a





# +
while(True):
    typ = input("Query Type? ")
    if(typ == "0"):
        print("exiting...")
        exit(0)
        
    qu = input("Enter your query: ")
    qu = qu.strip()
    if(qu[-1] == ';'):
        qu = qu[:-1]
    
    qu = qu.strip()
    #if(qu[-1] != ';'):
    qu = qu + ";"
    
    #print(qu)
    
    if(typ == "1a"):
        qu1a(qu)
    elif(typ == "1b"):
        qu1b(qu)
    elif(typ == "1c"):
        qu1c(qu)
    elif(typ == "2"):
        qu2(qu)
    elif(typ == "3"):
        qu3(qu)
    elif(typ == "4a"):
        qu4a(qu)
    elif(typ == "4b"):
        qu4b(qu)
    
    
    
# -








