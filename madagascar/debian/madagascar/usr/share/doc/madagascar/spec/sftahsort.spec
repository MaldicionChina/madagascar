[sftahsort]
Cat:    RSF/user/karl
Desc:   Read Trace And Header from separate files in sorted order, write to pipe
DocCmd: sftahsort | cat
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
Param:  sort string  -   -  		
LDesc:  
LDesc:       list of the sort keys.  Each key must be a trace header key name.
LDesc:       It may be preceeded with + (the default) for ascending or - for 
LDesc:       descending sort direction.  The key may be followed with :min,max 
LDesc:       or :min,max,inc.  These parameters allow you to select a subset of 
LDesc:       of the traces based on the header key.  The sort keys are blank
LDesc:       seperated you should enclose the sort string in ''s.  Examples are
LDesc:       sort='iline xline offset' and sort='cdp:100,500,25 offset'
LDesc:    
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    

