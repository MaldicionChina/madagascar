[sftahstack]
Cat:    RSF/user/karl
Desc:   Read Trace And Header (tah) from STDIN, stack matching header keys
DocCmd: sftahstack | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  key string-list  -   -  		 [numkeys]
Param:  ntaper int  -  12 		
LDesc:  
LDesc:         length of the taper on the stack mute
LDesc:      
Param:  tmute float-list  -   -  		 [numtmute]
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    
Param:  xmute float-list  -   -  		 [numxmute]

