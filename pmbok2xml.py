#pmbok2xml.py
#morgan mitchell
#April 29 2016
# -*- coding: utf-8 -*-

import re, sys, os

try:

  #variables for file paths
  infile = sys.argv[1]
  outfile = sys.argv[2]


  with open(infile, newline='\n', encoding='utf-8-sig') as f:

     txt = open(outfile, "w")

     txt.write("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>")
     txt.write("<rdf:RDF \n xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" \n xmlns:skos=\"http://www.w3.org/2004/02/skos/core#\" \n xmlns:dc=\"http://purl.org/dc/elements/1.1/\"> \n \n")


     #define our conceptScheme
     txt.write("<skos:conceptScheme rdf:about=\"http://www.thesaurus.gc.ca/#CoreSubjectThesaurus\"></skos:conceptScheme>\n\n")


     txt.write("\n \n \n")


     #infile content read into string
     content = str(f.readlines())


     #content cropped to leave out irrelevant leading/trailing information
     content = content.rpartition('</Styles>')[-1]
     content = content.rpartition('</Table>')[0]

     #arrays for titles and definitions of each concept
     titles = []
     definitions = []


     # count is the count of ALL cells INCLUDING EMPTY CELLS
     # this variable is used to tell if a cell is odd or even
     #    odd = column 1 = English, even = column 2 = French
     
     # when definitions get split(span more than one cell)
     # count is important so we know which column the split cell is from
     # and THEN can pair it with the correct first half of it's definition

     # ex: we encounter a split definition DEF
     # on encountering DEF the count is 22
     # 22 % 2 = 0, therefore DEF is a French definition fragment; 
     # so we add it to the SECOND last definition (the last one will be an English definition)
     # cd = definitions[-2];
     # DEF = cd + DEF;
     # definitions[-2] = DEF;
     count = 0


     #for each <Cell> in xml file do...
     #or more specifically: counts from beginning splitting the xml
     #by occurences of </Cell>
     for item in content.split("</Cell>"):

          # this is what an empty cell looks like in the xml
          # used to catch the otherwise uncounter empty cells  
          if '<Cell ss:StyleID=\"s19\"/>' in item:
            count = count + 1
          

          #if a cell has BOLD text then...
          #this is used to seperate SPLIT definitions from full ones
          #full definitions have a bold title
          #split definitions have no title, therefore no bold text
          if "<B>" in item:
              #extract the title by taking the text inside the bold tags
              t = item [ item.find("<B>")+len("<B>") : ]
              d = t.rpartition("</B>")[-1]
              t = t.split("</B>")[0]
              
              # if the cell is NOT a "Glossary" or "Glossaire" placeholder cell
              # THEN it is a title we need to append to the title array
              # we then extract the exact title and use replace to fix the formatting
              if ("Glossary" not in str(t)) and ("Glossaire" not in str(t)):
                  t = t.split("</Font>")[0]
                  t = t.split("<Font html:Size=\"12\">")
                  t = "".join(t)
                  t = t.replace("   ","  ").replace("  ", " ").replace(".","").replace("\\","").strip()
                  titles.append(t)

              # use split to extract the entry's definition
              # use replace and sub to fix formatting
              d = d.split("html:Size=\"12\">",1)[-1]
              d = re.sub('<[^>]+>', '', d)
              d = d.replace("   ","  ").replace("  ", " ").replace("\\","").strip()

              # if d is not an empty String
              # then it is a definition we need to add to the array
              if d:
                definitions.append(d)


          # if cell does NOT contain BOLD tag
          # then cell has NO title
          # therefore the cell in question is a split definition

          # we start by counting the cell
          # then split the definition from the xml tags
          # use sub and replace to fix formatting

          # finally:
          # if the count is even, append to last EN definition
          # if the count is odd,  append to last FR definition
          else:
            count = count + 1
            ud = item
            ud = ud.split("REC-html40\">",1)[-1]

            ud = re.sub('<[^>]+>', '', ud)
            ud = ud.replace("   ","  ").replace("  ", " ").replace("\\","").strip()
            
            if(ud != "rn\', \' rn\', \'"):
              if count % 2 == 0 :
                cd = definitions[-2]
                definitions[-2] = cd + ud
               # print(cd + ud +"\n")
              else:
                cd = definitions[-1]
                definitions[-1] = cd + ud
               # print(cd + ud +"\n")


  # for each title in the title array
  # create a skos concept containing:
  #      -  English title (preflabel)
  #      -  French title (preflabel)
  #      -  English definition
  #      -  French definition
  #      -  rdf about tag linking to thesaurus location of the concept
  c = 1
  for item in titles:
    a = c - 1
    txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#"+titles[a].replace(" ","%20")+"\"> \n"+
                            "<skos:prefLabel xml:lang=\"fr\">"+titles[c]+" </skos:prefLabel> \n"+
                            "<skos:prefLabel xml:lang=\"en\">" +titles[a]+" </skos:prefLabel> \n"+
                            "<skos:definition xml:lang=\"fr\">"+definitions[c]+"</skos:definition> \n"+
                            "<skos:definition xml:lang=\"en\">"+definitions[a]+"</skos:definition> \n"+
                            "</skos:concept> \n\n")

    #stop at end of definitions
    t = c + 2
    ld = len(definitions)
    if t <= ld:
      c = c + 2 

    else:
      break

  #close file
  txt.write("</rdf:RDF>")
  txt.close()

#end of try at file start, used to fail gracefully if input/output file paths are not specified
except IndexError:
    print ("Oops! Missing valid input or output file! Please try again with format: \n      python test.py <input xml file here> <output xml file here>")