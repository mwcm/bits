#csv2xml.py
#morgan mitchell
#April 27 2016
# -*- coding: utf-8 -*-

import csv, re, sys, os


#try, except block used to catch missing file paths
try:

    #set input / output file paths
    infile = sys.argv[1]
    outfile = sys.argv[2]



    #the code is broken up into two open file blocks
    #the first pass through we loop through specific columns to create concepts which the final concepts will reference
    #the second pass through we create one concept for each row in the spreadsheet, referencing basic concepts created in the first pass

    #creating basic concepts
    with open(infile, newline='\n', encoding='utf-8-sig') as q:


        #check if in/out files are valid

        if not infile.lower().endswith('.csv'):
            raise Exception('Invalid Input Format', 'Please try again with a valid CSV file')
            sys.exit()

        if not outfile.lower().endswith('.xml'):
            raise Exception('Invalid Output Format', 'Please try again with a valid XML file extension')
            sys.exit()

        if os.stat(infile).st_size == 0:
            raise Exception('Empty Input File', 'Please try again with a valid input CSV.')
            sys.exit()


        #all of this is included here so we ONLY do opetartions on the outfile IF the infile loads correctly        
        #define to xml, rdf, skos, dc
        txt = open(outfile, "w")
        txt.write("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>")
        txt.write("<rdf:RDF \n xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" \n xmlns:skos=\"http://www.w3.org/2004/02/skos/core#\" \n xmlns:dc=\"http://purl.org/dc/elements/1.1/\"> \n \n")


        #define our conceptScheme
        txt.write("<skos:conceptScheme rdf:about=\"http://www.thesaurus.gc.ca/#CoreSubjectThesaurus\"></skos:conceptScheme>\n\n")


        txt.write("\n \n \n")

        #top copncepts related to spreadsheet columns
        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#InputFormat\"> \n")
        txt.write("<skos:prefLabel>Input format</skos:prefLabel></skos:concept>\n \n ")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#DropDownDataEN\"> \n")
        txt.write("<skos:prefLabel>Drop down data EN</skos:prefLabel></skos:concept> \n \n")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#DropDownDataFR\"> \n")
        txt.write("<skos:prefLabel>Drop down data FR</skos:prefLabel></skos:concept> \n \n")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#MetadataUsedFor\"> \n")
        txt.write("<skos:prefLabel>Metadata used for</skos:prefLabel></skos:concept> \n \n ")


        txt.write("\n \n \n")

        #more top concepts related to spreadsheet columns
        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#UsedByCPNO\"> \n")
        txt.write("<skos:prefLabel>Metadata used by CPNO</skos:prefLabel></skos:concept> \n \n ")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#UsedByeSchool\"> \n")
        txt.write("<skos:prefLabel>Metadata used by eSchool</skos:prefLabel></skos:concept> \n \n ")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#UsedByDesign\"> \n")
        txt.write("<skos:prefLabel>Metadata used by Design</skos:prefLabel></skos:concept> \n \n ")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#UsedByOST\"> \n")
        txt.write("<skos:prefLabel>Metadata used by OST</skos:prefLabel></skos:concept> \n \n ")


        txt.write("\n \n \n")

        #more top concepts related to spreadsheet columns
        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#AddedProtegeWhen\"> \n")
        txt.write("<skos:prefLabel>Metadata added to protege on the date</skos:prefLabel></skos:concept> \n \n ")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#MetadataReference\"> \n")
        txt.write("<skos:prefLabel>Metadata reference</skos:prefLabel></skos:concept> \n \n ")

        txt.write("\n \n \n")




        #open input data
        reader = list(csv.reader(q))


        #these lists used to make sure we only create ONE concept 
        #for each given: format, enDropDownData, frDropDownData, MetadataRelatedTo value
        #i.e: Course, Policy, Yes, No, Oui, Non, etc... occur many times but each require only one concept

        #these lists correspond the 4 fields we have to create entries for FIRST in the output xml
        #we MUST create the entries for these 4 fields first since following entries will need to reference them
        formatList = []
        enPossibleList = []
        frPossibleList = []
        metadataList = []


        #for row in spreadsheet
        #START AT ROW 1 (NOT 0) to avoid creating an object for the column labels
        for row in reader[1:]:
            j = 0

            #for each entry in each row
            for col in row:
                #col = re.sub(r'&', "and", col).strip()

                #j counts current position in current row

                if j == 2:  #FORMAT

                    #strip ampersands and trailing/leading spaces
                    col = re.sub(r'&', "and", col).strip()
                    #replace non-trainling/leading spaces
                    #listText is for formatList to check duplicates
                    #webText is encoded to be in browser's path bar
                    #display text is formatted to be readable
                    listText = col.replace(" ","")
                    webText = col.replace(" ","%20")
                    displayText = col
                    if (listText and not listText.isspace()) and (listText not in formatList):
                        #append entry to list so no duplicates arise
                        formatList.append(listText)
                        #write skos concept entry
                        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#"+webText+"\"> \n"+
                                    "<skos:prefLabel>"+displayText+" </skos:prefLabel> \n"+
                                    "<skos:hasTopConcept  rdf:resource=\"http://www.thesaurus.gc.ca/concept/#InputFormat\"/> \n"+
                                    "</skos:concept> \n\n")
             
                elif j == 3: #DROP DOWN OPTIONS EN
                    lines = col.splitlines(True)
                
                    #same as above, except Drop Down Options EN is a field which
                    #has multiple options in ONE cell seperated by newlines 
                    #
                    #SO, we make an entry (same process as Format above)
                    #EXCEPT, we make the entries in a loop, one for each newline
                    for item in lines:
                        item = re.sub(r'&', "and", item).strip()
                        listText = item.replace(" ","")
                        webText = item.replace(" ","%20")
                        displayText = item
                        if (listText and not listText.isspace()) and (listText not in enPossibleList):
                            enPossibleList.append(listText)
                            txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#"+webText+"\"> \n"+
                                    "<skos:prefLabel>"+displayText+" </skos:prefLabel> \n"+
                                    "<skos:hasTopConcept  rdf:resource=\"http://www.thesaurus.gc.ca/concept/#DropDownDataEN\"/> \n"+
                                    "</skos:concept> \n\n")

                elif j == 4:  #DROP DOWN OPTIONS FR

                    lines = col.splitlines(True)
                    for item in lines:
                        item = re.sub(r'&', "and", item).strip()
                        listText = item.replace(" ","")
                        webText = item.replace(" ","%20")
                        displayText = item
                        if (listText and not listText.isspace()) and (listText not in frPossibleList):
                            frPossibleList.append(listText)
                            txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#"+webText+"\"> \n"+
                                    "<skos:prefLabel>"+displayText+" </skos:prefLabel> \n"+
                                    "<skos:hasTopConcept  rdf:resource=\"http://www.thesaurus.gc.ca/concept/#DropDownDataFR\"/> \n"+
                                    "</skos:concept> \n\n")

                elif j == 9:    #METADATA

                    lines = col.splitlines(True)
                    for item in lines:
                        item = re.sub(r'&', "and", item).strip()
                        listText = item.replace(" ","")
                        webText = item.replace(" ","%20")
                        displayText = item
                        if (listText and not listText.isspace()) and (listText not in metadataList):
                            metadataList.append(listText)
                            txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#"+webText+"\"> \n"+
                                    "<skos:prefLabel>"+displayText+" </skos:prefLabel> \n"+
                                    "<skos:hasTopConcept  rdf:resource=\"http://www.thesaurus.gc.ca/concept/#MetadataUsedFor\"/> \n"+
                                    "</skos:concept> \n\n")

                        

                else:
                    #if j is not one of the 4 fields we MUST create first 
                    #do nothing with the value in the cell and pass to next one
                    pass

            
                j = j + 1


    #once done with required concepts from those four columns:
    #continue to make one concept per row in the spreadsheet, referencing the basic concepts we have just created as we go

    with open(infile, newline='\n', encoding='utf-8-sig') as f:
        reader = list(csv.reader(f))

        #START AT ROW 1 (NOT 0) to avoid creating an object for the column labels
        for row in reader[1:]:

            #beginning of concept
            txt.write("<skos:Concept>")

            i = 0
            #for each cell in a row
            for item in row:
                
                #strip amperands and leading/trailing spaces
                amp = re.sub(r'&', "and", item).strip()

                if i == 0:
                    #create English prefLabel if it exists
                 if amp:
                    txt.write("<skos:prefLabel xml:lang=\"en\">"+amp+"</skos:prefLabel>\n")
                
                elif i == 1: 
                    #create French preflabel if it exists
                 if amp:
                    txt.write("<skos:prefLabel xml:lang=\"fr\">"+amp+"</skos:prefLabel>\n")
                
                elif i == 2: 
                    #create reference to Format of the concept if it has one
                 if amp:
                    amp = amp.replace(" ","%20")
                    txt.write("<skos:hasTopConcept rdf:resource= \"http://www.thesaurus.gc.ca/concept/#"+amp+"\"/> \n")

                elif i == 3:
                    #create references to the concepts EN drop down options if they exist
                    lines = amp.splitlines(True)
                    for item in lines:
                        if item:
                            item = item.replace(" ","%20").strip()
                            txt.write("<skos:narrower rdf:resource= \"http://www.thesaurus.gc.ca/concept/#"+item+"\"/> \n")

                elif i == 4:
                    #create references to the concepts FR drop down options if they exist
                    lines = amp.splitlines(True)
                    for item in lines:
                        if item:
                            item = item.replace(" ","%20").strip()
                            txt.write("<skos:narrower rdf:resource= \"http://www.thesaurus.gc.ca/concept/#"+item+"\"/> \n")
                    
                elif i == 5:
                    #if concept used by CPNO create a reference
                 if amp:
                    txt.write("<dc:isRequiredBy rdf:resource = \"http://www.thesaurus.gc.ca/concept/#UsedByCPNO\"/>\n")
                
                elif i == 6:
                    #if concept used by eSchool create a reference
                 if amp:
                    txt.write("<dc:isRequiredBy rdf:resource = \"http://www.thesaurus.gc.ca/concept/#UsedByeSchool\"/>\n")
                
                elif i == 7:
                    #if concept used by Design create a reference
                 if amp:
                    txt.write("<dc:isRequiredBy rdf:resource = \"http://www.thesaurus.gc.ca/concept/#UsedByDesign\"/>\n")
                
                elif i == 8:
                    #if concept used by OST create a reference
                 if amp:
                    txt.write("<dc:isRequiredBy rdf:resource = \"http://www.thesaurus.gc.ca/concept/#UsedByOST\"/>\n")
                
                elif i == 9:
                    #create reference(s) to concepts related to the data (what the data is tied to)
                    lines = amp.splitlines(True)
                    for item in lines:
                        if item:
                            item = item.replace(" ","%20").strip()
                            txt.write("<skos:related rdf:resource= \"http://www.thesaurus.gc.ca/concept/#"+item+"\"/> \n")




                #still unsure if these two fields should be included in the XML output
                #have included just in case!

                elif i == 10:
                    #if date included, create date added to protege field
                 if amp:
                    txt.write("<dc:date>"+amp+"</dc:date>\n")
                
                elif i == 11:
                    #if same concept exists somewhere else, create reference to it
                 if amp:
                    amp.replace(" ","%20")
                    txt.write("<skos:exactmatch rdf:resource=\""+amp+"\"/>\n")
                
                #ignore all other cells
                else:
                    pass

                i = i + 1

            #end of concept
            txt.write("</skos:Concept>\n \n")

    #end of file
    txt.write("</rdf:RDF>") 
    txt.close()

#end of try at file start, used to fail gracefully if input/output file paths are not specified
except IndexError:
    print ("Oops! Missing valid input or output file! Please try again with format: \n      python test.py <input csv file here> <output xml file here>")