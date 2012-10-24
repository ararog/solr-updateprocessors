def processAdd(cmd):
        import re
        _regexps = []
        _fromField = params.get('FromField').strip()
        _toField   = params.get('ToField').strip()
        
        filename = params.get('MappingFile').strip()
        if not filename:
            return
        try:
	    f = open(filename, 'r')
            xmlconfig = f.read()
        except:
            logger.info('Error loading mapping file "%s" from path' % filename)
        
        from xml.dom.minidom import parseString
        dom = parseString(xmlconfig)
        
        for attribute in dom.getElementsByTagName("map"):
            f = attribute.getAttribute("from").encode("utf-8")
            if not f:
                logger.info("Missing from attr in map element")
            t1 = attribute.getAttribute("to1").encode("utf-8")
            if not t1:
                logger.info("Missing to attr:to1 in map element")
            try:
                creg = re.compile(f);
                _regexps.append((creg, t1))
            except re.error, e:
                logger.info('Not a valid regexp "%s"' % f)

        dom.unlink()
  
 	doc = cmd.solrDoc

        fromvalue = str(doc.getFieldValue(_fromField));
        for creg, tovalue in _regexps:
            if creg.match(fromvalue)!= None:
                doc.setField(_toField, tovalue)
		break

	logger.info("FieldMapper#processAdd: url=" + fromvalue)	

def processDelete(cmd):
	# no-op
	logger.info("FieldMapper#processDelete")	

def processMergeIndexes(cmd):
	# no-op
	logger.info("FieldMapper#processMergeIndexes")	

def processCommit(cmd):
	# no-op
	logger.info("FieldMapper#processCommit")	

def processRollback(cmd):
	# no-op
	logger.info("FieldMapper#processRollback")	

def finish():
	# no-op
	logger.info("FieldMapper#finish")	
