[sfmiss]
Cat:    RSF/user/gee
Desc:   Multi-dimensional missing data interpolation
DocCmd: sfmiss | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0. 		regularization parameter 
Param:  exact enum-bool  -  y 		If y, preserve the known data values (when prec=y) 
Param:  lag string  -   -  		optional input file with filter lags (auxiliary input file name)
Param:  mask string  -   -  		optional input mask file for known data (auxiliary input file name)
Param:  n int-list  -   -  		 [dim]
Param:  niter int  -  100 		Number of iterations 
Param:  padin int  -  0 		Pad beginning 
Param:  padout int  -  0 		Pad end 
Param:  prec enum-bool  -  y 		If y, use preconditioning 

