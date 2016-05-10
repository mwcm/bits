#tsb2xml.py
#morgan mitchell
#May 5th 2016
# -*- coding: utf-8 -*-

import re, sys, os


# variables for file paths
endata = sys.argv[1]
frdata = sys.argv[2]
outfile = sys.argv[3]


# arrays for titles and definitions of each concept
titles = []
definitions = [] 
frtitles = []
frdefinitions = [] 

# array to hold english titles corresponding to french list
# necessary due to both lists being un ordered
# used to match definitions up later
frtoe = []


# define xml and rdf
out = open(outfile, "w")
out.write("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>")
out.write("<rdf:RDF \n xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" \n xmlns:skos=\"http://www.w3.org/2004/02/skos/core#\" \n xmlns:dc=\"http://purl.org/dc/elements/1.1/\"> \n \n")


# define our conceptScheme
out.write("<skos:conceptScheme rdf:about=\"http://www.thesaurus.gc.ca/#CoreSubjectThesaurus\"></skos:conceptScheme>\n\n")


out.write("\n \n \n")

# get english definitions & titles
with open(endata, newline='\n', encoding='utf-8-sig') as e:

	content = str(e.readlines())

	# cut english content down to purely necessary information (the list of definitions)
	content = content.rpartition('</a>Appendix A - Definitions</h2>')[-1]
	content = content.rpartition('</details>')[0]

	# for each definition:
	# -strip the title, put it in an array
	# -strip the definition, put it in another array (if not \r\n, which occurs at the end of list of definitions)
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

	# cut  french content down to purely necessary information (the list of definitions)
	content = content.rpartition('</a>Annexe A - Définitions</h2>')[-1]
	content = content.rpartition('</details>')[0]


	# for each definition:
	# -strip the title, put it in an array
	# -strip the definition, put it in another array (if not \r\n, which occurs at the end of list of definitions
	for item in content.split("</dd>"):
		t = item.rpartition('<strong>')[-1]
		t = t.partition('</em>')[0]


		# strip the French title's corresponding English version
		et = t.rpartition('<em>')[-1]
		et = re.sub('<[^>]+>', '', et)
		et = et.strip()

		# append ENGLISH versions of FRENCH titles to array created earlier
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


# now we must match English definitions with French
# must do this since they're listed on EN/FR web pages in different orders
# therefore, the two definition data files downloaded are not in corresponding order

# so we make new arrays, one for EN titles and one for EN definitions
# these english definitions are compared to  the frtoe array created previously
newENTitleArray = []
newENDefinitionArray = []
a = 0
for item in frtoe:


	# for each item in the array frtoe (English titles in order of French page) :
	# check if there is an identical item in the titles array
	# IF there is a matching item then:
	# remove the matching item from the titles array and append it to the newENTitleArray
	# repeat

	# should result in newENTitleArray & the newENDefinitionarray 
	# containg every English definition title & definition in the 
	# SAME ORDER as the French definitions
	b = 0
	for title in titles:
		if frtoe[a].lower() == titles[b].lower():
			newENTitleArray.append(titles[b])
			newENDefinitionArray.append(definitions[b])
			titles.remove(titles[b])
			definitions.remove(definitions[b])

		b = b +1
	a = a + 1


# now that we have corresponding French and English definitions
# we simply write a new SKOS RDF entry for each definition including:
# - link to entry in thesaurus
# - English title
# - French title
# - English definition
# - French definition
# - reference to data's source (TSB definitions in this case)

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


# Validate is a definition that is ONLY present in the English version of this site
# http://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=12405
# Validate MUST be hardcoded in since it does not appear in the French version
# trying to include it programmatically would be far more effort than hardcoding
# will also probably result in broken links / missing definitions / this script not working

out.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#Validate\"> \n"+
                            "<skos:prefLabel xml:lang=\"fr\">Valider</skos:prefLabel> \n"+
                            "<skos:prefLabel xml:lang=\"en\">Validate</skos:prefLabel> \n"+
                            "<skos:scopeNote xml:lang=\"fr\">un moyen de confirmer qu'une personne possède les connaissances.</skos:scopeNote> \n"+
                            "<skos:scopeNote xml:lang=\"en\">means of confirming that an individual possesses the knowledge.</skos:scopeNote> \n"+
                            "<skos:references> TSB </skos:references>"+"\n"
                            "</skos:concept> \n\n")


#close file
out.write("</rdf:RDF>")
out.close()