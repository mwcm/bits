# -*- coding: utf-8 -*-

import sys, re

with open("data.xml", newline='\n', encoding='utf-8-sig') as f:


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
  print(titles[c]+" "+definitions[c]+"\n")
  c = c +1