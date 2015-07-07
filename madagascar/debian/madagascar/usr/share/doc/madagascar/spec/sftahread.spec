[sftahread]
Cat:    RSF/user/karl
Desc:   Read Trace And Header from separate files, combine, write to pipe
DocCmd: sftahread | cat
Port:   stdin  rsf r req 	RSF standard input (containing infile data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  headers string  -   -  		
LDesc:  
LDesc:       Trace header file name.  Default is the input data file
LDesc:       name, with the final .rsf changed to _hdr.rsf 
LDesc:    
Param:  input string  -   -  		
LDesc:  
LDesc:       Input file for traces amplitudes
LDesc:    
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    

