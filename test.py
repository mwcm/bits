# -*- coding: utf-8 -*-

import csv, re

txt = open("out.xml", "w")
txt.write("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>")
txt.write("<rdf:RDF \n xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" \n xmlns:skos=\"http://www.w3.org/2004/02/skos/core#\"> \n \n")

with open('data.csv', newline='\n', encoding='utf-8-sig') as f:
	reader = csv.reader(f)
	
	count = 1



	for row in reader:

		txt.write("<skos:Concept>")
		txt.write("entry # " + str(count) +"\n")
		print("entry # " + str(count) +"\n")
		#temp = ", ".join(row)

		i = 0
		for item in row:
			
			
			amp = re.sub(r'&', "and", item).strip()

			if i == 0:
				aeiou = re.sub(r'\n', " ", amp).strip()
				print(aeiou+"\n")
				txt.write(aeiou+"\n")
			elif i == 1:
				aeiou = re.sub(r'\n', " ", amp).strip()
				print("	FRE:  "+aeiou+"\n")
				txt.write("	FRE:  "+aeiou+"\n")
			elif i == 2:
				aeiou = re.sub(r'\n', " ", amp).strip()
				print("	Format:  "+aeiou+"\n")
				txt.write("	Format:  "+aeiou+"\n")
			elif i == 3:
				aeiou = re.sub(r'\n', ", ", amp).strip()
				print("	Drop Down Data EN:  "+aeiou+"\n")
				txt.write("	Drop Down Data EN:  "+aeiou+"\n")
			elif i == 4:
				aeiou = re.sub(r'\n', ", ", amp).strip()
				print("	Drop Down Data FR:  "+aeiou+"\n")
				txt.write("	Drop Down Data FR:  "+aeiou+"\n")
			elif i == 5:
				aeiou = re.sub(r'\n', " ", amp).strip()
				print("	CPNO USED:  "+aeiou+"\n")
				txt.write("	CPNO USED:  "+aeiou+"\n")
			elif i == 6:
				aeiou = re.sub(r'\n', " ", amp).strip()
				print("	eSchool USED:  "+aeiou+"\n")
				txt.write("	eSchool USED:  "+aeiou+"\n")
			elif i == 7:
				aeiou = re.sub(r'\n', " ", amp).strip()
				print("	Design USED:  "+aeiou+"\n")
				txt.write("	Design USED:  "+aeiou+"\n")
			elif i == 8:
				aeiou = re.sub(r'\n', " ", amp).strip()
				print("	OST USED:  "+aeiou+"\n")
				txt.write("	OST USED:  "+aeiou+"\n")
			elif i == 9:
				aeiou = re.sub(r'\n', " ", amp).strip()
				print("	METADATA related to:  "+aeiou+"\n")
				txt.write("	METADATA related to:  "+aeiou+"\n")
			elif i == 10:
				aeiou = re.sub(r'\n', " ", amp).strip()
				print("	Added to protege:  "+aeiou+"\n")
				txt.write("	Added to protege:  "+aeiou+"\n")
			elif i == 11:
				aeiou = re.sub(r'\n', " ", amp).strip()
				print("	Reference:  "+aeiou+"\n")
				txt.write("	Reference:  "+aeiou+"\n")
			else:
				print("ERR OUT OF RANGE")
				txt.write("ERR OUT OF RANGE")
				break

			i = i + 1

		print("\n\n")
		txt.write("\n\n")
		count = count + 1

		txt.write("</skos:Concept>")

txt.write("</rdf:RDF>")
txt.close()