[sftahfilter]
Cat:    RSF/user/karl
Desc:   Read Trace And Header (tah) from standard input and FILTER
DocCmd: sftahfilter | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  filt_indx_t0 int  -  0 		
LDesc:  
LDesc:       indx to time 0 in the filter.  Must be in the range [0,numfilter)
LDesc:      
Param:  filter float-list  -   -  		 [numfilter]
Param:  filter_file string  -   -  		
LDesc:  
LDesc:       name of the rsf file containing the filter(s)
LDesc:    (auxiliary input file name)
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    

