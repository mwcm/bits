#pmbok2xml.py
#morgan mitchell
#April 29 2016
# -*- coding: utf-8 -*-

import csv, re, sys, os

#try, except block used to catch missing file paths
try:

    infile = sys.argv[1]
    outfile = sys.argv[2]


    with open(infile, newline='\n', encoding='utf-8-sig') as f:

       txt = open(outfile, "w")

       txt.write("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>")
       txt.write("<rdf:RDF \n xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" \n xmlns:skos=\"http://www.w3.org/2004/02/skos/core#\" \n xmlns:dc=\"http://purl.org/dc/elements/1.1/\"> \n \n")


       #define our conceptScheme
       txt.write("<skos:conceptScheme rdf:about=\"http://www.thesaurus.gc.ca/#CoreSubjectThesaurus\"></skos:conceptScheme>\n\n")


       txt.write("\n \n \n")

       content = f.readlines()


       titleList = []
       defList = []



       for row in reader[1:]:
            j=0


            for col in row:
                #if j == whatever
                #CHECK and add record definition & title to lists
                #tell what a cell contains by <b> text tag
                #MAKE SURE TO ACCOUNT FOR SPLIT DEFINITIONS
                #txt.write(<skos:concept......)
                txt.write("<skos:Concept>")
                amp = re.sub(r'&', "and", item).strip() 


    txt.write("</rdf:RDF>")
    txt.close()

#end of try at file start, used to fail gracefully if input/output file paths are not specified
except IndexError:
    print ("Oops! Missing valid input or output file! Please try again with format: \n      python test.py <input csv file here> <output xml file here>")