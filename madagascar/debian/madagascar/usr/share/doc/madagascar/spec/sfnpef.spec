[sfnpef]
Cat:    RSF/user/gee
Desc:   Estimate Non-stationary PEF in N dimensions
DocCmd: sfnpef | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing flt data)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  a int-list  -   -  		 [dim]
Param:  center int-list  -   -  		 [dim]
Param:  epsilon float  -  0.01 		regularization parameter 
Param:  filt_lag string  -   -  		input file for double-helix filter lags 
Param:  filt_pch string  -   -  		
Param:  gap int-list  -   -  		 [dim]
Param:  lag string  -   -  		output file for filter lags 
Param:  maskin string  -   -  		optional input mask file (auxiliary input file name)
Param:  maskout string  -   -  		optional output mask file 
Param:  niter int  -  100 		number of iterations 
Param:  pch string  -   -  		auxiliary input file name

