[sftahscscale]
Cat:    RSF/user/karl
Desc:   Surface Consistant SCALE - Compute & apply surface consistant scale
DocCmd: sftahscscale | cat
Port:   stdin  rsf r req 	RSF standard input (containing infile data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  endtime float  -   -  		
LDesc:  (defaults to: (n1_traces-1)*d1+o1)
Param:  gxy string  -   -  		
Param:  gxyamp string  -   -  		
Param:  headers string  -   -  		
LDesc:  
LDesc:       Trace header file name.  Default is the input data file
LDesc:       name, with the final .rsf changed to _hdr.rsf 
LDesc:    
Param:  input string  -   -  		
LDesc:  
LDesc:       Input file for traces amplitudes
LDesc:    
Param:  starttime float  -   -  		start time to compute average trace ampltide 
LDesc:  (defaults to: o1)
Param:  sxy string  -   -  		
Param:  sxyamp string  -   -  		
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    

