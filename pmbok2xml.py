#pmbok2xml.py
#morgan mitchell
#April 29 2016
# -*- coding: utf-8 -*-

import re, sys, os

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

       content = str(f.readlines())

       content = content.rpartition('</Styles>')[-1]
       content = content.rpartition('</Table>')[0]


       titles = []
       definitions = []
       count = 0


       for item in content.split("</Cell>"):

            if '<Cell ss:StyleID=\"s19\"/>' in item:
              count = count + 1
            if "<B>" in item:
                t = item [ item.find("<B>")+len("<B>") : ]
                d = t.rpartition("</B>")[-1]
                t = t.split("</B>")[0]
                
                
                if '<Cell ss:StyleID=\"s19\"/>' in item:
                   count = count + 1

                if ("Glossary" not in str(t)) and ("Glossaire" not in str(t)):
                    t = t.split("</Font>")[0]
                    t = t.split("<Font html:Size=\"12\">")
                    t = "".join(t)
                    t = t.replace("   ","  ").replace("  ", " ").replace(".","").replace("\\","").strip()
                    titles.append(t)

                d = d.split("html:Size=\"12\">",1)[-1]
                d = re.sub('<[^>]+>', '', d)
                d = d.replace("   ","  ").replace("  ", " ").replace("\\","").strip()

                if d:
                  definitions.append(d)

            else:
              count = count + 1
              ud = item
              ud = ud.split("REC-html40\">",1)[-1]

              ud = re.sub('<[^>]+>', '', ud)
              ud = ud.replace("   ","  ").replace("  ", " ").replace("\\","").strip()
              
              if(ud != "rn\', \' rn\', \'"):
                if count % 2 == 0 :
                  cd = definitions[-1]
                  definitions[-1] = cd + ud
                 # print(cd + ud +"\n")
                else:
                  cd = definitions[-2]
                  definitions[-2] = cd + ud
                 # print(cd + ud +"\n")

   
    c = 0
    for item in titles:
      txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#"+titles[c].replace(" ","%20")+"\"> \n"+
                              "<skos:prefLabel>"+titles[c]+" </skos:prefLabel> \n"+
                              "<skos:definition>"+definitions[c]+"</skos:definition> \n"+
                              "</skos:concept> \n\n")
      c = c +1 

    txt.write("</rdf:RDF>")
    txt.close()
 
 #end of try at file start, used to fail gracefully if input/output file paths are not specified
except IndexError:
    print ("Oops! Missing valid input or output file! Please try again with format: \n      python test.py <input csv file here> <output xml file here>")