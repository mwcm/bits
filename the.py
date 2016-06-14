import re, sys, os, io

try:
	infile  = sys.argv[1]
	outfile = sys.argv[2]

	with io.open(outfile,'w',encoding='utf8') as f:

		with io.open(infile, 'r', encoding='utf8') as q:

			thesaurus = q.read()

			urls = re.findall(r'http://(.*?)\"', thesaurus)

			for url in urls:
			 	newUrl = url.replace(" ","%20")
			 	thesaurus = thesaurus.replace(url, newUrl,1)
			 	print(newUrl)

			f.write(thesaurus)

#end of try at file start, used to fail gracefully if input/output file paths are not specified
except IndexError:
    print ("Oops! Missing valid input or output file! Please try again with format: \n      python test.py <input xml file here> <output xml file here>")