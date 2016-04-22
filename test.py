# -*- coding: utf-8 -*-

import csv, re

txt = open("out.xml", "w")
txt.write("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>")
txt.write("<rdf:RDF \n xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" \n xmlns:skos=\"http://www.w3.org/2004/02/skos/core#\"> \n \n")


txt.write("<skos:conceptScheme rdf:about=\"http://www.thesaurus.gc.ca/#CoreSubjectThesaurus\"></skos:conceptScheme>\n\n")



with open('data.csv', newline='\n', encoding='utf-8-sig') as q:
	reader = csv.reader(q)

	formatList = []
	enPossibleList = []
	frPossibleList = []
	metadataList = []

	for row in reader:
		j = 0
		for item in row:
			amp = re.sub(r'&', "and", item).strip()

			
			if j == 2:  #FORMAT

				if amp not in formatList:
					formatList.append(amp)
					txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#"+amp+"\">")
					txt.write("<skos:prefLabel>"+amp+" </skos:prefLabel> </skos:concept>")

			elif j == 3: #DROP DOWN OPTIONS EN
				#FOR EACH NEW LINE SEPERATED VALUE IN AMP .....
				if amp not in enPossibleList :
					enPossibleList.append(amp)
					txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#"+amp+"\">")
					txt.write("<skos:prefLabel>"+amp+" </skos:prefLabel> </skos:concept>")
				

				#FOR EACH NEW LINE SEPERATED VALUE IN AMP .....

			elif j == 4:  #DROP DOWN OPTIONS FR
				#FOR EACH NEW LINE SEPERATED VALUE IN AMP .....
				if amp not in frPossibleList :
					frPossibleList.append(amp)
					txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#"+amp+"\">")
					txt.write("<skos:prefLabel>"+amp+" </skos:prefLabel> </skos:concept>")
				
			elif j == 9:	#METADATA
				#FOR EACH NEW LINE SEPERATED VALUE IN AMP .....
				if amp not in metadataList :
					metadataList.append(amp)
					txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#"+amp+"\">")
					txt.write("<skos:prefLabel>"+amp+" </skos:prefLabel> </skos:concept>")
				

			else:
				#do nothing

				j = j + 1


txt.write("\n \n END OF format / drop down options / metadata \n \n ")


with open('data.csv', newline='\n', encoding='utf-8-sig') as f:
	reader = csv.reader(f)
	for row in reader:

		txt.write("<skos:Concept>")

		i = 0
		for item in row:
			
			amp = re.sub(r'&', "and", item).strip()

			if i == 0:
				aeiou = re.sub(r'\n', " ", amp).strip()
				print(aeiou+"\n")
				txt.write(aeiou+"\n")
			
			elif i == 1:
				aeiou = re.sub(r'\n', " ", amp).strip()
				print("<skos:prefLabel xml:lang=\"fr\">"+aeiou+"</skos:prefLabel>\n")
				txt.write("<skos:prefLabel xml:lang=\"fr\">"+aeiou+"</skos:prefLabel>\n")
			
			elif i == 2:
				#REFERENCE VALUES CREATED IN 1ST SECTION
				aeiou = re.sub(r'\n', " ", amp).strip()
				print("<skos:note>"+aeiou+"</skos:note>\n")
				txt.write("<skos:note>"+aeiou+"</skos:note>\n")

			elif i == 3:
				#REFERENCE VALUES CREATED IN 1ST SECTION
					break

			elif i == 4:
				#REFERENCE VALUES CREATED IN 1ST SECTION
					break
			
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
				#REFERENCE VALUES CREATED IN 1ST SECTION
				break

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
				break

			i = i + 1

		print("\n\n")
		txt.write("\n")

		txt.write("</skos:Concept>")


		txt.write("\n\n")

txt.write("</rdf:RDF>") 
txt.close()