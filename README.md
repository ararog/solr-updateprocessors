solr-updateprocessors
=====================

solr-updateprocessors is a set of python scripts that takes advantage of StatelessScriptUpdateProcessorFactory
feature present on Solr 4.0

Right now we have 4 scripts avaliable:

FieldAssigner
FieldReplacer
FieldMapper
FieldLookup

You can find an example on how to configure these script inside solrconfig.xml, please keep in mind that you need
jython available on collection libraries path like below:

SOLR_HOME/conf
         /lib
             /Lib
             jython.jar

Note: The Lib folder is where you will place the jython modules takes from its installed.