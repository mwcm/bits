#tsb2xml.py
#morgan mitchell
#May 5th 2016
# -*- coding: utf-8 -*-

import re, sys, os


#variables for file paths
endata = sys.argv[1]
frdata = sys.argv[2]
outfile = sys.argv[3]


#arrays for titles and definitions of each concept
titles = []
definitions = [] 
frtitles = []
frdefinitions = [] 

#array to hold english titles corresponding to french list
#necessary due to both lists being un ordered
frtoe = []

out = open(outfile, "w")
out.write("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>")
out.write("<rdf:RDF \n xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" \n xmlns:skos=\"http://www.w3.org/2004/02/skos/core#\" \n xmlns:dc=\"http://purl.org/dc/elements/1.1/\"> \n \n")


#define our conceptScheme
out.write("<skos:conceptScheme rdf:about=\"http://www.thesaurus.gc.ca/#CoreSubjectThesaurus\"></skos:conceptScheme>\n\n")


out.write("\n \n \n")


with open(endata, newline='\n', encoding='utf-8-sig') as e:

	content = str(e.readlines())

	content = content.rpartition('</a>Appendix A - Definitions</h2>')[-1]
	content = content.rpartition('</details>')[0]
	#cut content up to occurence of </a>Appendix A - Definitions</h2>  </summary>

	for item in content.split("</dd>"):
		t = item.rpartition('<strong>')[-1]
		t = t.rpartition('</strong>')[0]
		t = t.strip()

		d = item.rpartition('<dd>')[-1]
		d = re.sub('<[^>]+>', '', d)
		d = d.strip()

		if t:
			titles.append(t)

		if d and "\\r\\n" not in d:
			definitions.append(d)

with open(frdata, newline='\n', encoding='utf-8-sig') as f:

	content = str(f.readlines())

	#cut content up to occurence of </a>Appendix A - Definitions</h2>  </summary>
	content = content.rpartition('</a>Annexe A - Définitions</h2>')[-1]
	content = content.rpartition('</details>')[0]

	for item in content.split("</dd>"):
		t = item.rpartition('<strong>')[-1]
		t = t.partition('</em>')[0]

		et = t.rpartition('<em>')[-1]
		et = re.sub('<[^>]+>', '', et)
		et = et.strip()

		if et[0].isalpha():
			frtoe.append(et)

		t = t.rpartition('</strong>')[0]
		t = t.strip()

		d = item.rpartition('<dd>')[-1]
		d = re.sub('<[^>]+>', '', d)
		d = d.strip()

		if t:
			frtitles.append(t)
			
		if d and "\\r\\n" not in d:
			frdefinitions.append(d)


#print(frtoe)
print(titles)
print(frtitles)

newENTitleArray = []
newENDefinitionArray = []
a = 0
for item in frtoe:


	b = 0
	for title in titles:
		print(frtoe[a] +"         "+titles[b]+"\n\n\n")
		if frtoe[a].lower() == titles[b].lower():
			newENTitleArray.append(titles[b])
			newENDefinitionArray.append(definitions[b])
			titles.remove(titles[b])
			definitions.remove(definitions[b])

		b = b +1
	a = a + 1

#newENTitleArray.append(titles)

c = 0
for item in newENTitleArray:
	out.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#"+newENTitleArray[c].replace(" ","%20")+"\"> \n"+
                            "<skos:prefLabel xml:lang=\"fr\">"+frtitles[c]+" </skos:prefLabel> \n"+
                            "<skos:prefLabel xml:lang=\"en\">" +newENTitleArray[c]+" </skos:prefLabel> \n"+
                            "<skos:scopeNote xml:lang=\"fr\">"+frdefinitions[c]+"</skos:scopeNote> \n"+
                            "<skos:scopeNote xml:lang=\"en\">"+newENDefinitionArray[c]+"</skos:scopeNote> \n"+
                            "<skos:references> TSB </skos:references>"+"\n"
                            "</skos:concept> \n\n")
	c = c + 1


out.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#Validate\"> \n"+
                            "<skos:prefLabel xml:lang=\"fr\">Validé</skos:prefLabel> \n"+
                            "<skos:prefLabel xml:lang=\"en\">Validate</skos:prefLabel> \n"+
                            "<skos:scopeNote xml:lang=\"fr\">un moyen de confirmer qu'une personne possède les connaissances.</skos:scopeNote> \n"+
                            "<skos:scopeNote xml:lang=\"en\">means of confirming that an individual possesses the knowledge.</skos:scopeNote> \n"+
                            "<skos:references> TSB </skos:references>"+"\n"
                            "</skos:concept> \n\n")


#close file
out.write("</rdf:RDF>")
out.close()