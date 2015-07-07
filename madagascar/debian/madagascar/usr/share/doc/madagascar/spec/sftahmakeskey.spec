[sftahmakeskey]
Cat:    RSF/user/karl
Desc:   Trace And Header MAKE Secondary KEY
DocCmd: sftahmakeskey | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  key string-list  -   -  		 [numkeys]
Param:  skey string  -   -  		The name of the secondary key created by the program. 
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    

