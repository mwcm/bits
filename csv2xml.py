#csv2xml.py
#morgan mitchell
#April 27 2016
# -*- coding: utf-8 -*-

import csv, re, sys, os


try:

    infile = sys.argv[1]
    outfile = sys.argv[2]

    with open(infile, newline='\n', encoding='utf-8-sig') as q:

        if not infile.lower().endswith('.csv'):
            raise Exception('Invalid Input Format', 'Please try again with a valid CSV file')

        if not outfile.lower().endswith('.xml'):
            raise Exception('Invalid Output Format', 'Please try again with a valid XML file')

        if os.stat(infile).st_size == 0:
            raise Exception('Empty Input File', 'Please try again with a valid input CSV.')
            sys.exit()

        #only do operations on outfile if infile loads properly
        txt = open(outfile, "w")
        txt.write("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>")
        txt.write("<rdf:RDF \n xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" \n xmlns:skos=\"http://www.w3.org/2004/02/skos/core#\" \n xmlns:dc=\"http://purl.org/dc/elements/1.1/\"> \n \n")

        txt.write("<skos:conceptScheme rdf:about=\"http://www.thesaurus.gc.ca/#CoreSubjectThesaurus\"></skos:conceptScheme>\n\n")


        txt.write("\n \n \n")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#InputFormat\"> \n")
        txt.write("<skos:prefLabel>Input format</skos:prefLabel></skos:concept>\n \n ")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#DropDownDataEN\"> \n")
        txt.write("<skos:prefLabel>Drop down data EN</skos:prefLabel></skos:concept> \n \n")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#DropDownDataFR\"> \n")
        txt.write("<skos:prefLabel>Drop down data FR</skos:prefLabel></skos:concept> \n \n")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#MetadataUsedFor\"> \n")
        txt.write("<skos:prefLabel>Metadata used for</skos:prefLabel></skos:concept> \n \n ")


        txt.write("\n \n \n")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#UsedByCPNO\"> \n")
        txt.write("<skos:prefLabel>Metadata used by CPNO</skos:prefLabel></skos:concept> \n \n ")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#UsedByeSchool\"> \n")
        txt.write("<skos:prefLabel>Metadata used by eSchool</skos:prefLabel></skos:concept> \n \n ")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#UsedByDesign\"> \n")
        txt.write("<skos:prefLabel>Metadata used by Design</skos:prefLabel></skos:concept> \n \n ")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#UsedByOST\"> \n")
        txt.write("<skos:prefLabel>Metadata used by OST</skos:prefLabel></skos:concept> \n \n ")


        txt.write("\n \n \n")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#AddedProtegeWhen\"> \n")
        txt.write("<skos:prefLabel>Metadata added to protege on the date</skos:prefLabel></skos:concept> \n \n ")

        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/#MetadataReference\"> \n")
        txt.write("<skos:prefLabel>Metadata reference</skos:prefLabel></skos:concept> \n \n ")

        txt.write("\n \n \n")





        reader = csv.reader(q)

        formatList = []
        enPossibleList = []
        frPossibleList = []
        metadataList = []

        for row in reader:
            j = 0

            for col in row:
                #col = re.sub(r'&', "and", col).strip()

                
                if j == 2:  #FORMAT

                    col = re.sub(r'&', "and", col).strip()
                    listText = col.replace(" ","")
                    webText = col.replace(" ","%20")
                    displayText = col
                    if (listText and not listText.isspace()) and (listText not in formatList):
                        formatList.append(listText)
                        txt.write("<skos:concept rdf:about=\"http://www.thesaurus.gc.ca/concept/#"+webText+"\"> \n"+
                                    "<skos:prefLabel>"+displayText+" </skos:prefLabel> \n"+
                                    "<skos:hasTopConcept  rdf:resource=\"http://www.thesaurus.gc.ca/concept/#InputFormat\"/> \n"+
                                    "</skos:concept> \n\n")
                elif j == 3: #DROP DOWN OPTIONS EN
                    #FOR EACH NEW LINE SEPERATED VALUE IN AMP .....
                    lines = col.splitlines(True)
                
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

                    #FOR EACH NEW LINE SEPERATED VALUE IN AMP .....

                elif j == 4:  #DROP DOWN OPTIONS FR
                    #FOR EACH NEW LINE SEPERATED VALUE IN AMP .....

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
                    #FOR EACH NEW LINE SEPERATED VALUE IN AMP .....

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
                    #do nothing
                    pass

            
                j = j + 1

    print(formatList)
    txt.write("\n \n END OF format / drop down options / metadata \n \n ")


    with open(infile, newline='\n', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:

            txt.write("<skos:Concept>")

            i = 0
            for item in row:
                
                amp = re.sub(r'&', "and", item).strip()

                if i == 0:
                 if amp:
                    txt.write("<skos:prefLabel xml:lang=\"en\">"+amp+"</skos:prefLabel>\n")
                
                elif i == 1: 
                 if amp:
                    txt.write("<skos:prefLabel xml:lang=\"fr\">"+amp+"</skos:prefLabel>\n")
                
                elif i == 2: 
                 if amp:
                    amp = amp.replace(" ","%20")
                    txt.write("<skos:hasTopConcept rdf:resource= \"http://www.thesaurus.gc.ca/concept/#"+amp+"\"/> \n")

                elif i == 3:
                    lines = amp.splitlines(True)
                    for item in lines:
                        if item:
                            item = item.replace(" ","%20").strip()
                            txt.write("<skos:narrower rdf:resource= \"http://www.thesaurus.gc.ca/concept/#"+item+"\"/> \n")

                elif i == 4:
                    lines = amp.splitlines(True)
                    for item in lines:
                        if item:
                            item = item.replace(" ","%20").strip()
                            txt.write("<skos:narrower rdf:resource= \"http://www.thesaurus.gc.ca/concept/#"+item+"\"/> \n")
                    
                elif i == 5:
                 if amp:
                    txt.write("<dc:isRequiredBy rdf:resource = \"http://www.thesaurus.gc.ca/concept/#UsedByCPNO\"/>\n")
                
                elif i == 6:
                 if amp:
                    txt.write("<dc:isRequiredBy rdf:resource = \"http://www.thesaurus.gc.ca/concept/#UsedByeSchool\"/>\n")
                
                elif i == 7:
                 if amp:
                    txt.write("<dc:isRequiredBy rdf:resource = \"http://www.thesaurus.gc.ca/concept/#UsedByDesign\"/>\n")
                
                elif i == 8:
                 if amp:
                    txt.write("<dc:isRequiredBy rdf:resource = \"http://www.thesaurus.gc.ca/concept/#UsedByOST\"/>\n")
                
                elif i == 9:
                    lines = amp.splitlines(True)
                    for item in lines:
                        if item:
                            item = item.replace(" ","%20").strip()
                            txt.write("<skos:related rdf:resource= \"http://www.thesaurus.gc.ca/concept/#"+item+"\"/> \n")

                elif i == 10:
                 if amp:
                    txt.write("<dc:date>"+amp+"</dc:date>\n")
                
                elif i == 11:
                 if amp:
                    amp.replace(" ","%20")
                    txt.write("<skos:exactmatch rdf:resource=\""+amp+"\"/>\n")
                
                else:
                    pass

                i = i + 1

            txt.write("</skos:Concept>")


            txt.write("\n\n")

    txt.write("</rdf:RDF>") 
    txt.close()

except IndexError:
    print ("Oops! Missing valid input or output file! Please try again with format: \n      python test.py <input csv file here> <output xml file here>")