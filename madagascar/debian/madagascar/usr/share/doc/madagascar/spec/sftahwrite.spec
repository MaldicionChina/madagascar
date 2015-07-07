[sftahwrite]
Cat:    RSF/user/karl
Desc:   Read Trace And Header (tah) from standard input, write to separate files
DocCmd: sftahwrite | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d# float  -   -  		delta in the #-th dimension 
LDesc:  (defaults to: (2,...))
Param:  label# string  -   -  		name of each of the axes. 
LDesc:  	   label1 is not changed from input. Each label must be a 
LDesc:  	   header key like cdp, cdpt, or ep.  The trace header 
LDesc:  	   values are used to define the output trace location in
LDesc:  	   the output file. 
LDesc:  (defaults to: (2,...))
Param:  n# largeint  -   -  		number of locations in the #-th dimension 
LDesc:  (defaults to: (2,...))
Param:  o# float  -   -  		origin of the #-th dimension 
LDesc:  (defaults to: (2,...))
Param:  outheaders string  -   -  		
LDesc:  
LDesc:       Output trace header file name.  Default is the input data
LDesc:       file name, with the final .rsf changed to _hdr.rsf. 
LDesc:    
Param:  output string  -   -  		
LDesc:  
LDesc:       output trace filename. Required parameter with no default.
LDesc:    
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    

