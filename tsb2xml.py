#pmbok2xml.py
#morgan mitchell
#May 5th 2016
# -*- coding: utf-8 -*-

import re, sys, os


#variables for file paths
endata = sys.argv[1]
frdata = sys.argv[2]
outfile = sys.argv[3]


with open(endata, newline='\n', encoding='utf-8-sig') as e:

	txt = open(outfile, "w")

	content = str(e.readlines())


	#arrays for titles and definitions of each concept
	entitles = []
	endefinitions = [] 
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
			entitles.append(t)
			print(t+"\n")

		if d and "\\r\\n" not in d:
			endefinitions.append(d)
			print(d+"\n")

with open(frdata, newline='\n', encoding='utf-8-sig') as f:

	txt = open(outfile, "a")

	content = str(f.readlines())


	#arrays for titles and definitions of each concept
	frtitles = []
	frdefinitions = [] 
	content = content.rpartition('</a>Annexe A - Définitions</h2>')[-1]
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
			frtitles.append(t)
			print(t+"\n")

		if d and "\\r\\n" not in d:
			frdefinitions.append(d)
			print(d+"\n")




