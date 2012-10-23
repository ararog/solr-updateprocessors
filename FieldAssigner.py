def processAdd(cmd):
        _field = params.get('Field').strip()
        _value = params.get('Value').strip()
        
 	doc = cmd.solrDoc

      	doc.addField(_field, _value)

	logger.info("FieldAssigner#processAdd")	

def processDelete(cmd):
	# no-op
	logger.info("FieldAssigner#processDelete")	

def processMergeIndexes(cmd):
	# no-op
	logger.info("FieldAssigner#processMergeIndexes")	

def processCommit(cmd):
	# no-op
	logger.info("FieldAssigner#processCommit")	

def processRollback(cmd):
	# no-op
	logger.info("FieldAssigner#processRollback")	

def finish():
	# no-op
	logger.info("FieldAssigner#finish")	
