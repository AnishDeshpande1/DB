import csv

txt = "text"
struser = "CREATE (:User {name:\"%s\"});\n"
strtweet = "CREATE (:Tweet {%s:\"%s\"});\n"
strhashtag = "CREATE (:Hashtag {tag:\"%s\"});\n" 
strfollows = "MATCH (u1: User {name:\"%s\"}), (u2: User {name:\"%s\"}) CREATE (u1)-[:Follows]->(u2);\n"
strcontains = "MATCH (t: Tweet {text:\"%s\"}), (h: Hashtag {tag:\"%s\"}) CREATE (t)-[:Contains]->(h);\n"
strmentions = "MATCH (t: Tweet {text:\"%s\"}), (u: User {name:\"%s\"}) CREATE (t)-[:Mentions]->(u);\n"
strsent = "MATCH (u: User {name:\"%s\"}), (t: Tweet {text:\"%s\"}) CREATE (u)-[:Sent]->(t);\n"

users = {}
hashtags = {}
tweets = {}

with open("load-data.cypher", 'w') as of:
	with open("users.csv") as file:
		csvreader = csv.reader(file)
		l = 0
		for row in csvreader:
			if l==0:
				l = l + 1
			else:
				s = str(row[1])
				users[row[0]] = s
				of.write(struser%(s))

	with open("tweets.csv") as file:
		csvreader = csv.reader(file)
		l = 0
		for row in csvreader:
			if l==0:
				l = l + 1
			else:
				s = str(row[1])
				tweets[row[0]] = s
				of.write(strtweet%(txt,s))

	with open("hashtags.csv") as file:
		csvreader = csv.reader(file)
		l = 0
		for row in csvreader:
			if l==0:
				l = l + 1
			else:
				s = str(row[1])
				hashtags[row[0]] = s
				of.write(strhashtag%(s))

	with open("follows.csv") as file:
		csvreader = csv.reader(file)
		l = 0
		for row in csvreader:
			if l==0:
				l = l + 1
			else:
				s1 = str(users[row[0]])
				s2 = str(users[row[1]])
				of.write(strfollows%(s1,s2))

	with open("contains.csv") as file:
		csvreader = csv.reader(file)
		l = 0
		for row in csvreader:
			if l==0:
				l = l + 1
			else:
				s1 = str(tweets[row[0]])
				s2 = str(hashtags[row[1]])
				of.write(strcontains%(s1,s2))

	with open("mentions.csv") as file:
		csvreader = csv.reader(file)
		l = 0
		for row in csvreader:
			if l==0:
				l = l + 1
			else:
				s1 = str(tweets[row[0]])
				s2 = str(users[row[1]])
				of.write(strmentions%(s1,s2))

	with open("sent.csv") as file:
		csvreader = csv.reader(file)
		l = 0
		for row in csvreader:
			if l==0:
				l = l + 1
			else:
				s1 = str(users[row[0]])
				s2 = str(tweets[row[1]])
				of.write(strsent%(s1,s2))




