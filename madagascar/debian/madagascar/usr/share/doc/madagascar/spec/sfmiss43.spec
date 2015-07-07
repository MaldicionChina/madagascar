[sfmiss43]
Cat:    RSF/user/yliu
Desc:   3-D missing data interpolation with adaptive PEFs
DocCmd: sfmiss43 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0. 		regularization parameter 
Param:  exact enum-bool  -  y 		If y, preserve the known data values 
Param:  mask string  -   -  		optional input mask file for known data (auxiliary input file name)
Param:  niter int  -  100 		Number of iterations 
Param:  verb enum-bool  -  n 		verbosity flag 

