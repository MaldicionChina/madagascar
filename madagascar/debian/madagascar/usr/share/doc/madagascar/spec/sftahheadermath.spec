[sftahheadermath]
Cat:    RSF/user/karl
Desc:   read Trace and Header (tah), compute header values
DocCmd: sftahheadermath | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  output string  -   -  		Describes the output in a mathematical notation. 
Param:  outputkey string  -   -  		name of the header key to put the results of the output equation 
Param:  verbose int  -  1 		
LDesc:  
LDesc:         flag to control amount of print
LDesc:         0 terse, 1 informative, 2 chatty, 3 debug
LDesc:      

