<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" 
			xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
			xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
			xmlns:skos="http://www.w3.org/2004/02/skos/core#"
			xmlns:dc="http://purl.org/dc/elements/1.1/"
			xmlns:lrmi="http://purl.org/dcx/lrmi-terms/"
			xpath-default-namespace="http://www.w3.org/1999/02/22-rdf-syntax-ns#">

  <xsl:output method="text"/>
  <xsl:output method="html" indent="yes" name="html"/>


<xsl:template match="/rdf">
  <xsl:for-each select="skos:Concept">
    <xsl:result-document method="xml" href="file_{number()}-output.xml">

          <xsl:copy-of select="../@* | ." />
    </xsl:result-document>
  </xsl:for-each>
</xsl:template> 
</xsl:stylesheet>