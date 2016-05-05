#pmbok2xml.py
#morgan mitchell
#May 5th 2016
# -*- coding: utf-8 -*-

import re, sys, os


#variables for file paths
infile = sys.argv[1]
outfile = sys.argv[2]


with open(infile, newline='\n', encoding='utf-8-sig') as f:

	txt = open(outfile, "w")

	content = str(f.readlines())


	#arrays for titles and definitions of each concept
	titles = []
	definitions = [] 
	content = content.rpartition('</a>Appendix A - Definitions</h2>')[-1]
	content = content.rpartition('</details>')[0]
	#cut content up to occurence of </a>Appendix A - Definitions</h2>  </summary>



	for item in content.split("</dd>"):
		print(item+"\n")