<script type="text/javascript">
  var xml = new ActiveXObject("Microsoft.XMLDOM")
  xml.async = false
  xml.load("../DB/CSPS_withLRMI.xml")
  var xsl = new ActiveXObject("Microsoft.XMLDOM")
  xsl.async = false
  xsl.load("split.xsl")
  document.write(xml.transformNode(xsl))
</script>