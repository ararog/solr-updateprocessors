def processAdd(cmd):
        _fromField = params.get('FromField').strip()
        _toField = params.get('ToField').strip()
        
 	doc = cmd.solrDoc

	_fromValue = doc.getFieldValue(_fromField)
	if _fromValue is not None:
	      	doc.setField(_toField, str(_fromValue))

	logger.info("FieldReplacer#processAdd")	

def processDelete(cmd):
	# no-op
	logger.info("FieldReplacer#processDelete")	

def processMergeIndexes(cmd):
	# no-op
	logger.info("FieldReplacer#processMergeIndexes")	

def processCommit(cmd):
	# no-op
	logger.info("FieldReplacer#processCommit")	

def processRollback(cmd):
	# no-op
	logger.info("FieldReplacer#processRollback")	

def finish():
	# no-op
	logger.info("FieldReplacer#finish")	
