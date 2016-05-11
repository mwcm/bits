<xsl:stylesheet version="1.0"
      xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
      xmlns:skos="http://www.w3.org/2004/02/skos/core#"
      xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:lrmi="http://purl.org/dcx/lrmi-terms/"
      xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
      xmlns:owl="http://www.w3.org/2002/07/owl#"
      xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">

<xsl:template match="/">
    <html>
      <body>
        <h1>My Thesaurus Portal</h1>

      	<xsl:apply-templates/>

	<xsl:call-template name="deprecated" />
	<xsl:call-template name="subjectList_toc" />
 	<xsl:call-template name="subjectList_expanded" />
 	
</body>
    </html>
  </xsl:template>


<xsl:template name="subjectList_toc" >
	<hr />
	<h2><a name="subjectList_toc" />List of Subjects:</h2>

 	<xsl:for-each select="//skos:concept/skos:hasTopConcept">
	<xsl:sort lang="en"  data-type="text"  order="ascending"  case-order="upper-first"/>
		<xsl:if test="not(. = preceding::skos:concept/skos:hasTopConcept)">
          		
			<a href="#{.}"><xsl:value-of select="."/></a>
            		<br />
         	</xsl:if>
	</xsl:for-each>
	<hr />
</xsl:template>
	
 <xsl:template name="subjectList_expanded" >
	<hr />
	<h2><a name="subjectList_expanded" />Terms by Subject:</h2>

 	<xsl:for-each select="//skos:concept/skos:hasTopConcept">
	<xsl:sort lang="en"  data-type="text"  order="ascending"  case-order="upper-first"/>
		<xsl:if test="not(. = preceding::skos:concept/skos:hasTopConcept)">
          		
			<h2><a name="{.}" /><xsl:value-of select="."/></h2>
            		
         	</xsl:if>
		<a href="#{../skos:prefLabel}"><xsl:value-of select="../skos:prefLabel"/></a><br />
        </xsl:for-each>
	<hr />
</xsl:template>

<!--
<xsl:template name="subjectList_expanded" >
	<hr />
	<h2><a name="subjectList_expanded" />Terms by Subject:</h2>

 	<xsl:for-each select="//skos:concept/skos:hasTopConcept">
   	 <xsl:sort lang="en"  data-type="text"  order="ascending"  case-order="upper-first"/>
		<xsl:if test="not(. = preceding::skos:concept/skos:hasTopConcept)">
          		
			<h2><a name="." /><xsl:value-of select="."/></h2>
            	
		</xsl:if>	
		<a href="#{../skos:prefLabel}"><xsl:value-of select="../skos:prefLabel"/></a>
            	<br />
        	
        	
    </xsl:for-each>
<hr />
	
</xsl:template>

-->

<xsl:template name="terms_in_subject" >
	<a href="#{.}"><xsl:value-of select="."/></a>
            	<xsl:for-each select="//skos:concept[skos:hasTopConcept = . ]">
   	<xsl:sort lang="en"  data-type="text"  order="ascending"  case-order="upper-first"/>
		<a href="#{.}"><xsl:value-of select="./skos:prefLabel"/></a>
            	<br />
        </xsl:for-each>
</xsl:template>


<xsl:template name="deprecated" >
	<hr />
	<h2><a name="deprecated"></a>Deprecated Terms:</h2>

 	<xsl:for-each select="//skos:concept/skos:altLabel">
   	 <xsl:sort lang="en"  data-type="text"  order="ascending"  case-order="upper-first"/>
		<xsl:if test="not(. = preceding::skos:concept/skos:hasTopConcept)">
          		<hr/><h2><a name="{.}" /><xsl:value-of select="." /></h2>
				<h3>Use: </h3>
					<a href="#{../skos:prefLabel}"><xsl:value-of select="../skos:prefLabel"/></a>
            		     
         </xsl:if>
        	
    </xsl:for-each>
<hr />
	

</xsl:template>


<xsl:template match="skos:conceptScheme">
   <p>
   <a href="{@rdf:about}"><xsl:value-of select="."/>Information</a>
   </p>
</xsl:template>

<xsl:template match="skos:concept">
   
	<xsl:apply-templates select="skos:prefLabel"/>
	<xsl:apply-templates select="skos:Historynote"/>
   	<xsl:apply-templates select="skos:scopeNote"/>
	<xsl:apply-templates select="skos:altLabel"/>
	
	<xsl:apply-templates select="skos:related"/>
	<xsl:apply-templates select="skos:broader"/>
	<xsl:apply-templates select="skos:narrower"/>
	<xsl:apply-templates select="skos:hasTopConcept"/>
	<xsl:apply-templates select="dc:author"/>
	<xsl:apply-templates select="lrmi:alignmentType"/>
	<xsl:apply-templates select="skos:inScheme"/>
</xsl:template>

<xsl:template match="skos:concept/skos:hasTopConcept">
	<xsl:choose>
		<xsl:when test="position()=1">
			<h3><xsl:text>Subject Category: </xsl:text></h3>
			<a href="#{.}"><xsl:value-of select="."/></a>
            		<br />
		</xsl:when>
         	<xsl:otherwise>
        		<a href="#{.}"><xsl:value-of select="."/></a>
            		<br />
         	</xsl:otherwise>
       </xsl:choose>
