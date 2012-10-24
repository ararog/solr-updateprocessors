def processAdd(cmd):
        import re
        _regexps = []
        _fromField = params.get('FromField').strip()
        _toField   = params.get('ToField').strip()
        
        filename = params.get('File').strip()
        if not filename:
            return
        try:
		f = open(filename, 'r')
		_entries = f.readlines()
        except:
		logger.info('Error loading source file "%s" from path' % filename)
  
	doc = cmd.solrDoc

	fromvalue = doc.getFieldValue(_fromField)
	for term in _entries:
		term = term.strip()
        	if term in fromvalue:
                	doc.addField(_toField, term)

	logger.info("FieldLookup#processAdd")	

def processDelete(cmd):
	# no-op
	logger.info("FieldLookup#processDelete")	

def processMergeIndexes(cmd):
	# no-op
	logger.info("FieldLookup#processMergeIndexes")	

def processCommit(cmd):
	# no-op
	logger.info("FieldLookup#processCommit")	

def processRollback(cmd):
	# no-op
	logger.info("FieldLookup#processRollback")	

def finish():
	# no-op
	logger.info("FieldLookup#finish")	
