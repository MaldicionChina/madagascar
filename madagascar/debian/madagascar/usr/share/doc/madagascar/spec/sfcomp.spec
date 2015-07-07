[sfcomp]
Cat:    RSF/user/chen
Desc:   Compare 2 data set
DocCmd: sfcomp | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  mode int  -  0 		compare method: 
LDesc:  	0 - normalized xcorrelation; 
LDesc:  	1 - mean square error 

