# -*- coding: utf-8 -*-

import sys

with open("data.xml", newline='\n', encoding='utf-8-sig') as f:


       content = str(f.readlines())

       content = content.rpartition('</Styles>')[-1]


       titles = []
       definitions = []


       for item in content.split("</Cell>"):
            if "<B>" in item:
                t = item [ item.find("<B>")+len("<B>") : ]
                t = t.split("</B>")[0]
                
                
                if ("Glossary" not in str(t)) and ("Glossaire" not in str(t)):
                    t = t.split("</Font>")[0]
                    t = t.split("<Font html:Size=\"12\">")
                    t = "".join(t)
                    t = t.replace("   ","  ").replace("  ", " ").replace(".","").replace("\\","").strip()
                    print(t)
                    titles.append(t)