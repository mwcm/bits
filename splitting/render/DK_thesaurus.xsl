<xsl:stylesheet version="1.0"
      xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
      xmlns:skos="http://www.w3.org/2004/02/skos/core#"
      xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
      xmlns:owl="http://www.w3.org/2002/07/owl#"
      xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">

  <xsl:template match="/">
    <html>
      <body>
        <h1>My Thesaurus Portal</h1>
	<xsl:apply-templates/>
      </body>
    </html>
  </xsl:template>

<xsl:template match="skos:conceptScheme">
   <p>
   <a href="{@rdf:about}"><xsl:value-of select="."/>Information</a>
   </p>
</xsl:template>

<xsl:template match="skos:concept">
   <xsl:apply-templates select="skos:prefLabel"/>
   <xsl:apply-templates select="skos:scopeNote"/>

   	<xsl:text>Related: </xsl:text>
        <br />
	  <xsl:for-each select="skos:related">
            <a href="{@rdf:resource}"><xsl:value-of select="@rdf:resource"/></a>
            <br />
          </xsl:for-each>

   <xsl:apply-templates select="skos:altLabel"/>
   <xsl:apply-templates select="skos:broader"/>
   <xsl:apply-templates select="skos:narrower"/>
   <xsl:apply-templates select="skos:Historynote"/>
   <xsl:apply-templates select="skos:hasTopConcept"/>
   <xsl:apply-templates select="skos:inScheme"/>
</xsl:template>

<xsl:template match="skos:concept/skos:prefLabel">
   <xsl:choose>
         <xsl:when test="@xml:lang='fr'">
        	<h2><xsl:text>FR: </xsl:text><xsl:value-of select="." /></h2>
	</xsl:when>
         <xsl:otherwise>
        	<h2><xsl:text>EN: </xsl:text><xsl:value-of select="." /></h2>
	</xsl:otherwise>
       </xsl:choose>
</xsl:template>

<xsl:template match="skos:concept/skos:scopeNote">
 	<xsl:text>Scope Note: </xsl:text>
        <br />
	  <xsl:for-each select="concept/skos:scopeNote">
            <a href="{@rdf:resource}"><xsl:value-of select="."/></a>
            <br />
          </xsl:for-each>
</xsl:template>
      
<xsl:template match="skos:concept/skos:related">
 	<xsl:text>Related: </xsl:text>
        <br />
	  <xsl:for-each select="concept/skos:related">
            <a href="{@rdf:resource}"><xsl:value-of select="."/></a>
            <br />
          </xsl:for-each>
</xsl:template>
      
<xsl:template match="skos:concept/skos:altLabel">
 	<xsl:text>Alt Label: </xsl:text>
        <br />
	  <xsl:for-each select="concept/skos:altLabel">
            <a href="{@rdf:resource}"><xsl:value-of select="."/></a>
            <br />
          </xsl:for-each>
</xsl:template>
      
<xsl:template match="skos:concept/skos:broader">
 	<xsl:text>Broader: </xsl:text>
        <br />
	  <xsl:for-each select="concept/skos:broader">
            <a href="{@rdf:resource}"><xsl:value-of select="."/></a>
            <br />
          </xsl:for-each>
</xsl:template>
      
<xsl:template match="skos:concept/skos:narrower">
 	<xsl:text>Narrower: </xsl:text>
        <br />
	  <xsl:for-each select="concept/skos:narrower">
            <a href="{@rdf:resource}"><xsl:value-of select="."/></a>
            <br />
          </xsl:for-each>
</xsl:template>
 <xsl:template match="skos:concept/skos:Historynote">
 	<xsl:text>Historynote: </xsl:text>
        <br />
	  <xsl:for-each select="concept/skos:narrower">
            <a href="{@rdf:resource}"><xsl:value-of select="."/></a>
            <br />
          </xsl:for-each>
</xsl:template>
 <xsl:template match="skos:concept/skos:hasTopConcept">
 	<xsl:text>hasTopConcept: </xsl:text>
        <br />
	  <xsl:for-each select="concept/skos:hasTopConcept">
            <a href="{@rdf:resource}"><xsl:value-of select="."/></a>
            <br />
          </xsl:for-each>
</xsl:template>
 <xsl:template match="skos:concept/skos:inScheme">
 	<xsl:text>inScheme: </xsl:text>
        <br />
	  <xsl:for-each select="concept/skos:inScheme">
            <a href="{@rdf:resource}"><xsl:value-of select="."/></a>
            <br />
          </xsl:for-each>
</xsl:template>
      
</xsl:stylesheet>