</xsl:template>
<xsl:template match="skos:concept/dc:author">
	<xsl:choose>
		<xsl:when test="position()=1">
			<h3><xsl:text>Author: </xsl:text></h3>
			<xsl:value-of select="."/>
			<br />
		</xsl:when>
         	<xsl:otherwise>
        		<xsl:value-of select="."/>
            		<br />
         	</xsl:otherwise>
       </xsl:choose>
</xsl:template>
<xsl:template match="skos:concept/lrmi:alignmentType">
	<xsl:choose>
		<xsl:when test="position()=1">
			<h3><xsl:text>Alignment Type: </xsl:text></h3>
			<xsl:value-of select="."/>
			<br />
		</xsl:when>
         	<xsl:otherwise>
        		<xsl:value-of select="."/>
            		<br />
         	</xsl:otherwise>
       </xsl:choose>
</xsl:template>
<xsl:template match="skos:concept/skos:narrower">

	<xsl:variable name="linkSuffix" select="@rdf:resource" />
	<xsl:choose>
		<xsl:when test="position()=1">
			<h3><xsl:text>Narrower Term: </xsl:text></h3>
			<a href="{concat('#',substring-after($linkSuffix,'#'))}"><xsl:value-of select="substring-after($linkSuffix,'#')"/></a>
            		<br />
		</xsl:when>
         	<xsl:otherwise>
        		<a href="{concat('#',substring-after($linkSuffix,'#'))}"><xsl:value-of select="substring-after($linkSuffix,'#')"/></a>
            		<br />
         	</xsl:otherwise>
       </xsl:choose>
</xsl:template>
<xsl:template match="skos:concept/skos:related">

	<xsl:variable name="linkSuffix" select="@rdf:resource" />
	<xsl:choose>
		<xsl:when test="position()=1">
			<h3><xsl:text>Related Term: </xsl:text></h3>
			<a href="{concat('#',substring-after($linkSuffix,'#'))}"><xsl:value-of select="substring-after($linkSuffix,'#')"/></a>
            		<br />
		</xsl:when>
         	<xsl:otherwise>
        		<a href="{concat('#',substring-after($linkSuffix,'#'))}"><xsl:value-of select="substring-after($linkSuffix,'#')"/></a>
            		<br />
         	</xsl:otherwise>
       </xsl:choose>
</xsl:template>
<xsl:template match="skos:concept/skos:broader">
	<xsl:variable name="linkSuffix" select="@rdf:resource" />
	<xsl:choose>
		<xsl:when test="position()=1">
			<h3><xsl:text>Broader Term: </xsl:text></h3>
			<a href="{concat('#',substring-after($linkSuffix,'#'))}"><xsl:value-of select="substring-after($linkSuffix,'#')"/></a>
            		<br />
		</xsl:when>
         	<xsl:otherwise>
        		<a href="{concat('#',substring-after($linkSuffix,'#'))}"><xsl:value-of select="substring-after($linkSuffix,'#')"/></a>
            		<br />
         	</xsl:otherwise>
       </xsl:choose>
</xsl:template>
<xsl:template match="skos:concept/skos:altLabel">
	<xsl:choose>
		<xsl:when test="position()=1">
			<h3><xsl:text>Use For: </xsl:text></h3>
			<xsl:value-of select="."/>
            		<br />
		</xsl:when>
         	<xsl:otherwise>
        		<xsl:value-of select="."/>
            		<br />
         	</xsl:otherwise>
       </xsl:choose>
</xsl:template>

<xsl:template match="skos:concept/skos:Historynote">
	<xsl:choose>
		<xsl:when test="position()=1">
			<h3><xsl:text>History Note: </xsl:text></h3>
			<xsl:value-of select="."/>
			<br />
		</xsl:when>
         	<xsl:otherwise>
        		<xsl:value-of select="."/>
            		<br />
         	</xsl:otherwise>
       </xsl:choose>
</xsl:template>
	
<xsl:template match="skos:concept/skos:scopeNote">
	<xsl:choose>
		<xsl:when test="position()=1">
			<h3><xsl:text>Scope Note: </xsl:text></h3>
			<xsl:value-of select="."/>
			<br />
		</xsl:when>
         	<xsl:otherwise>
        		<xsl:value-of select="."/>
            		<br />
         	</xsl:otherwise>
       </xsl:choose>
</xsl:template>
	
<xsl:template match="skos:concept/skos:prefLabel">
   <xsl:choose>
         <xsl:when test="@xml:lang='fr'">
        	<p><xsl:text>FR: </xsl:text><a href="http://www.thesaurus.gc.ca/#{.}"><xsl:value-of select="."/></a></p>
	</xsl:when>
         <xsl:otherwise>
        	<hr/><h2><a name="{.}" /><xsl:value-of select="." /></h2>
	</xsl:otherwise>
       </xsl:choose>
</xsl:template>

  

<xsl:template match="skos:concept/skos:inScheme">
</xsl:template>


      
</xsl:stylesheet>